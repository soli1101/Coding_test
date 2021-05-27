def solution(lottos, win_nums):
    answer = []
    # 2. 매칭되는 번호의 개수를 센다
    n_match = 0
    for i in lottos:
      if i in win_nums:
        n_match += 1
    # 3. 매칭되는 번호의 개수 만큼 순위를 answer에 append 한다(최저 순위)    
    num_to_rank = {6:1, 5:2, 4:3, 3:4, 2:5, 1:6, 0:6}
    answer.append(num_to_rank[n_match])
    # 4. 0의 갯수와 매칭되는 번호의 갯수를 더해서 answer에 append 한다(최고 순위)
    answer.append(num_to_rank[min(n_match+lottos.count(0),6)])
    return sorted(answer)
  
  ## better solution : dict 필요없이 rank 자체의 인덱스를 활용해 인덱스에 해당하는 number를 불러오면 이중으로 계한할 필요 x ##
  def solution(lottos, win_nums):

    rank=[6,6,5,4,3,2,1]

    cnt_0 = lottos.count(0)
    ans = 0
    for x in win_nums:
        if x in lottos:
            ans += 1
    return rank[cnt_0 + ans],rank[ans]
  
  ## best solution ##
  def solution(lottos, win_nums):
    rank = {
        0: 6,
        1: 6,
        2: 5,
        3: 4,
        4: 3,
        5: 2,
        6: 1
    }
    return [rank[len(set(lottos) & set(win_nums)) + lottos.count(0)], rank[len(set(lottos) & set(win_nums))]]
