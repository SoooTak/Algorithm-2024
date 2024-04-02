#202311388 김민상
#Chapter 2
#반복 알고리즘 - 2진수 비트 수 계산
def binary_digits(n) :
    count = 1
    while n > 1 :
        count += 1
        n //= 2
    return count

num = int(input("숫자 입력 : "))
print(f"{num}를 2진수로 나타내는데 필요한 비트 수 = {binary_digits(num)}")