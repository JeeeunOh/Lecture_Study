누가 해킹하거나, 잘못된 접근을 했을 때 시스템은 어떤 유저가 잘못된 접근 권한으로 접근했는지 알아야 함.

- ****identification****
    - 보안 시스템에 식별자 제공 ex. id, pw
- ****verification****
    - 인증 정보를 제시하거나 생성함.

<br/>

💡 ****user identity를 authenticate(인증) 하기위한 수단****

1. individual knows : 내가 나온 초등학교가 어딘지 등
2. individual posses : 열쇠, 학생증 등
3. static biometrics : 지문, 홍채, 얼굴 등
4. dynamics biometrics : 보이스패턴, 서체 등

<br/>

💡 **Password Authentication**

유저가 아이디, 비번을 데이터베이스에 저장해놓으면 나중에 시스템에서 유저가 아이디, 비번으로 로그인할 때 이 유저가 실제로 있는지 없는지를 판별함.

이전의 이슈 : etc/passwd 에 들어가면 해시코드나 솔트를 다 볼 수 있었다. 

→ 일반 유저가 해킹 가능했다.

현재 : 패스워드를 모아놓은 파일은 일반 유저들은 읽을 수 없고 관리자만 읽을 수 있음

→ 패스워드 관련돼서 별 이슈가 없다.

<br/>

💡 ****Password Cracking****

1. Dictionary attacks
    
    사전에 있는 단어들 하나씩 다 도전
    
2. Rainbow table attacks
    
    해시함수를 사용하여 만들어낼 수 있는 값들을 왕창 저장한 표
    
    영어 소문자와 숫자 조합으로 일정 길이까지의 모든 문자열에 대해서 계산한다거나 하는 것
    
<br/>

💡 **Password Selection Techniques**

1. user education
    1. 빡센 비밀번호 만들기 위해 유저 교육
2. computer generated passwords
    1. 어려운 비밀번호 → 외우기 힘듦
3. reactive password checking
    1. password 크래커가 주기적으로 암호 생성
4. proactive password checking
    1. passwords 크래커가 가지고 있는 암호면 리젝
    2. 사용자가 외우기 쉬우면서 암호크래커가 접근하기 어려운 암호 생성 유도

<br/>

💡 **Biometric Authentication**

패스워드는 고정 string → 매칭 쉬움. but, 생체 인증은 어려움

다만 생체 인증 정보는 바꿀 수 없다는 단점이 있음.

<br/>

💡 **Remote User Authentication**

공개키, 개인키의 개념 시작….!

`공개키` : public key : 누구나 접근 가능

`개인키` : private key : 특정 유저만 접근 가능

`공개키 암호 방식 (public-key cryptography)/ 비대칭키 암호 (asymmetric-key algorithm)`

1. **키 이용 방식 )** 
    
    공개키암호 - 공개키 : 암호화 사용 / 개인키 : 복호화 사용
    
    공개키서명 - 공개키 : 서명 검증 / 개인키 : 서명 생성
    
2. **A ↔ B 통신 과정 )**
    1. A가 메시지를 B의 공개키로 암호화 → 암호문 생성
    2. B는 암호문을 B의 개인키로 복호화 → 메시지 원본 생성
    
    → 이 때 암호문 생성 과정에서 리플레이 어택을 막기 위해 
    
    **Time stamp, random nonce**를 집어넣기도 함.
    
3. **종류 )**
    1. `공개 키 암호` : 특정 비밀키 가지고 있는 사용자만 열어볼 수 있음.
        
        ex. 공개키만 알면 누구나 편지를 넣을 수 있지만 개인키를 가진 사람만 내용을 확인 가능.
        
        ex. RSA
        
    2. `공개 키 서명` : 특정 비밀키로 만들었다는 것을 누구나 확인 가능
        
        ex. 봉인한 편지는 누구나 열어볼 수 있지만 인장확인을 통해 
        
        인장을 소유한 발신자가 이 편지를 보냈음을 증명 가능
        

후에 같은 키로 암호화 & 복호화하는 것도 배움 : `대칭키 암호 (symmetric-key algorithm)`

→ 같은 키 이용하는게 속도가 더 빠름

ex. `TLS` : 공개키 암호 알고리즘으로 대칭키 암호 알고리즘의 공통키 공유

→ 그 키 기반으로 실제 통신의 암호화 구조에 사용함.

<br/>

💡 **FIDO ( Fast ID Online )**

1. user가 생체정보 이용해서 스마트폰에 접근
2. 스마트폰의 개인키에 접근 가능
3. 스마트폰(개인키) ↔ 서버(공개키) 간 안전하게 통신함.

<br/>

💡 **Authentication Security Issues**

1. eavesdropping
2. host attacks
3. replay
4. client attacks
5. trojan horse
6. denial-of-service
