## 📌 TOR

<img src="https://github.com/JeeeunOh/Major-Study/assets/65931227/52eaf488-20a3-4aee-86a5-106dc98a766f" height="400px" width="700px">
<img src="https://github.com/JeeeunOh/Major-Study/assets/65931227/6b780af8-dbcb-4d39-b00e-016c20242c3f" height="400px" width="700px">

<br/>

**💡 TOR이란??**

TOR을 사용하면 실제 사용자의 IP주소를 숨길 수 있음. ( 라우터의 input, output 값이 다름. )

<img src="https://github.com/JeeeunOh/Major-Study/assets/65931227/76685e8b-c2ca-4033-9e18-1c101d9d00b6" height="300px" width="600px">

<br/>
<br/>

**💡 TOR connection establishment 방법???**

- OR1, OR2와 각각 디피헬만키 알고리즘 사용해서 키 교환
- TOR 연결 과정에서 디피헬만키를 이용해서 사용자의 익명성과 보안을 제공함.

<img src="https://github.com/JeeeunOh/Major-Study/assets/65931227/386d4ee7-0003-453d-84b9-da86380b85a3" height="300px" width="600px">

<br/>
<br/>

**💡 TOR을 사용한 DDoS 공격을 막는 방법??**

input이 많을 때, 트래픽 유추가 가능함.

노드들이 트래픽을 전달할 때 일정한 패턴을 보이는 경우가 있을 수 있고 이를 통한 추측 가능.

exit node를 보면 됨.

→ 다음 시간에 이어서 함.

## 📌 DFD

**💡 Website Fingerprinting이란???**

TOR 사용자가 방문하는 웹사이트를 추적하기 위한 기술 중 하나로 공격기법.

input → 라우터 → output 로 가는 이미지나 패킷 등을 분석한다.

방어 방법 )

이런 트래픽 학습을 막기 위해, 암호화 데이터를 사용하기도 함.

→ 매 세션마다 암호화 키가 달라지고 암호화 데이터가 달라짐.

but, 온전하지 않음. 암호화 데이터 통해서도 패턴, 암호화 데이터 길이 등을 통해 학습이 가능함.

<br/>

**💡 Adversarial Examples란??**

Website Fingerprinting 같은 공격을 공격함 → 결국엔 방어 의미

방법 ) **misclassification 유도**

1. **`targeted attack`**
    
    A를 B로 오해하게 하는 것
    
    장점 ) powerfull  / 단점 ) 더 어려움.
    
2. **`untargeted attack`**
    
    A를 정답이 아닌 아무거나로 오해하게 하는 것.
    
    - 장점 : 더 쉬움
    - 단점 : weak

<br/>

**💡 closed-world vs open-world ??**

**`closed-world` :** 

사용자가 방문할 수 있는 웹사이트 한정적 

→ 공격자는 웹사이트 샘플을 보유하고 있으므로 모델의 훈련이 가능함.

**`open-world`** : 

더 현실적인 설정 가정. 

공격자는 웹사이트 집합 중 일부만 훈련 가능.

공격자는 제한된 정보로 모델을 구축 

→ 공격자의 정확성 제한, 사용자 웹사이트 방문 추적 능력 제한

<br/>

**💡 Adversary의 목표???**

신뢰도 감소, untargeted misclassification, targeted misclassification

<br/>

**💡 Deep Fingerprinting Defender의 역할??**

**실제 통신 데이터에 가짜 메시지 삽입 → 패킷 흐름 패턴 변조**

→ 네트워크에서 사용자의 특성을 식별하는 공격을 방어

<br/>

**💡 DNN ? CNN ?**

DNN은 각 뉴런이 완전히 연결되어있음 → 전체 데이터를 한번에 처리

CNN은 이미지 처리에서 탁월

<br/>

**💡 결론**

**`DFD`** 을 사용하면 딥러닝 기반 WF(Wireless Fingerprinting) 공격 효과를 완화할 수 있었음. 

→ 사용자의 개인정보 보호와 네트워크 보안을 강화하는 데 도움이 됨.
