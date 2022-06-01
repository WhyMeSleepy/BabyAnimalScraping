from bs4 import BeautifulSoup
import requests



def lottery_number(page):
    global file_num
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

        with open('lotteryNumber/{}.txt'.format(file_num),'w',encoding='utf-8') as f:

            f.write('งวดที่ '+' '.join(lottery_date.split(' ')[-3:])+'\n')
            for i in list_num:
                award = i.find('em',class_='archive--lotto__result-txt').text
                number_award = i.find('strong',class_='archive--lotto__result-number').text
                f.write('{} : {}\n'.format(award,number_award.strip().replace("\n",' ')))
        file_num += 1
        print('file',file_num)
    print('page',page)


if __name__ == '__main__':
    file_num = 1
    for page in range(1,20):
        lottery_number(page)
    