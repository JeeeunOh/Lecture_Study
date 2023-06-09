핸드쉐이크 중 인증방식은 DH 1.2 핸드쉐이크, DH 1.3 핸드쉐이크, RSA 다 됨.

**💡 handshake 과정에서 일어나는 것???**

- 프로토콜 버전 협상
- 암호화 알고리즘 선택
- 비대칭 암호화 방식으로 서로 인증
- 다음 단계에서 대칭 암호화에 사용할 공유 비밀 키를 설정

→ 인증 및 키 교환

<br/>

**💡 RSA handshake**

![image](https://github.com/JeeeunOh/Univ-Lecture/assets/65931227/417c5eda-3d48-4ca0-b2ef-16f0577b6408)


공개키, 개인키 쌍을 생성해서 사용함. 

서버는 공개키를 클라이언트에게 제공하고, 클라이언트는 세션키를 생성한 후 서버의 공개키를 암호화하여 서버에 전송함. 서버는 개인키를 사용하여 암호문을 복호화하고 세션키를 얻음. 

→ 안전하고 신뢰성이 높지만, 연산량이 높아 성능 이슈 있음.

![image](https://github.com/JeeeunOh/Univ-Lecture/assets/65931227/af4eeabf-3042-4a89-9f45-889ebb69af28)

<br/>

**💡 DH 1.2 handshake**

클라이언트, 서버 간 공개 매개변수를 공유하고 비밀키를 생성하여 사용함.

→ 중간 값이 노출되어도 비밀키를 유추하기 어려움 → 안전성이 높음!!!!

<br/>

**💡 DH 1.3 handshake**

TLS 1.3에서 새롭게 도입된 키 교환 방식. 

ECDH를 기반으로 함. ECDH는 타원 곡선을 사용하여 키 교환 수행

→ 기존 DH 방식보다 더 효율적인 연산 제공

![image](https://github.com/JeeeunOh/Univ-Lecture/assets/65931227/b09f0a10-14c9-463f-8687-5a8322f939ae)

<br/>

**💡 AEAD란?**

인증된 암호화를 의미. 메시지의 기밀성과 무결성을 함께 제공하는 암호화 방식.

<br/>

**💡 AEAD가 도입된 이유?**

기존의 CBC모드와 RC4은 이전 버전의 TLS에서 사용되었지만, 보안 결함이 발견되어 TLS 1.3에서 제거 → AEAD 도입

AEAD는 CBC와 RC4보다 보안성과 성능 면에서 더 우수한 암호화 방식으로 인정받고 있음.

[미디엄 블로그 링크](https://medium.com/@techschool.guru/a-complete-overview-of-ssl-tls-and-its-cryptography-system-31336a85c278) 

![image](https://github.com/JeeeunOh/Univ-Lecture/assets/65931227/6389d07e-8911-41cc-be1e-5c419a036221)


MAC과 암호화된 메시지가 수신자에게 전송됨.

이 때, TLS 1.3에서는 암호화된 메시지 외에도 주소, 포트, 프로토콜 버전, 시퀀스 번호 같은 데이터 인증함. 

→ 이 데이터를 MAC의 입력값으로 넣기도 함.

이런 추가 데이터들로 인증된 암호화 방식을 AEAD라고 함.

![image](https://github.com/JeeeunOh/Univ-Lecture/assets/65931227/9421f0b6-3823-4740-b144-7668e186e849)


이렇게 암호화된 메시지는 비밀키, nonce와 함께 MAC 알고리즘으로 해독됨.

→ 수신자는 이렇게 해독된 MAC값과 수신한 MAC 값 비교해서 메시지 무결성 확인 가능.

![image](https://github.com/JeeeunOh/Univ-Lecture/assets/65931227/b70c67a6-d6ce-4b6d-9651-4642a4e82d55)

<br/>

**💡 Client Hello**

2 개의 공개 키 ( 디피헬만용, Curve 디피헬만용 ) 공유 → 어떤 알고리즘이던 공유 비밀키 계산 가능

지원하는 서명 알고리즘 목록 제공

<br/>

**💡 Server Hello**

서버를 인증할 수 있는 인증서 담아 보냄.

위 과정을 거치고 나서는, 그 후로는 축약된 핸드셰이크 수행

→ 클라이언트와 서버가 서로를 인증한 후이기 때문에 다시 인증할 필요가 없음.

![image](https://github.com/JeeeunOh/Univ-Lecture/assets/65931227/df141355-e874-4796-824b-858e0785c1b2)

<br/>

**💡 다음 hello 부터 주고 받는 것?**

이전 핸드쉐이크에서 얻었던 PSK ID 목록 보냄. 

디피헬만 모드의 PSK가 사용되는 경우, 클라이언트도 디피헬만 공개키를 공유해야함.

→ 서버가 전체 핸드쉐이크로 돌아갈 수 있음.

이 hello를 받은 서버는 선택한 사전 공유 키 ID, 선택한 디피헬만 공개키를 돌려줌

→ 클라이언트는 데이터를 보내기 위해 핸드쉐이크가 완료될 때까지 기다릴 필요 X

<br/>

Q. FULL보다 간소화된 handshake에서 어떻게 서버와 클라이언트가 서로를 신뢰??

TLS 1.3에서는 **Pre-Shared Key (PSK)를 사용하여 핸드쉐이크를 간소화** 가능.

→ PSK를 사용하면 기존에 사용된 암호화 키를 다시 사용 가능 

→ 핸드쉐이크가 더욱 빠르고 효율적이게 됨.

<br/>

**PSK 티켓** : 핸드쉐이크가 끝난 후에도 서버는 클라이언트에 대한 정보를 저장. 만료기한 있음.

→ 클라이언트는 이를 사용하여 이전에 핸드쉐이크한 서버와 더욱 빠르고 효율적으로 핸드쉐이크를 수행 가능

<br/>

**장점 )** 핸드쉐이크의 성능을 향상 & 보안성 유지

![image](https://github.com/JeeeunOh/Univ-Lecture/assets/65931227/9498e1d7-c21a-4c1a-8a28-a96831688132)


- TLS 1.3에서는 RSA 같은 키 교환 방식이 제거됨 → 더 안전한 키 교환 메커니즘으로 교환
- TLS 1.2보다 왕복 1회 이상 빠름.
- TLS의 대칭 암호화는 AEAD가 필수 → 더 안전함.
   CBC, RC4 같은 약한 알고리즘 제거
