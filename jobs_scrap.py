from bs4 import BeautifulSoup
import requests

def data_jobs(page):
    html_job = requests.get(f'https://th.jobsdb.com/th/th/search-jobs/python/{str(page)}').text
    soup = BeautifulSoup(html_job,'lxml')
    jobs = soup.find_all('div',class_='sx2jih0 zcydq89e zcydq88e zcydq872 zcydq87e')

    for i,job in enumerate(jobs):
        job_position = job.find('span',class_='sx2jih0').text
        company_name = job.find('span',class_='sx2jih0 zcydq84u _18qlyvc0 _18qlyvc1x _18qlyvc1 _18qlyvca').text
        location = job.find('span',class_='sx2jih0 zcydq84u zcydq80 iwjz4h0').text
        salary = job.find_all('span',class_='sx2jih0 zcydq84u _18qlyvc0 _18qlyvc1x _18qlyvc3 _18qlyvc7')[-1].text
        skills = job.find_all('li',class_='sx2jih0 zcydq86i')

        with open(f'jobsPosts/{page}{i}.txt','w', encoding='utf-8') as f:
            f.write(f'Job Positions : {job_position}\n')
            f.write(f'Company : {company_name}\n')
            f.write(f'Company Location : {location}\n')
            if 'THB' in salary:
                f.write(f'Salary : {salary}\n')
            else:
                f.write(f'Salary : No Infomation\n')
            if len(skills) > 0:
                f.write('  skill  \n')
                for skill in skills:
                    f.write(f'- {skill.text}\n')

            
if __name__ == '__main__':
    for page in range(1,46):
        data_jobs(page)