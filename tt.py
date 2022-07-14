from math import ceil
from collections import Counter
def solution(progresses, speeds):
    success_list = []
    success_list.append(ceil((100 - progresses[0]) / speeds[0]))
    
    for i in range(1, len(progresses)):
        bp = ceil((100 - progresses[i]) / speeds[i])
        av_bp = success_list[-1]
        if bp <= av_bp:
            success_list.append(av_bp)
        else:
            success_list.append(bp)

    cnt = Counter(success_list)

    return list(dict(cnt).values())

print(solution([93, 30, 55], [1, 30, 5]))    