N = int(input())
tops = list(map(int, input().split()))

stack = [[tops[-1], N - 1]]  # 마지막 탑 넣어두고 시작 
answer = ["0"] * N
max_top = tops[-1]
for idx in range(N - 2, -1, -1):  # 마지막에서 두 번째 탑부터
    current_top, current_idx = stack[-1]
    
    if max_top < tops[idx]:
        max_top = tops[idx]

    if tops[idx] == max_top:
        while stack:
            current_idx = stack.pop()[-1]
            answer[current_idx] = str(idx + 1)
            
        stack = [[tops[idx], idx]]

    elif tops[idx] > stack[-1][0]:
        while tops[idx] > stack[-1][0]:
            current_idx = stack.pop()[-1]
            answer[current_idx] = str(idx + 1)
      
        stack.append([tops[idx], idx])

    else:
        stack.append([tops[idx], idx])  # 맨 앞에 넣는 식(들어갈 값 + 기존 리스트)이면 복사로 인해 시간초과 남
print(" ".join(answer))