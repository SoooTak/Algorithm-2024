#202311388 김민상
#Chapter 1
#문제 22_스택이용 문자열 역순출력

list = []
list = input("문자열 입력 : ")
temp = len(list) * -1 - 1
print(f"입력한 문자열 : {list}")
print("역순 출력 : ", end="")
for i in range(-1, temp, -1) :
    print(f"{list[i]}", end="")
