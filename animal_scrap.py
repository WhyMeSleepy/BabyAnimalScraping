from bs4 import BeautifulSoup
import requests


def animal_name():
    url_html = requests.get('https://www.zooborns.com/zooborns/baby-animal-names.html').text
    soup = BeautifulSoup(url_html, 'lxml')
    animals = soup.find('table',class_='zebra').tbody
    filter_animal = animals.find_all('td')
    baby_filter = animals.find_all('td')[-1]
    count = 1
    i = 0
    list_baby_name = []
    for baby_animal in filter_animal:
        baby_name = baby_animal.text
        if baby_name != '':
            if count % 2 == 0:
                list_baby = baby_name.split(' ')
                baby = ''.join(list_baby)
                list_baby_name.append(baby)
            count += 1


    for animal in filter_animal:
        tage_name_animal = animal.find('a')
        

        if tage_name_animal is not None:
            name_animal = tage_name_animal.text.replace(' ','').strip()
            if name_animal != '':
                with open(f'animals/{i}.txt','w') as f:
                    f.write(f'Animal : {name_animal}\n')
                    f.write(f'Baby Name : {list_baby_name[i]}')
                    i += 1

if __name__ == '__main__':
    animal_name()