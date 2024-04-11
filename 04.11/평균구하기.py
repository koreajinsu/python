# 정수를 담고 있는 배열 arr의 평균값을 return하는 함수, solution을 완성해보세요.

# 제한사항
# arr은 길이 1 이상, 100 이하인 배열입니다.
# arr의 원소는 -10,000 이상 10,000 이하인 정수입니다.
'''
def solution(arr):
# def solution(arr):: 이 줄은 solution이라는 함수를 정의합니다. 
# 이 함수는 arr이라는 매개변수를 받습니다. 여기서 arr은 평균값을 구할 정수들이 담긴 배열입니다.
    sum_of_arr = 0
# sum_of_arr = 0: sum_of_arr이라는 변수를 선언하고, 0으로 초기화합니다. 이 변수는 배열 arr의 모든 요소들의 합을 저장할 것입니다.
    for num in arr:
# for num in arr:: arr 배열의 각 요소를 num이라는 변수에 하나씩 대입하여 반복문을 실행합니다.
        sum_of_arr += num
# sum_of_arr += num: 각 반복에서 num 값을 sum_of_arr에 더합니다. 이렇게 하면 sum_of_arr에는 arr 배열의 모든 요소들의 합이 저장됩니다.
    average = sum_of_arr / len(arr)
# average = sum_of_arr / len(arr): arr 배열의 길이로 나눠서 평균값을 계산하고, 그 결과를 average 변수에 저장합니다.
    return average
# return average: 평균값을 반환합니다.
arr = [1, 2, 3, 4, 5]
print(solution(arr))  # 3나온다
# 마지막 부분에서는 함수를 호출하여 예시 입력을 주고, 평균값이 제대로 계산되는지 확인합니다.
'''


# for i in range(len(list_value)):
#     sum=sum+list_value[i]
# for i in range(len(list_value)):
#     sum=sum+i
# print(sum / len(list_value))
# 박진






