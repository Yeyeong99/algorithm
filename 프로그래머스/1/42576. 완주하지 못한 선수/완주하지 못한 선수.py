def solution(participant, completion):
    completion_dict = {x: True for x in completion}
    participant_dict = {}
    for x in participant:
        participant_dict.setdefault(x, 0)
        participant_dict[x] += 1
        
    for y in completion:
        participant_dict[y] -= 1
    
    for k in participant_dict:
        if participant_dict[k]:
            return k
            