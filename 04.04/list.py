#리스트 튜플 

def main():
    print("list")
    a='월요일'
    b='화요일'
    c='수요일'
    
    print(a, b, c)
    var= ['월요일', '화요일', '수요일', 1, 2, 3]
    var.append('목요일')
    var.append('금요일')
    var.remove('화요일')
    
    
    print(var)
    
    if '일요일' in var:
        print('월요일')
        print('월요일')
    
    
    else:
        print('찾는 요일이 없습니다.')
        
if __name__ == '__main__':
    main()


