### 웹과 HTTP의 이해_웹 서비스의 이해 (p176~182)

1. HTTP 메소드
    
    GET : 데이터가 주소 입력란에 표시됨 → 취약
    
2. HTTP 응답
    1. 200 : 성공적으로 수행
    2. 403 : 서비스 요청 거부
    3. 404 : 원하는 문서 찾을 수 없음.
    4. 500 : 서버에 불가피한 오류 발생.
3. HTML, CSS, JS
4. 프론트엔드, 백엔드

### 웹 해킹 (p181~192)

1. 웹 취약점 스캐너를 통한 정보 수집
    
    장점 ) 빠르게 다양한 접속 시도 가능
    
    단점 ) 보안 문제가 있는 취약점이 아닌 경우가 많음.
    
2. 웹 프록시를 통한 취약점 분석
    
    클라이언트 ↔ 서버 ↔ 브라우저 간 모든 HTTP 패킷 확인, 수정 가능
    

### 구글 해킹을 통한 정보 수집 (p192~195)

- site:wishfree.com admin : 특정 도메인에서 문자열 검색
- filetype:txt password : 특정 파일 확장자에서 문자열 들어간 파일 검색
- intitle:index.of admin : 디렉터리 리스팅 가능한 사이트 검색

**검색 엔진의 검색을 피하는 방법)**

1. 구글 검색 엔진 / 모든 검색 로봇 검색 막기.
2. 특정 파일 접근 막기 : ex. dbconn.ini, admin

### 웹 취약점과 보안 (p196~215)

**웹의 취약점 )**

1. **명령 삽입 취약점 :** SQL 문 주의
2. **인증 및 세션 관리 취약점 :** 취약한 패스워드 설정 ‘ or ‘’=‘
3. **XSS 취약점 :** 공격자가 작성한 스크립트가 다른 사용자에게 전달됨.
4. **취약한 접근 제어**
    1. 인증된 사용자가 수행할 수 있는 것에 대한 제한 제대로 X
    
    ex. 디렉터리 탐색
    
5. **보안 설정 오류**
    1. 디렉터리 리스팅
    2. 백업 및 임시 파일 존재
    3. 미흡한 주석 관리
    4. 파일 업로드 제한 부재
    5. `리버스 텔넷` : 방화벽이 있는 시스템 공격할 때 자주 사용
6. **민감한 데이터 노출** : 데이터 중요도 따른 암호화 로직 사용 필요
7. **공격 방어 취약점**
8. **CSRF 취약점**
    
    불특정 다수 대상으로 로그인 된 사용자가 자신의 의지와 무관하게 공격자 의도대로 하게 하는 공격
    
    **XSS** : 악성스크립트가 클라이언트에서 실행
    
    **CSRF** : 사용자가 악성스크립트를 서버에 요청
    
9. **취약점 있는 컴포넌트 사용**
10. **취약한 API**

**보완방법 )**

1. 특수 문자 필터링 : XSS 취약점 공격 방어 가능
2. 서버 통제 작용 
3. 지속적인 세션 관리
