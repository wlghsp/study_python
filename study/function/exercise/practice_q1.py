
def is_odd(number):
    if number % 2 == 1:
        return True
    else:
        return False
a = input("숫자를 입력하세요: ")

if is_odd(int(a)):
    print("홀수")
else:
    print("짝수")