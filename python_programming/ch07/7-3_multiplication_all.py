# 1.3 구구단 전체 출력하기
print('\n1.3 구구단 전체 출력하기')

for m in range(1, 10):
    print('='*10) # 10번 반
    for n in range(1, 10):
        print(m, 'x', n, '=', m*n)
