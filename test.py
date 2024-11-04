def to_jaden_case(string):
    return string.title()

# 사용자 입력 받기
user_input = input("문장을 입력하시오: ")
jaden_cased = to_jaden_case(user_input)
print("Jaden-Cased:", jaden_cased)
