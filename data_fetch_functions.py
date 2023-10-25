import requests
import json
import data_analysis_functions
from bs4 import BeautifulSoup

x = []
            
def fetch_chosen_stat(selected_url, selected_attr):
    if selected_url:
        response = requests.get(selected_url)
        if response.status_code == 200:
            soup = BeautifulSoup(response.text, 'html.parser')
            if selected_attr == 'opp':
                chosen_stat = soup.find_all(attrs={'class': 'left', 'data-stat': selected_attr})
            elif selected_attr == 'team_record':
                chosen_stat = soup.find_all(attrs={'class': 'center', 'data-stat': selected_attr})
            else:
                chosen_stat = soup.find_all(attrs={'class': 'right', 'data-stat': selected_attr})
            if chosen_stat:
                for stat in chosen_stat:
                    print(stat.get_text())
            else:
                print('Data not found.\n')
        else:
            print('Failed to retrive the web page.')
            
#def fetch_spread_and_result(selected_url):
    