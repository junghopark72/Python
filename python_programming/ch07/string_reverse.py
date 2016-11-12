# 2.2 문자열 순서 바꾸기

s = input('영어 문장을 입력하세요.\n')

new_s = str()

for x in range(len(s)-1, -1, -1):
    new_s += s[x]

print(new_s)

print(s[::-1])

# range([start=0], end, [step=1])
