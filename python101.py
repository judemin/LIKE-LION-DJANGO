# 정수, 실수 자료형
num = 1

# 정수, 실수 자료형에서의 기본 연산
num1 = 1
num2 = 3
print(num1 + num2)  # 4
print(num1 - num2)  # -2
print(num1 * num2)  # 3

# 나눗셈 연산
num1 = 5
num2 = 2
print(num1 / num2)  # 2.5
print(num1 // num2)  # 2
print(num1 % num2)  # 1

# 특수 연산자
# 거듭제곱 연산자 지원
num1 = 3
num2 = 2
print(num1 * num1)  # 9
print(num1**2)  # 9
print(num1**num2)  # 9

#############################

text1 = "1"
text2 = "1"
print(type(text1))  # <class 'str'>
print(type(text2))  # <class 'str'>

# 문자열 관련 함수
text1 = "Hello World! I'm likelion"
print(text1[:5])  # Hello
print(text1[-4:])  # lion
print("World" in text1)  # True
print(text1.find("W"))  # 6 -> 문자열에서 특정 문자의 인덱스 값 반환
print(",".join(text1))  # H,e,l,l,o, ,W,o,r,l,d,!, ,I,',m, ,l,i
print(text1.split())  # ['Hello', 'World!', "I'm", 'likelion']

# split 함수
text1 = "Hello World! I'm likelion"
print(text1.split())  # ['Hello', 'World!', "I'm", 'likelion']
text_split = text1.split()
print(text_split[0])  # Hello


#############################

num = [1, 2, 3, 4, 5]
print(num[0])  # 1
print(num * 2)  # [1, 2, 3, 4, 5, 1, 2, 3, 4, 5]

# 리스트의 slicing
num = [1, 2, 3, 4, 5]
print(num[0:3])  # [1, 2, 3]

# 리스트 연산
num = [1, 2, 3, 4, 5]
num2 = [3, 4]
print(num + num2)  # [1, 2, 3, 4, 5, 3, 4]

# 리스트 길이 구하기
num = [1, 2, 3, 4, 5]
print(len(num))  # 5

# 리스트 요소 추가
num = [1, 2, 3, 4, 5]
num.append(100)
print(num)  # [1, 2, 3, 4, 5, 100]

# 리스트 요소 삭제
# remove - 리스트에서 특정 값을 찾아서 삭제
list5 = [1, 2, 3, 4]
list5.remove(2)  # [1, 3, 4]
# pop - 리스트에서 특정 위치에 있는 데이터를 삭제(맨 앞이 0번!)
list6 = ["a", "b", "c", "d"]
list6.pop(1)  # ['a', 'c', 'd']
# count
list6 = ["a", "b", "a", "b"]
list6.count("a")  # 2
print(list6.count("a"))

#############################

dic = {"사과": 100, "귤": 500, "오렌지": 200}
print(dic["사과"])  # 100

# 딕셔너리의 key:value
dic = {"감기": "약", "배고픔": "밥"}
dic["감기"]  # 약

# 딕셔너리에 요소 추가
dic = {"사과": 100, "귤": 500, "오렌지": 200}
dic["배"] = 700
print(dic["배"])  # 700

# 딕셔너리의 key 요소만 호출
dic = {"사과": 100, "귤": 500, "오렌지": 200}
print(dic.keys())  # dict_keys(['사과', '귤', '오렌지'])
print(dic.values())  # dict_values([100, 500, 200])


#############################

# 조건문 : if, elif, else
a = input("숫자를 입력하세요")
if a > 0:  # a > 0 이 참이 될 때
    print("양수입니다.")
elif a < 0:  # a > 0 이 거짓이고, a < 0일 때
    print("음수입니다.")
else:  # a > 0 도 거짓이고, a < 0 도 거짓일 때
    print("0 입니다.")

# 반복문
for i in range(0, 10, 1):  # in range -> [0, 1, 2 ,3, ..., 9]인 리
    if i % 2 == 0:
        print(i, "는 짝수입니다.")
    else:
        print(i, "는 홀수입니다.")

late = ["혜정", "연진", "재준", "사라"]
print("지각한 사람:")
for name in late:  # late리스트 안에 있는 모든 요소들에 대해 반복
    print(name)

for i in range(1, 4):  # i 는 몇 번째 세트인지를 나타냄
    print("회원님~!", i, "세트 시작하겠습니다")
    for j in range(1, 11):  # j는 해당 세트에서 동작을 몇 번 반복했는지를
        print(j)


def diamond_step():
    print("앞으로 한 칸 전진")
    print("시계방향으로 90도 회전")
    print("앞으로 한 칸 전진")
    print("시계방향으로 270도 회전")


diamond_step()


class Dog:
    def __init__(self, name):
        self.name = name

    # 클래스가 가지는 모든 함수는 첫 번째 매개변수로 self를 무조건 포함해
    def respond_to_command(self, command):  # 이름을 부르면 짖는다!
        if command == self.name:
            self.speak()

    def speak(self):
        print("Woof Woof")


# 이름이 "Max"인 개를 만들기
fido = Dog("Max")

# call respond_to_command 함수를 호출해보자
fido.respond_to_command("Kitty")  # do nothing
fido.respond_to_command("Max")  # print Woof Woof
