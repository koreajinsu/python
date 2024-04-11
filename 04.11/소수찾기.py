'''

1부터 입력받은 숫자 n 사이에 있는 소수의 개수를 반환하는 함수, solution을 만들어 보세요.

소수는 1과 자기 자신으로만 나누어지는 수를 의미합니다.
(1은 소수가 아닙니다.)

제한 조건
n은 2이상 1000000이하의 자연수입니다.
'''

def solution(n):
    sosoo= [True] * (n+1)
    sosoo[0] = sosoo[1] = False

    for i in range(2, int(n**0.5)+1):
        if sosoo[i]:
            for j in range(i*i, n+1, i):
                sosoo[j] = False

    return sum(sosoo)

# 예시 입력
print(solution(10))  # 출력: 4 (2, 3, 5, 7은 소수)