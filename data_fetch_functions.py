import requests
import json
import data_analysis_functions
from bs4 import BeautifulSoup
            
def fetch_chosen_stats(selected_url, stat_vector):
    x = []
    if selected_url:
        response = requests.get(selected_url)
        if response.status_code == 200:
            soup = BeautifulSoup(response.text, 'html.parser')
            print(stat_vector)
            for item in stat_vector:
                chosen_stat = soup.find_all(attrs={'class': 'right', 'data-stat': item})
                if chosen_stat:
                    for stat in chosen_stat:
                        if stat.get_text():
                            x.append(int(stat.get_text()))
                        else:
                            x.append(int(0))
                else:
                    print('Data not found.\n')
                #data_analysis_functions.create_graph(x)
        else:
            print('Failed to retrive the web page.')
            
#def fetch_spread_and_result(selected_url):