# 카카오 - 숫자 문자열과 영단어
def solution(s):
    en_num = ['zero', 'one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight', 'nine']
    
    for en in en_num: s = s.replace(en, str(en_num.index(en)))
    return int(s)

solution("one4seveneight")