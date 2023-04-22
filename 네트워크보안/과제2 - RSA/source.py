import random;

# 1 ~ pow(2, 16) 범위의 소수 리스트 리턴
def get_prime():
    prime = []
    for num in range(1, pow(2, 16)):
        if num > 1:
            for i in range(2, round(num/2)):
                if (num % i) == 0:
                    break
            else:
                prime.append(num)
    return prime

# a, b 서로수 여부 판별
def gcd(a,b):
	if (a<b): return gcd(b,a)
	if (a%b) == 0: return b
	return gcd(b, a % b)

# e 구하는 함수
# 2 ~ phi 사이면서 phi와 서로수인 e를 구함.
def get_e(phi):
    while(True):
        e = random.randint(2, phi)
        if(gcd(e, phi)==1): return e

# d 구하는 함수
# e*d를 phi로 나누었을 때 나머지가 1인 d를 구함.
def get_d(e, phi):
    new_d = phi-1
    while(True):
        if((new_d*e)%phi==1): break
        new_d-=1
    
    return new_d

prime = get_prime()

# p, q는 소수 리스트 중 랜덤으로 하나 선택
p = prime[random.randint(1, len(prime)-1)]
q = prime[random.randint(1, len(prime)-1)]
n = p*q
phi = (p-1)*(q-1)

print('p = ', p)
print('q = ', q)
print('N = ', n)
print('phi = ', phi)

e = get_e(phi) # 공개키
d = get_d(e, phi) # 개인키
M = 12345

print('e = ', e)
print('d = ', d)
print('Message Input : ', M)

C = pow(M, e)%n # 공개키로 암호화
guessM = pow(C, d)%n # 개인키로 복호화
print('**Encryption - cipher = ', C)
print('**Decryption - decrypted cipher = ', guessM)