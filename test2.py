def reverse_string(s):
    reversed_string = ''  # 결과를 담을 빈 문자열
    for char in s:        # 입력된 문자열의 각 문자를 하나씩 가져와서
        reversed_string = char + reversed_string  # 앞에 추가해 줍니다
    return reversed_string  # 최종적으로 뒤집힌 문자열을 반환
