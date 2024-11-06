#IN ORDER TO RUN THIS SCRIPT FIRST RUN THIS COMMAND IN THE TERMINAL -> pip install -r requirements.txt

import requests
from bs4 import BeautifulSoup

import pandas as pd

headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/92.0.4515.107 Safari/537.36'}

response = requests.get('https://sih.gov.in/sih2024PS?technology_bucket=QWxs&category=U29mdHdhcmU=&organization=QWxs&organization_type=QWxs',headers = headers,verify = False)


with open('sih_software.html','w',encoding = 'UTF-8') as f:
    file = f.write(response.text)


with open('sih_software.html','r',encoding = 'UTF-8') as f:
    file = f.read()

soup = BeautifulSoup(file,'html.parser')

modal_bodies = [[data.get_text() for data in item.find_all(name = 'div',class_ = 'style-2')] for item in soup.find_all(name = 'div',class_ = 'modal-body')]


modal_dict_df = {
    'id':[],
    'problem_statement':[],
    'description':[]
} 

for modal_data in modal_bodies:
    try:
        modal_dict_df['id'].append(modal_data[0])
        modal_dict_df['problem_statement'].append(modal_data[1])
        modal_dict_df['description'].append(modal_data[2])
    except IndexError:
        pass
    
modal_dict_df_pandas = pd.DataFrame(modal_dict_df)
modal_dict_df_pandas.index = range(1, len(modal_dict_df_pandas) + 1)
modal_dict_df_pandas.to_excel("SIH_SOFTWARE.xlsx",)