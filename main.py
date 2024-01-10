import requests
from bs4 import BeautifulSoup
import pandas as pd

base_url = 'https://www.payscale.com/college-salary-report/majors-that-pay-you-back/bachelors'
page_number = 1
data = []

while page_number < 33:
    url = f'{base_url}/page/{page_number}'  
    response = requests.get(url)
    soup = BeautifulSoup(response.text, 'html.parser')

    table = soup.find('table', {'class': 'data-table'})  
    
    if not table:
        break

    for row in table.find_all('tr')[1:]:  
        columns = row.find_all('td')
        row_data = [column.text.strip() for column in columns]
        data.append(row_data)

    
    page_number += 1

columns = ['Rank', 'Major', 'Degree Type', 'Early Career Pay', 'Mid-Career Pay', '% High Meaning']

df = pd.DataFrame(data, columns=columns)

df.to_csv('salaries_by_major(new).csv', index=False)  