# 어떤 정수들이 있습니다. 
# 이 정수들의 절댓값을 차례대로 담은 정수 배열 absolutes와 이 정수들의 부호를 차례대로 담은 불리언 배열 signs가 매개변수로 주어집니다. 
# 실제 정수들의 합을 구하여 return 하도록 solution 함수를 완성해주세요.

# 제한사항
# absolutes의 길이는 1 이상 1,000 이하입니다.
# absolutes의 모든 수는 각각 1 이상 1,000 이하입니다.
# signs의 길이는 absolutes의 길이와 같습니다.
# signs[i] 가 참이면 absolutes[i] 의 실제 정수가 양수임을, 그렇지 않으면 음수임을 의미합니다.


# 순서도

# 1.함수를 정의한다. 함수는 매개변수 absolutes와 signs를 받는다.
# 2.합을 저장할 변수 total을 초기화한다.
# 3.absolutes와 signs의 각 값들을 보면서, 해당 값들의 절댓값을 구한다.
# 4 만약 signs의 요소가 True라면, 절댓값을 그대로 total에 더합니다.
# 5만약 signs의 요소가 False라면, 절댓값을 음수로 바꾼 후 total에 더합니다.
# 6 모든 요소에 대해 반복한 후, total을 반환합니다.


# 교수님이 작성한 순서도
# 1.우선순위. signs
# 2.signs 값 읽기 -반복문 for i in signs
# 3.signs 극성 값을 판별 참인경우 + 거짓인 경우 -
#    참 또는 거짓 일 때 absolutes 변수를 사용해서 연산을 한다. -조건문 사용한다
# 4.signs 개수 끝날 때 까지 연산을 해서 전체 합을 구합니다.
# sum=sum : +- absolutes

# def solution(absolutes, signs):
    
# false=False
# true=True

# absolutes=[4,7,12]
# signs=[true,false,true]

# for i in range(len(signs)):
#     #print(i)
        
#     if(signs[i] == True):
#         #print("True")
#         sum =sum + absolutes[i]
#     else:
#         #print("False")        
#         sum= sum - absolutes[i]

# return sum
# # 박진

def solution(absolutes, signs):
    total = 0  # 합계를 저장할 변수를 초기화합니다.

    for i in range(len(signs)):
        if signs[i]:  # signs의 요소가 True이면
            total += absolutes[i]  # 절댓값을 더합니다.
        else:
            total -= absolutes[i]  # signs의 요소가 False이면 절댓값을 뺍니다.

    return total  # 합계를 반환합니다.

# 함수를 호출하여 결과를 출력합니다.
print(solution([4, 7, 12], [True, False, True]))