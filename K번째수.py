def solution(array, commands):
  answer = []
  for c in commands:
    sliced = array[c[0]-1:c[1]]
    answer.append(sliced[c[2]-1])
  return answer
  
  
def solution(array, commands):
  return [ sorted(array[c[0]-1:c[1]])[c[2]-1] for c in commands ] 
