# 3. 내가 읽은 책 목록 만들기

# 3.3 소스 코드 단순화하기

books = list()

books.append({'제목': '개발자의 코드', '출판년도': '2013.02.28', '출판사': 'A', '쪽수': 200, '추천유무': False})
books.append({'제목': '클린 코드', '출판년도': '2010.03.04', '출판사': 'B', '쪽수': 584, '추천유무': True})
books.append({'제목': '빅데이터 마케팅', '출판년도': '2014.07.02', '출판사': 'A', '쪽수': 296, '추천유무': True})
books.append({'제목': '구글드', '출판년도': '2010.02.10', '출판사': 'B', '쪽수': 526, '추천유무': False})
books.append({'제목': '강의력', '출판년도': '2013.12.12', '출판사': 'A', '쪽수': 248, '추천유무': True})

#many_page = list()
#recommends = list()
all_pages = int()
#pub_company = set()

many_page = [book['제목'] for book in books if book['쪽수'] > 250]
recommends = [book['제목'] for book in books if book['추천유무'] == True]
pub_company = {book['출판사'] for book in books}

for book in books:
    #if book['쪽수'] > 250:
    #    many_page.append(book['제목'])
    #if book['추천유무'] == True:
    #   recommends.append(book['제목'])
    all_pages += book['쪽수']
    #pub_company.add(book['출판사'])

print('쪽수가 250쪽이 넘는 책 리스트:', many_page)
print('내가 추천하는 책 리스트:', recommends)
print('내가 읽은 책 전체 쪽수:', all_pages)
print('내가 읽은 책의 출판사 목록:', pub_company)
