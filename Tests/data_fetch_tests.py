import requests
import data_fetch_functions
import pfr_link_list
import stat_enum
import spread_list
import data_analysis_functions
from bs4 import BeautifulSoup
import tkinter as tk
from tkinter import ttk 
from tkinter import *
import requests
import json


class TestCreateGraphFunction(unittest.TestCase):
    
    def connect_test():
        for key in pfr_link_list.url_aliases:
            response = requests.get(key)
            if response.status_code == 200:
                print("Successful Connection")

    def beautiful_soup_test():
        html = "<h1>test</h1>"
        soup = BeautifulSoup(html, "html.parser")
        test_title = soup.title.string
        assert test_title == "test"
        
    def TK_test():
        app = tk.Tk()
        app.title("Football Stat Analyzer")
        app.geometry("720x250")

        display_label = Label(app, text="", font=('Helvetica 13'))
        display_label.pack()   
        
    def test_create_graph(self):
            opponent_array = ['Opponent 1', 'Opponent 2', 'Opponent 3']
            data1 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18]
            data2 = [18, 17, 16, 15, 14, 13, 12, 11, 10, 9, 8, 7, 6, 5, 4, 3, 2, 1]

            plt.show = lambda: None

            try:
                create_graph(opponent_array, data1, data2)
            except Exception as e:
                self.fail(f"Function create_graph() raised an exception: {e}")
                
if __name__ == '__main__':
    unittest.main()