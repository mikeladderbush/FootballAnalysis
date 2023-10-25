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

app = tk.Tk()
app.title("Football Stat Analyzer")
app.geometry("720x250")

display_label = Label(app, text="", font=('Helvetica 13'))
display_label.pack()

selected_alias_var = tk.StringVar()
selected_stat_var = tk.StringVar()
selected_week_var = tk.StringVar()

stat_vector = []

def on_combobox_select(event):
    selected_alias_var.set(url_combobox.get())
    
def add_stat_to_box():
    selected_stat_var = stat_combobox.get()
    stat_box.insert(tk.END, selected_stat_var)
    stat_vector.append(selected_stat_var)
    
url_combobox = ttk.Combobox(app, values=list(pfr_link_list.url_aliases.keys()), width=50, textvariable=selected_alias_var)
url_combobox.set(list(pfr_link_list.url_aliases.keys())[0]) 
url_combobox.pack(pady=10)

stat_combobox = ttk.Combobox(app, values=list(stat_enum.stat_list.keys()), width=50, textvariable=selected_stat_var)
stat_combobox.set(list(stat_enum.stat_list.keys())[0]) 
stat_combobox.pack(pady=10)

add_chosen_stat = tk.Button(app,text="Add Stat", command=add_stat_to_box)
add_chosen_stat.pack()

fetch_chosen_stats = tk.Button(app, text="Analyze Chosen Stats", command=lambda: data_fetch_functions.fetch_chosen_stats(pfr_link_list.url_aliases.get(selected_alias_var.get()), stat_vector))
fetch_chosen_stats.pack()

fetch_spreads = tk.Button(app, text="Fetch Spreads", command=lambda: data_fetch_functions.fetch_spread_and_result(spread_list_get(selected_alias_var.get())))
fetch_spreads.pack()

stat_box = tk.Listbox(app)
stat_box.pack()

app.mainloop()
