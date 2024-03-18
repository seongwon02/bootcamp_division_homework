"""
    main 함수 안의 내용만 수정해주세요.
    수정할 경우, 자동 채점 프로그램이 제대로 동작하지 않을 가능성이 있습니다.
"""

def main():
    # 이곳에 코드를 작성해주세요!
    num = int(input())

    sum = 0
    facto = 1
    for i in range(1, num+1):
        sum += i
        facto *= i
    
    print(sum)
    print(facto)

    return


if __name__ == '__main__':
    main()
