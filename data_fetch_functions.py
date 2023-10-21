import requests
import json
import data_analysis_functions
from bs4 import BeautifulSoup

x = []

def fetch_total_yards(selected_alias, selected_url):
    if selected_url:
        response = requests.get(selected_url)
        if response.status_code == 200:
            soup = BeautifulSoup(response.text, 'html.parser')
            data = soup.find('td', {'class': 'right', 'data-stat': 'total_yards'})
            if data:
                print("Total Yards for", selected_alias + ":", data.text)
            else:
                print('Data not found.')
        else:
            print('Failed to retrieve the web page.')

def fetch_yards_per_game_with_opponent(selected_alias, selected_url):
    if selected_url:
        response = requests.get(selected_url)
        if response.status_code == 200:
            soup = BeautifulSoup(response.text, 'html.parser')
            yards = soup.find_all(attrs={'class': 'right', 'data-stat': 'yards_off'})
            opponents = soup.find_all(attrs={'class': 'left', 'data-stat': 'opp'})
            if yards and opponents:
                for opponent, yard in zip(opponents, yards):
                    print(opponent.get_text())
                    print(yard.get_text())
                    x.append(yard.get_text())
            else:
                print('Data not found.')
            
            data_analysis_functions.create_graph(x)
            
        else:
            print('Failed to retrieve the web page.')
            
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
            
def fetch_quarterback(selected_url):
    if selected_url:
        response = requests.get(selected_url)
        if response.status_code == 200:
            soup = BeautifulSoup(response.text, 'html.parser')
            quarterback_data = soup.find_all('td', {'data-stat': 'player'})
            if quarterback_data:
                for player in quarterback_data:
                    player_name = player.get_text()
                    print(f"Player Name: {player_name}")
            else:
                print("No quarterback data found on the page.")
        else:
            print(f"Failed to retrieve the URL. Status Code: {response.status_code}")
    else:
        print("No URL provided.")

def print_soup(selected_alias, selected_url):
    if selected_url:
        response = requests.get(selected_url)
        if response.status_code == 200:
            soup = BeautifulSoup(response.text, 'html.parser')
            print(soup.prettify())