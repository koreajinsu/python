def solution(num, n):
    
    #num 과 n 값 지정
    #num이 n의 배수이면 1 아니면 0
    #num % n == 0 일 때 배수 1
    #아니면 0
    
    num, n =int, input('숫자를 두 개 입력해 주세요: ').split(' ')
    
    if(num % n == 0):
        print("1")
    else:
        print('0')        
    return 0
W
def solution(num, n):
    if num % n == 0:
        return 1
    else:
        return 0

