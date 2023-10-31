import requests
import json
import data_analysis_functions
from bs4 import BeautifulSoup
            
def fetch_chosen_stats(selected_url, stat_vector):
    opponent_vector = []
    chosen_stat_vector = []
    vector_of_stat_vectors = []
    if selected_url:
        response = requests.get(selected_url)
        if response.status_code == 200:
            soup = BeautifulSoup(response.text, 'html.parser')
            opponent = soup.find_all(attrs={'class': 'left', 'data-stat': 'opp'})
            if opponent:
                for team in opponent:
                    if team.get_text():
                        opponent_vector.append(team.get_text())
            for item in stat_vector:
                chosen_stat = soup.find_all(attrs={'class': 'right', 'data-stat': item})
                if chosen_stat:
                    for stat in chosen_stat:
                        if stat.get_text():
                            chosen_stat_vector.append(int(stat.get_text()))
                        else:
                            chosen_stat_vector.append(int(0))                  
                else:
                    print('Data not found.\n')
                vector_of_stat_vectors.append(chosen_stat_vector)
                chosen_stat_vector = []
            vector_of_stat_vectors.append(opponent_vector)
            data_analysis_functions.create_graph(vector_of_stat_vectors)
        else:
            print('Failed to retrive the web page.')