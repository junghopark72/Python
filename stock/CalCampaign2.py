# CalCampaign.py
# Written by Jungho.Park

import requests
from bs4 import BeautifulSoup
import json
import os
import re

total = []
g_index = 0  # global index for total
max_page = 70


def get_page_count(phase, page_no):

    # base_dir = os.path.dirname(os.path.abspath(__file__))

    # url_frag1 = ''
    # url_frag2 = ''

    if phase == 1:
        url_frag1 = 'http://stock.thinkpool.com/bbs/itemanal/read/stock_bbs.do?sn=10580693&code=068270&pageNo=1&iMax=00105807549999&memoPageNo='
        url_frag2 = '&gmYn=&schIdx=1#list_comment'
    elif phase == 2:
        url_frag1 = 'http://stock.thinkpool.com/bbs/itemanal/read/stock_bbs.do?sn=10580938&code=068270&pageNo=1&iMax=00105809549999&memoPageNo='
        url_frag2 = '&gmYn=&schIdx=1#list_comment'

    url = url_frag1 + str(page_no) + url_frag2
    # print(url)
    req = requests.get(url)
    # print('request ok?', req.ok)
    # print('request status?', req.status_code)
    if req.ok is not True:
        print('page', page_no, "doesn't exist yet !!!")
        return 0

    html = req.text
    soup = BeautifulSoup(html, 'html.parser')
    members = soup.select('#list_comment > ul > li > form > div > a')
    voters = soup.select('#list_comment > ul > li > form > p > span')
    members2 = soup.select('#list_comment > ul > li > form > div > div > a')
    voters2 = soup.select('#list_comment > ul > li > form > div > p > span')

    global g_index

    # print('----- member -----')
    m_index = 0  # the number of members in each page
    for member in members:
        if len(member.text) != 0:
            # print('%d,%s' % (index, member.text))
            m_index += 1
            total.append(str(phase) + ',' + str(page_no) + ',' + str(m_index) + ',' + member.text)

    # print('----- member2 -----')
    for member in members2:
        # print(member.get('href'), member.get('class'))
        attrs = member.get('class')
        if isinstance(attrs, type(None)):
            continue
        if len(attrs) == 1 and attrs[0] == 'name':
            if len(member.text):
                # print('%d,%s' % (index, member.text))
                m_index += 1
                total.append(str(phase) + ',' + str(page_no) + ',' + str(m_index) + ',' + member.text)

    # for i in range (0, len(total)):
    #     print(total[i])

    # print('m_index =', m_index)  # the number of members in each page
    # print('g_index =', g_index)

    count = 0
    v_index = 0  # the number of voters in each page
    is_special = False

    # print('----- voters -----')
    for voter in voters:
        # numbers = re.findall('\d+', voter.text)
        num = voter.text.count('척')
        total[g_index + v_index] += ','
        if num is 0:
            count += 1
            total[g_index + v_index] += voter.text.strip() + ',1'
        elif num is 1:
            numbers = re.findall('\d+', voter.text)
            if len(numbers) > 0:
                number = numbers.pop(0)
                num = int(number)
                # print(voter.text.strip())
                is_special = True
            count += num
            total[g_index + v_index] += voter.text.strip() + ',' + str(num)
            if is_special:
                # print(total[g_index + v_index])
                is_special = False
        else:
            count += num
            total[g_index + v_index] += voter.text.strip() + ',' + str(num)
        v_index += 1
    # print('count = ', count)

    # print('----- voters2 -----')
    for voter in voters2:
        num = voter.text.count('척')
        total[g_index + v_index] += ','
        if num is 0:
            count += 1
            total[g_index + v_index] += voter.text.strip() + ',1'
        elif num is 1:
            numbers = re.findall('\d+', voter.text)
            if len(numbers) > 0:
                number = numbers.pop(0)
                num = int(number)
                # print(voter.text.strip())
                is_special = True
            count += num
            total[g_index + v_index] += voter.text.strip() + ',' + str(num)
            if is_special:
                # print(total[g_index + v_index])
                is_special = False
        else:
            count += num
            total[g_index + v_index] += voter.text.strip() + ',' + str(num)
        v_index += 1

    # page summary
    # print('# %-2d페이지: 댓글수(%2d), 참여인원(%2d)' % (page_no, m_index, count))
    if count is not 0:
        print('%-2d페이지: %2d' % (page_no, count))

    if m_index is not v_index:
        print('Oops!!!')

    g_index += m_index
    # print('g_index =', g_index)

    return count


if __name__ == '__main__':
    
    total_sum = 0
    print('------------------------------')
    print('## 페이지 1 : 글번호 10580693')
    for i in range(1, 50):
        total_sum += get_page_count(1, i)

    print('------------------------------')
    print('## 페이지 2 : 글번호 10580938')
    for i in range(1, 10):
        total_sum += get_page_count(2, i)

    print('------------------------------')
    print('댓글인원 :', len(total))
    print('참여인원 :', total_sum)
    print('------------------------------')

    # for i in range(0, len(total)):
    #     print(total[i])
