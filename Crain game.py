def solution(board, moves):
    
    # board의 열 한줄 씩 list로 만들어 f list에 넣어주기
    f=[]
    for j in range(len(board)):
        f.append([i[j] for i in reversed(board) if i[j]!=0])

    cnt = 0        # 사라진 개수를 cnt
    stack = []     # 쌓이는 deck
     
    for move in moves: #0~7
        if f[move-1] != []:                  # f가 전부 비어있지 않을 때만 
            stack.append(f[move-1][-1])      # stack에 append 시키기 
            f[move-1].pop()                  # 옮긴 번호는 윗줄에서 지우기

        while len(stack) > 1:
            if stack[-1] == stack[-2]:
                stack.pop()
                stack.pop()
                cnt += 2
            else: break
            
    return print(stack, cnt)

board = [[0, 0, 0, 0, 0], [0, 0, 1, 0, 3], [0, 2, 5, 0, 1], [4, 2, 4, 4, 2], [3, 5, 1, 3, 1]]
moves = [1, 5, 3, 5, 1, 2, 5, 1, 4, 3]

solution(board,moves)