def solution(a, b):
    answer=''
    last_date = [0,31,29,31,30,31,30,31,31,30,31,30,31]
    day = ['THU','FRI','SAT','SUN','MON','TUE','WED','THU','FRI','SAT','SUN','MON','TUE','WED','THU','FRI','SAT','SUN','MON','TUE','WED','THUR'] 
    slicing_idx_list=[0, 0]

    for i in range(1,13):
        slicing_idx_list.append(last_date[i]%7)
    
    for n, d in zip(range(7),day[slicing_idx_list[a]:slicing_idx_list[a]+7]):
        if b%7==n:
            answer = d

    return print(answer)

solution(5,24)
