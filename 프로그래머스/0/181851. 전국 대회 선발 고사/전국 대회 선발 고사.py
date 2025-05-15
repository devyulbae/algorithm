def solution(rank, attendance):
    for i in range(len(rank)):
        rank[i] = rank[i] + (attendance[i]==False)*100
    sorted_rank = sorted(rank)
    a = rank.index(sorted_rank[0])
    b = rank.index(sorted_rank[1])
    c = rank.index(sorted_rank[2])
        
    return 10000*a + 100*b + c