def solution(people, limit):
    people.sort()
    left = 0 # 가장 가벼운 사람
    right = len(people) - 1 # 가장 무거운 사람
    boats = 0
    
    while left <= right:
        if people[left] + people[right] <= limit:
            left += 1
        right -= 1
        boats += 1

    return boats
    