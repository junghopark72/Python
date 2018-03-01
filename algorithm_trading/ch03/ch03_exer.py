naver_closing_price = []
naver_closing_price2 = {}

def add_closing_price(price):
    naver_closing_price.append(price)

if __name__ == '__main__':
    
    add_closing_price(474500)
    add_closing_price(461500)
    add_closing_price(501000)
    add_closing_price(500500)
    add_closing_price(488500)

    # 1
    print("naver_closing_price =", naver_closing_price)

    # 2
    max_closing_price = max(naver_closing_price)
    print("max_closing_price = %d" % max_closing_price)

    # 3
    min_closing_price = min(naver_closing_price)
    print("min_closing_price = %d" % min_closing_price)
    
    # 4
    print("diff =", max_closing_price - min_closing_price)

    # 6
    naver_closing_price2['09/07'] = naver_closing_price[0]
    naver_closing_price2['09/08'] = naver_closing_price[1]
    naver_closing_price2['09/09'] = naver_closing_price[2]
    naver_closing_price2['09/10'] = naver_closing_price[3]
    naver_closing_price2['09/11'] = naver_closing_price[4]

    print("naver_closing_price2 =", naver_closing_price2)

    # 7
    print("naver_closing_price2[%s] = %d" % ('09/09', naver_closing_price2['09/09']))
