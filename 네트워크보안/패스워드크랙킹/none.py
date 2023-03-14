import hashlib

# 1MillionPassword_hashed 경로를 통해 텍스트 파일 가져와서 읽기 w/https://wikidocs.net/81809
file_path = '/content/sample_data/1MillionPassword_hashed.txt'
f = open(file_path)
text = f.readlines()
idx=0

combination = \
    ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', \
    'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', \
    'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', \
    '0', '1', '2', '3', '4', '5', '6', '7', '8', '9']

def getPassWord(curPw, hashcode):
    
    for i in range(len(combination)):
        nextPw = curPw + combination[i]
        
        enc = hashlib.md5()
        enc.update(nextPw.encode('utf-8'))
        encText = enc.hexdigest()
        
        if len(nextPw) == 5: return '예상 실패 패스워드: '+ nextPw +', 패스워드 인코딩: ' + encText 
        
        if encText == hashcode: return nextPw
        else: getPassWord(nextPw, hashcode)
        
    
    

for hashcode in text:
    # 예상 패스워드, 아직 로직 X
    hashcode = hashcode.strip()
    password = getPassWord('', hashcode)
    
    # md5에 값 넣어보기
    # enc = hashlib.md5()
    # enc.update(password.encode('utf-8'))
    # encText = enc.hexdigest()

    idx+=1
    print(idx,'/1000000 password has been cracked, hashed: ',hashcode, 'cracked: ', password)

f.close()