true = True
false = False
def solution(absolutes, signs):
    minus = []
    plus = []
    for a,s in zip(absolutes, signs):
        if s == False :
            minus.append(a)
        else :
            plus.append(a)
    return sum(plus) - sum(minus)
  
## best answer 
'''
def solution(absolutes, signs):
    return sum(absolutes if sign else -absolutes for absolutes, sign in zip(absolutes, signs))
''
