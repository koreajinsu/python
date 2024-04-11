
# 문제

# 자연수 n이 매개변수로 주어집니다.
# n을 x로 나눈 나머지가 1이 되도록 하는 가장 작은 자연수 x를 return 하도록
# solution 함수를 완성해주세요. 답이 항상 존재함은 증명될 수 있습니다.


# # 순서도
# 1. 함수를 정의합니다. 함수는 매개변수 n을 받습니다.
# 2. x를 찾기 위해 반복문을 사용합니다. 
# 3.초기값으로 x를 2로 설정합니다. (1로 나눈 나머지는 항상 1이므로 1은 고려하지 않아도 됩니다.)
# 4.반복문을 사용하여 x를 증가시키면서, n을 x로 나눈 나머지가 1이 되는지 확인합니다.
# 5.나머지가 1이 되면 해당 x를 반환하고 반복문을 종료합니다.
# 6. 반복문을 종료하지 못했다면, x를 증가시키며 계속해서 확인합니다.

# # def solution(n):

#     x = 2  # x는 1을 제외한 가장 작은 자연수이므로 초기값을 2로 설정합니다.
#     while True:
#         if n % x == 1:  # n을 x로 나눈 나머지가 1인지 확인합니다.
#             return x   # 만약 나머지가 1이면 x를 반환합니다.
#         x += 1  # x를 1씩 증가시킵니다.

'''
교수님이 풀어주신 부분
n=10
x=1
num=[]
while x < n:
    # print(n%x)
    if ((n%x) == 1):
        print(x)
        num.append(x)
    x+=1
print(num)
print(num[0])
'''