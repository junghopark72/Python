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


def get_page_count(page_no):

    # base_dir = os.path.dirname(os.path.abspath(__file__))

    url_frag1 = 'http://stock.thinkpool.com/bbs/itemanal/read/stock_bbs.do?sn=10579165&code=068270&pageNo=1&iMax=00105791659999&memoPageNo='
    url_frag2 = '&gmYn=&schIdx=1#list_comment'
    url = url_frag1 + str(page_no) + url_frag2
    # print(url)
    req = requests.get(url)
    # print('request ok?', req.ok)
    if req.ok is not True:
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
            total.append(str(page_no) + ',' + str(m_index) + ',' + member.text)

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
                total.append(str(page_no) + ',' + str(m_index) + ',' + member.text)

    # for i in range (0, len(total)):
    #     print(total[i])

    # print('m_index =', m_index)  # the number of members in each page
    # print('g_index =', g_index)

    count = 0
    v_index = 0  # the number of voters in each page

    # print('----- voters -----')
    for voter in voters:
        numbers = re.findall('\d+', voter.text)
        total[g_index + v_index] += ','
        if len(numbers) == 0:
            count += 1
            total[g_index + v_index] += voter.text.strip() + ',1'
        elif len(numbers) == 1:
            number = numbers.pop(0)
            count += int(number)
            total[g_index + v_index] += voter.text.strip() + ',' + number
        else:
            count += 1
            total[g_index + v_index] += '(wrong)' + ',1'
            # print(total[g_index + v_index])
        v_index += 1
    # print('count = ', count)

    # print('----- voters2 -----')
    for voter in voters2:
        numbers = re.findall('\d+', voter.text)
        total[g_index + v_index] += ','
        if len(numbers) == 0:
            count += 1
            total[g_index + v_index] += voter.text.strip() + ',1'
        elif len(numbers) == 1:
            number = numbers.pop(0)
            count += int(number)
            total[g_index + v_index] += voter.text.strip() + ',' + number
        else:
            count += 1
            total[g_index + v_index] += '(wrong)' + ',1'
        v_index += 1

    # page summary
    # print('# %-2d페이지: 댓글수(%2d), 참여인원(%2d)' % (page_no, m_index, count))
    if count is not 0:
        print('# %-2d페이지: %2d' % (page_no, count))

    if m_index is not v_index:
        print('Oops!!!')

    g_index += m_index
    # print('g_index =', g_index)

    return count


if __name__ == '__main__':
    
    total_sum = 0
    for i in range(1, 100):
        total_sum += get_page_count(i)

    print('댓글인원 :', len(total))
    print('참여인원 :', total_sum)

    # for i in range (0, len(total)):
    #     print(total[i])
