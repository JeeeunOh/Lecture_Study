# 4자리 발굴 성공

import hashlib
from string import*  
from itertools import combinations

# 1MillionPassword_hashed 경로를 통해 텍스트 파일 가져와서 읽기 w/https://wikidocs.net/81809
file_path = '/Users/jieun/Documents/GitHub/Univ-Lecture/네트워크보안/패스워드크랙킹/1MillionPassword_hashed.txt'
f = open(file_path)
text = f.readlines()
idx=0

# combination = \
#     ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', \
#     'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', \
#     'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', \
#     '0', '1', '2', '3', '4', '5', '6', '7', '8', '9']

combination = ['a', 'b', 'c', 'o', 'p', 's']

def getPassWord(hashcode):
    
    combi = list(combinations(combination, 4))
    
    for i in range(len(combi)):
        pw = ''.join(combi[i])
        enc = hashlib.md5()
        enc.update(pw.encode('utf-8'))
        encText = enc.hexdigest()
        
        if encText == hashcode: return pw
    
    return 'Fail'
    

for hashcode in text:
    # 예상 패스워드, 아직 로직 X
    hashcode = hashcode.strip()
    password = getPassWord(hashcode)
    if(password!='Fail'):
        idx+=1
        print(idx,'/1000000 password has been cracked, hashed: ',hashcode, 'cracked: ', password)

f.close()