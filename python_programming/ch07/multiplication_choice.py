# 1.2 원하는 구구단 출력
print('\n1.2 원하는 구구단 출력')

m = int(input('구구단 몇 단을 출력할까요? 숫자를 입력하세요: '))

while m < 1 or m > 9:
    m = int(input('구구단은 1단부터 9단까지 출력 가능합니다. 맞는 숫자를 다시 입력하세요: '))

print(m, "단을 출력합니다.")
for n in range(1, 10):
    print('%d x %d = %d' % (m, n, m*n))
