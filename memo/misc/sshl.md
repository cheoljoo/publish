- description : support more than two services through 1 port (sshl) : sshl -> ssh or http
- tag : misc , sshl, ssh, http
- date : 2025-08-04



# sshl
```txt
╭─────────────────────────────────────────────────────────────────────────────────────────────────────╮
│  > 현재 22443 port 번호로 ssh를 사용하고 있다. 이 port를 이용하여 https 나 http를 운영할수 있는가?  │
╰─────────────────────────────────────────────────────────────────────────────────────────────────────╯

✦ 아니요, 일반적으로 하나의 포트 번호는 하나의 서비스(프로세스)만 사용할 수 있습니다. 따라서 SSH 서비스가 22443 포트를 사용하고 있다면, 웹 서버(HTTP/HTTPS)가 동시에 같은 22443 포트를
  직접 사용하는 것은 불가능합니다.

  하지만 포트 멀티플렉서(Port Multiplexer) 와 같은 도구를 사용하면 이 문제를 해결할 수 있습니다. 가장 대표적인 도구는 sslh 입니다.

  sslh의 작동 방식

  sslh는 특정 포트(예: 22443)에서 연결을 받은 다음, 들어오는 트래픽의 프로토콜을 감지하여 내부적으로 다른 포트에서 실행 중인 실제 서비스로 전달해주는 역할을 합니다.

  예를 들어 다음과 같이 설정할 수 있습니다.

   1. `sslh` 가 외부 포트 22443 에서 연결을 기다립니다.
   2. SSH 서버는 내부 포트(예: localhost:22)에서 실행됩니다.
   3. 웹 서버 (HTTPS) 는 다른 내부 포트(예: localhost:443)에서 실행됩니다.

  이제 사용자가 22443 포트로 접속하면 sslh가 다음을 판단합니다.

   * SSH 클라이언트가 접속하면 -> SSH 프로토콜임을 감지하고 트래픽을 localhost:22 로 전달합니다.
   * 웹 브라우저가 접속하면 -> TLS/SSL (HTTPS) 프로토콜임을 감지하고 트래픽을 localhost:443 으로 전달합니다.

  이렇게 하면 사용자는 동일한 your-domain.com:22443 주소와 포트 번호를 사용하여 SSH와 HTTPS 두 가지 서비스를 모두 이용할 수 있게 됩니다.

  결론: 직접적으로는 불가능하지만, sslh와 같은 프로토콜 멀티플렉서를 이용하면 가능합니다.

╭─────────────────────────────────────╮
│  > sshl 은 어떻게 설정을 하는지요?  │
╰─────────────────────────────────────╯

✦ 네, sslh 설정 방법을 단계별로 안내해 드리겠습니다. 이 예제는 사용자의 요청에 맞춰 SSH와 HTTPS 트래픽을 22443 포트 하나로 받는 것을 기준으로 합니다.

  설정 개요

   * 외부 포트: 22443 (sslh가 이 포트에서 대기)
   * 내부 SSH 포트: 22 (sshd가 이 포트에서 대기)
   * 내부 HTTPS 포트: 443 (웹서버가 이 포트에서 대기)

  ---

  1단계: sslh 설치

  먼저 사용 중인 리눅스 배포판에 맞는 명령어로 sslh를 설치합니다.

  Debian / Ubuntu:

   1 sudo apt-get update
   2 sudo apt-get install sslh

  CentOS / RHEL / Fedora:
   1 sudo yum install sslh
   2 # 또는 dnf
   3 sudo dnf install sslh

  ---

  2단계: 기존 서비스 설정 변경

  sslh가 22443 포트를 사용해야 하므로, 기존에 22443 포트를 사용하던 SSH 서버의 포트를 변경해야 합니다.

  SSH 서버 (sshd) 설정

   1. SSH 설정 파일을 엽니다.

   1     sudo nano /etc/ssh/sshd_config

   2. Port 지시어를 찾아 22로 변경하거나, 주석(#)이 있다면 해제하고 22로 설정합니다. 기존에 Port 22443 이었다면 Port 22로 수정합니다.

   1     #Port 22
   2     ListenAddress 0.0.0.0
      위와 같이 되어있다면 #을 제거하고 Port 22로 바꿔주세요.

   3. SSH 서비스를 재시작합니다. (아직 연결은 끊지 마세요!)
   1     sudo systemctl restart sshd

  웹 서버 (Nginx/Apache) 설정

  웹 서버가 localhost:443 또는 127.0.0.1:443에서 HTTPS 연결을 수신하도록 설정해야 합니다. 외부에서 직접 443 포트로 접근하는 것이 아니라, sslh가 전달해주는 트래픽만 받도록 하는 것이
  좋습니다.

  Nginx 예시 (`/etc/nginx/sites-available/default` 등):

    1 server {
    2     # listen 443 ssl; # 이 줄 대신 아래와 같이 변경
    3     listen 127.0.0.1:443 ssl;
    4
    5     server_name your_domain.com;
    6
    7     ssl_certificate /path/to/your/cert.pem;
    8     ssl_certificate_key /path/to/your/key.pem;
    9
   10     # ... 나머지 설정
   11 }

  Apache 예시 (`/etc/apache2/ports.conf` 및 가상 호스트 파일):
  ports.conf 파일에서:

   1 Listen 443
  가상 호스트 파일 (<VirtualHost> 블록)에서:

   1 <VirtualHost 127.0.0.1:443>
   2     ServerName your_domain.com
   3     # ... SSL 및 기타 설정
   4 </VirtualHost>

  설정 변경 후 웹 서버를 재시작합니다.
   1 sudo systemctl restart nginx  # 또는 apache2

  ---

  3단계: sslh 설정 파일 수정

  배포판에 따라 설정 파일 위치와 형식이 다릅니다.

  A) Debian / Ubuntu (/etc/default/sslh)

  이 파일은 sslh 데몬의 시작 옵션을 정의합니다.

   1. 설정 파일을 엽니다.

   1     sudo nano /etc/default/sslh

   2. RUN=yes 로 변경하여 sslh가 실행되도록 합니다.
   1     RUN=yes

   3. DAEMON_OPTS 부분을 다음과 같이 수정합니다.

   1     DAEMON_OPTS="--user sslh --listen 0.0.0.0:22443 --ssh 127.0.0.1:22 --ssl 127.0.0.1:443 --pidfile /var/run/sslh/sslh.pid"

  각 옵션 설명:
   * --user sslh: sslh 권한으로 실행 (보안 강화)
   * --listen 0.0.0.0:22443: 외부에서 22443 포트로 들어오는 모든 연결을 받음
   * --ssh 127.0.0.1:22: SSH 트래픽이면 로컬호스트의 22번 포트로 전달
   * --ssl 127.0.0.1:443: SSL/TLS(HTTPS) 트래픽이면 로컬호스트의 443번 포트로 전달
   * --pidfile ...: 프로세스 ID 파일 경로

  B) CentOS / RHEL (/etc/sslh.cfg)

  이 파일은 sslh의 설정을 직접 정의합니다.

   1. 설정 파일을 엽니다.

   1     sudo nano /etc/sslh.cfg

   2. 파일 내용을 다음과 같이 수정합니다.

    1     verbose: false;
    2     foreground: false;
    3     pidfile: "/var/run/sslh/sslh.pid";
    4     user: "sslh";
    5
    6     listen:
    7     (
    8         { host: "0.0.0.0"; port: "22443"; }
    9     );
   10
   11     protocols:
   12     (
   13         { name: "ssh"; host: "127.0.0.1"; port: "22"; },
   14         { name: "ssl"; host: "127.0.0.1"; port: "443"; }
   15     );

  ---

  4단계: sslh 서비스 시작 및 활성화

  이제 sslh 서비스를 시작하고, 부팅 시 자동으로 실행되도록 활성화합니다.

   1 sudo systemctl start sslh
   2 sudo systemctl enable sslh

  서비스 상태를 확인하여 오류가 없는지 확인합니다.
   1 sudo systemctl status sslh
  active (running) 상태가 표시되면 정상입니다.

  ---

  5단계: 방화벽 설정

  방화벽에서 22443 포트를 열어주어야 합니다.

  ufw (Ubuntu/Debian):

   1 sudo ufw allow 22443/tcp
   2 sudo ufw reload

  firewalld (CentOS/RHEL):

   1 sudo firewall-cmd --permanent --add-port=22443/tcp
   2 sudo firewall-cmd --reload

  ---

  6단계: 최종 테스트

  이제 다른 컴퓨터에서 22443 포트를 통해 SSH와 HTTPS 접속을 테스트합니다.

  SSH 테스트:

   1 ssh your_username@your_domain.com -p 22443

  HTTPS 테스트:
  웹 브라우저에서 주소창에 https://your_domain.com:22443 을 입력하여 접속합니다.

  이제 모든 설정이 완료되었습니다. 하나의 포트로 두 가지 서비스를 모두 이용할 수 있습니다.

```
