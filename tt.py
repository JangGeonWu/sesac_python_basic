def solution(n):
    n = n - 1
    answer = ''
    while True:
        
        num1 = n % 3
        num2 = n // 3
        if num1 == 2:
            answer = '4' + answer
        else:
            answer = str(num1 + 1) + answer
        
        if num2 > 0:
            n = num2 - 1
        else:
            break
    
    return answer

for i in range(1, 20):
    print(solution(i))