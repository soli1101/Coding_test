def solution(left, right):
    plus, minus = [], []
    for i in range(left, right+1):
        if len([j for j in range(1,i+1) if i%j==0])%2 == 0 :
              plus.append(i)
        else :
              minus.append(i)

    answer = sum(plus) - sum(minus)
    return answer

## 다른 풀이 : 루트 씌운 값이 정수로 떨어지면, 약수의 개수가 짝수!!

def solution(left, right):
    answer = 0
    for i in range(left,right+1):
        if int(i**0.5)==i**0.5:
            answer -= i
        else:
            answer += i
    return answer
