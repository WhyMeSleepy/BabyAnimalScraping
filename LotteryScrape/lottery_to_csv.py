from bs4 import BeautifulSoup
import requests
import csv
import re

def main():
    global writer
    global count_id
    count_id = 368
    file = open('filecsv/lottery.csv','w',encoding='utf-8')
    writer = csv.writer(file)
    writer.writerow(['id','DrawDate','FirstPrize','FirstThree DigitsPrize','LastThreeDigitsPrize','LastTwoDigitsPrize'])
    for page in range(1,20):
        lottery_number(page)

def lottery_number(page):
    global file_num
    global count_id
    if page == 1:
        get_html = requests.get('https://news.sanook.com/lotto/archive/').text
    else:
        get_html = requests.get(f'https://news.sanook.com/lotto/archive/page/{page}/').text
    
    soup = BeautifulSoup(get_html,'lxml')
    lotteries = soup.find_all('article',class_='archive--lotto')
    for lottery in lotteries:
        lottery_date = lottery.find('h3',class_='archive--lotto__head-lot').text
        
        contain_num = lottery.find('ul',class_='archive--lotto__result-list')
        list_num = contain_num.find_all('li')

        date = (' '.join(re.split(' |-',lottery_date)[-3:]))
        
        firstPrize = None
        firstThree = None
        lastThree = None
        lastTwo = None
        for i in list_num:
            award = i.find('em',class_='archive--lotto__result-txt').text
            number_award = i.find('strong',class_='archive--lotto__result-number').text
            if 'รางวัลที่ 1' in award:
                firstPrize = (number_award.strip().replace("\n",' '))
            elif 'เลขหน้า 3 ตัว' in award:
                firstThree = (number_award.strip().replace("\n",' '))
            elif 'เลขท้าย 3 ตัว' in award:
                lastThree = (number_award.strip().replace("\n",' '))
            elif 'เลขท้าย 2 ตัว' in award:
                lastTwo = (number_award.strip().replace("\n",' '))

        writer.writerow([count_id,date,firstPrize,firstThree,lastThree,lastTwo])
        count_id -= 1
        print(date)
        print(firstPrize)
        print(firstThree)
        print(lastThree)
        print(lastTwo)
        
        
    


if __name__ == '__main__':
    main()