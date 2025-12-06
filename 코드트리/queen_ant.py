def ants_visit_comb(ants_num, num, ants_visit):
    global min_time

    if len(ants_visit) == ants_num:
        # 시간 계산
        max_time = -999999999999999999
        for i in range(len(ants_visit) - 1): # 개미 수 가 1이면 for문 안돌고 값 업데이트 안됨
            next_idx = ants_visit[i + 1] - 1
            ant_time = homes[next_idx] - homes[i]
            max_time = max(ant_time, max_time)

        min_time = min(max_time, min_time)
        return

    if homes[num] > 0:
        ants_visit.append(num)
        num += 1
        ants_visit_comb(ants_num, num, ants_visit)
        ants_visit.pop()
        num -= 1

n = int(input())

for i in range(n):
    inputs = list(map(int, input().split()))
    
    order = inputs[0]
    # 마을 건설
    if order == 100:
        number_of_home = inputs[1]
        home_list = inputs[2:]
        last_home = inputs[-1]

        homes = []
        for j in home_list:
            homes.append(j)

    
    # 개미집 건설 (좌표)
    if order == 200:
        x = inputs[1]
        homes.append(x)

    # 개미집 철거(n 번째)
    if order == 300:
        remove_x = inputs[1]
        homes[remove_x - 1] = 0

    # 정찰  
    if order == 400:
        ants_num = inputs[1]
        min_time = float("inf")
        ants_visit = []
        num = 0
        ants_visit_comb(ants_num, num, ants_visit)
        print(min_time)
