# 8자리까지 발굴해보기

import hashlib
from string import*  
from itertools import permutations

file_path = '/Users/jieun/Documents/GitHub/Univ-Lecture/네트워크보안/패스워드크랙킹/1MillionPassword_hashed.txt'
f = open(file_path)
text = f.readlines()

combination = \
    ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', \
    'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', \
    'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', \
    '0', '1', '2', '3', '4', '5', '6', '7', '8', '9']

def getPassWord(hashcode):
    
    for length in range(1, 9):
    
        combi = list(permutations(combination, length))
        
        for i in range(len(combi)):
            pw = ''.join(combi[i])
            enc = hashlib.md5()
            enc.update(pw.encode('utf-8'))
            encText = enc.hexdigest()
            
            if encText == hashcode: return pw
    
    return 'Fail'
    
cnt=0
idx=0
for hashcode in text:
    idx+=1
    # 예상 패스워드, 아직 로직 X
    print(idx, '번째 hashcode 탐색 중...')
    
    hashcode = hashcode.strip()
    password = getPassWord(hashcode)

    if(password!='Fail'):
        cnt+=1
        print(cnt,'/1000000 password has been cracked, hashed: ',hashcode, 'cracked: ', password)

print(cnt,'/1000000 password has been cracked')
f.close()