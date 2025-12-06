def solution(sizes):
    sizes_sort = list(map(lambda x: [max(x), min(x)], sizes))
    height = []
    width =  []
    for i, j in sizes_sort:
        height.append(i)
        width.append(j)
    
    answer = max(height) * max(width)
    return answer
