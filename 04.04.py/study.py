def main():
    print('aa')

    a = '1'
    b = '2'
    print(a + b)

    # 입력에서 충분한 값을 받도록 수정
    while True:
        try:
            num1, num2 = map(int, input('숫자를 두 개 입력해 주세요: ').split(' '))
            break  # 유효한 입력이 제공되면 반복문을 종료
        except ValueError:
            print("숫자를 정확히 입력해 주세요.")

    print(num1 + num2)

    # < , <=, >, >=, ==, !=
    # 1<x<10
    x = int(input('x: '))
    if 1 < x < 10:
        print(x)
    else:
        print(x)

if __name__ == '__main__':
    main()
