#202311388 김민상
#Chapter 1
#문제 15_문자열 찾기 알고리즘 설계

def FindText(text, a) :
    temp = False
    for i in text :
        if a in text :
            print(f"\"{a}\"가 text 안에 있음")
            temp = True
            break
    
    if temp == False :
        print(f"\"{a}\"가 text에 없음")

text = input("문자열 입력 : ")
word = input("찾을 문자열 입력 : ")
FindText(text, word)