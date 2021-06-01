import re
def solution(new_id):
  #1단계 
  n = new_id.lower()
  #2단계
  n = re.sub(r"[^a-z0-9-_.]","",n)
  #3단계
  n = re.sub(r"[.]+",".",n)
  #4단계
  n = re.sub(r"^[.]","",n)
  if len(n)>=1 and n[-1]== "." : n = re.sub(r".$","",n)
  #5단계
  if n == "": n = "a"
  #6단계
  if len(n) >= 16:
    n = n[0:15]
    if n[-1]==".": n = re.sub(r".$","",n)
  if len(n) <= 2:
    while len(n) < 3: n += n[-1]
  return n

### best answer ###
import re

def solution(new_id):
    st = new_id
    st = st.lower()
    st = re.sub('[^a-z0-9\-_.]', '', st)
    st = re.sub('\.+', '.', st)
    st = re.sub('^[.]|[.]$', '', st)  ## 이런식으로 |를 사용해서 and 표현 가능
    st = 'a' if len(st) == 0 else st[:15] ## 헐 if문을 한줄로 표현할 수도 있는 거구나 comprehension처럼
    st = re.sub('^[.]|[.]$', '', st)  ## 역시 concat
    st = st if len(st) > 2 else st + "".join([st[-1] for i in range(3-len(st))])
    return st
