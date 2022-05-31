# from bs4 import BeautifulSoup
# import requests , json

# html_lottery = requests.get('https://www.thairath.co.th/lottery/archive').text
# soup = BeautifulSoup(html_lottery,'lxml')
# all_data = json.loads(soup)


# lotteries = all_data.find_all('div',class_='css-1tw01wy ecgl95t26')
# for lottery in lotteries:
#     date = lottery.find('h2',class_='css-uppvlb efr6tej2').span.text
#     print(date)

#     print('')