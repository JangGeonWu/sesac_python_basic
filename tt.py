from math import ceil
def solution(w,h):
    ratio = w / h if w > h else h / w
    
    num_square = ceil(ratio)
    
    loss = h * num_square if w > h else w * num_square
    
    
    return (w*h) - loss

print(solution(3,3))    