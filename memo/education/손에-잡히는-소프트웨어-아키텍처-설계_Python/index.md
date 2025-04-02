- description : (education정리) 손에-잡히는-소프트웨어-아키텍처-설계_Python
- tag : education , summary , my-summary , python , design , pattern , architecture
- date : 

TOC


-------

<H1>손에-잡히는-소프트웨어-아키텍처-설계_Python</H1>

# 1. 【한글자막】 소프트웨어 아키텍처 및 대규모 시스템 설계
- URL : https://lg.udemy.com/course/software-architecture-design-large-scale-systems/learn/lecture/30800568?learning_path_id=9371175#overview
- [pdf 강의 워크북](./Software_Architecture_and_Design_of_Large_Scale_Systems-Workbook.pdf)

## 1.1. 섹션2 : 시스템 요구사항 및 아키텍처 드라이버
### 1.1.1. T3. 시스템 설계 및 아키텍처 다이렉트 드라이버 개요
- Features/Functional Requirement
  - What "system must do"
- Quality Attributes / Non-Functional Requirement 
- System Requirement
  - Time / Financial / Staffing constraints
### 1.1.2. T4. 기능 요구 사항 - 단계적 과정
- gathering
  - use cases
  - user flows : step-by-sep
- steps
  - identify all the actors / users in our system
  - capture  and describe all the possible use-cases / scenarios
  - user flow - expand each use case through flow of events (event : action / data)
- UML (Unified Modeling Language) - Sequence Diagram
  - action들이 API 가 되는 것이다.
### 1.1.3. T5. 시스템 품질 속성 요구 사항
- important considerations
  - measurable / testable
  - trade off - ex) performance & security
  - feasibility - ex) unrealistically low latency / 100% availability
### 1.1.4. T6. 시스템 제약 사항
- it is not always bad.
- types of contraints
  - technical
  - business : deadline , budget
  - legal

## 1.2. 섹션3: 대규모 시스템에서 가장 중요한 품질 속성
### 1.2.1. T7. 성능
### 1.2.2. T8. 확장성
### 1.2.3. T9. 가용성 - 개요 및 측정
### 1.2.4. T10. 내결함성 및 고가용성
### 1.2.5. T11. SLA, SLO, SLI
### 1.2.6. T12. 업계 SLA 예시
## 1.3. 섹션4: API 설계
### 1.3.1. T13. API 설계 개요
### 1.3.2. T14. RPC
### 1.3.3. T15. 인기 있는 RPC 프레임워크
### 1.3.4. T16. REST API
## 1.4. 섹션5: 대규모 시스템에 필요한 아키텍처 빌딩 블록
### 1.4.1. T17. DNS, 로드 밸런싱 및 GSLB
### 1.4.2. T18. 로드 밸런싱 솔루션
### 1.4.3. T19. 메시지 브로커
### 1.4.4. T20. 메시지 브로커 솔루션
### 1.4.5. T21. API 게이트웨이
### 1.4.6. T22. API 게이트웨이 솔루션
### 1.4.7. T23. 콘텐츠 전송 네트워크
### 1.4.8. T24. 콘텐츠 전송 네트워크 솔루션
## 1.5. 섹션6: 글로벌 규모의 데이터 스토리지
### 1.5.1. T25. 관계형 데이터베이스 및 ACID 트랜잭션
### 1.5.2. T26. 비관계형 데이터베이스
### 1.5.3. T27. 비관계형 데이터베이스 - 솔루션
### 1.5.4. T28. 데이터베이스의 가용성과 확장성, 성능을 개선하는 기술
### 1.5.5. T29. Brewer의 (CAP) 정리
### 1.5.6. T30. 확장 가능한 비정형 데이터 스토리지
### 1.5.7. T31. 확장 가능한 비정형 데이터 스토리지 - 클라우드 및 오픈 소스 솔루션
## 1.6. 섹션7: 소스트웨어 아키텍처 패턴
### 1.6.1. T32. 소프트웨어 아키텍처 패턴 개요
### 1.6.2. T33. 멀티티어 아키텍처
### 1.6.3. T34. 마이크로서비스 아키텍처
### 1.6.4. T35. 이벤트 기반 아키텍처
## 1.7. 섹션8: 빅 데이터 아키텍처 패턴
### 1.7.1. T36. 빅 데이터 개요
### 1.7.2. T37. 빅 데이터 처리 방식
### 1.7.3. T38. 람다 아키텍처
## 1.8. 섹션9: 소스트웨어 아키텍처 & 시스템 디자인 연습
### 1.8.1. T39. 확장성이 높은 포럼 디자인 1 - 요구 사항 & API
### 1.8.2. T40. 확장성이 높은 포럼 디자인 2 - 기능 아키텍처 다이어그램
### 1.8.3. T41. 확장성이 높은 포럼 디자인 3 - 소프트웨어 아키텍처 완성
### 1.8.4. T42. 인터넷 쇼핑몰 플랫폼 디자인 1 - 요구 사항 & 시퀀스 다이어그램
### 1.8.5. T43. 인터넷 쇼핑몰 플랫폼 디자인 2 - 기능 다이어그램
### 1.8.6. T44. 인터넷 쇼핑몰 플랫폼 디자인 3 - 소프트웨어 아키텍처 완성
## 1.9. 섹션10: 보너스 섹션
### 1.9.1. T45. 보너스 강의 - 계속 공부하기


# 2. Python OOP - Object Oriented Programming for Beginners

# 3. Design Patterns in Python