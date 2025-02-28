- description : dreamhack (LGE 해킹대회 사전 교육) 관련 정리하던 것으로 , 제대로 끝내지 못한 교육이었음.
- tag : dreamhack , education
- date : 2024-01-01

# history
- 9월 ~ 12월

# 2023 LGE 해킹대회 사전교육 2차수 - 드림 비기너즈
- 내용들은 읽어보면 된다.
## simple-operation
- binary를 disassemble해야 하는 것이다.  IDA 라는 툴을 이용해야 한다.
  - 실행이 vpc안에서만 c code로 변환하는 기능이 유용하다. 밖에서 되는 것은 돈을 주고 사야 한다. 
- 다음 disassemble된 코드를 보고 Congrats! 가 나오도록 input을 입력하면 된다. 
```
int __fastcall main(int argc, const char **argv, const char **envp)
{
  char s1[9]; // [rsp+6h] [rbp-3Ah] BYREF
  char s[9]; // [rsp+Fh] [rbp-31h] BYREF
  unsigned int v6; // [rsp+18h] [rbp-28h] BYREF
  unsigned int v7; // [rsp+1Ch] [rbp-24h] BYREF
  char *s2; // [rsp+20h] [rbp-20h]
  int fd; // [rsp+2Ch] [rbp-14h]
  void *buf; // [rsp+30h] [rbp-10h]
  unsigned int v11; // [rsp+38h] [rbp-8h]
  int i; // [rsp+3Ch] [rbp-4h]

  v7 = 0;
  v6 = 0;
  v11 = 0;
  initialize(argc, argv, envp);
  buf = malloc(0x45uLL);
  fd = open("./flag", 0);
  read(fd, buf, 0x45uLL);
  close(fd);
  get_rand_num(&v6);
  printf("Random number: %#x\n", v6);
  printf("Input? ");
  __isoc99_scanf("%d", &v7);
  v11 = v6 ^ v7;
  snprintf(s, 9uLL, "%08x", v6 ^ v7);
  for ( i = 0; i <= 7; ++i )
    s1[i] = s[7 - i];
  printf("Result: %s\n", s1);
  s2 = "a0b4c1d7";
  if ( !strcmp(s1, "a0b4c1d7") )
  {
    puts("Congrats!");
    puts((const char *)buf);
  }
  else
  {
    puts("Try again");
  }
  return 0;
}
```

- 이를 해석해서 관련 쉽게 처리하는 python을 만들어 처리하면 된다.
  - v7 (input) = v6 (random) ^ v11 (0x7d1c4b0a)

## 64se64
- base64 decode

## baby-linux
- cat dreamhack/.../*.txt

## Exercise: SSH
- ssh chall@host3.dreamhack.games -p 12770 cat flag

## ex-reg-ex
- drwwwwwwe3am@lge.com

## phpreg
- id : dnnyangyang0310
- passwd : @44319!+1+13
- command : cat ../dream/f*g.txt