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

def on_combobox_select(event):
    selected_alias_var.set(url_combobox.get())

url_combobox = ttk.Combobox(app, values=list(pfr_link_list.url_aliases.keys()), width=50, textvariable=selected_alias_var)
url_combobox.set(list(pfr_link_list.url_aliases.keys())[0]) 
url_combobox.pack(pady=10)

stat_combobox = ttk.Combobox(app, values=list(stat_enum.stat_list.keys()), width=50, textvariable=selected_stat_var)
stat_combobox.set(list(stat_enum.stat_list.keys())[0]) 
stat_combobox.pack(pady=10)

spread_combobox = ttk.Combobox(app, values=list(spread_list.weeks.keys()), width=50, textvariable=selected_week_var)
spread_combobox.set(list(spread_list.weeks.keys())[0])
spread_combobox.pack(pady=10)

url_combobox.bind("<<ComboboxSelected>>", on_combobox_select)

fetch_chosen_stat = tk.Button(app, text="Fetch Chosen Stat", command=lambda: data_fetch_functions.fetch_chosen_stat(pfr_link_list.url_aliases.get(selected_alias_var.get()), stat_enum.stat_list.get(selected_stat_var.get())) )
fetch_chosen_stat.pack()

fetch_spreads = tk.Button(app, text="Fetch Spreads", command=lambda: data_fetch_functions.fetch_spread_and_result(spread_list_get(selected_alias_var.get())))
fetch_spreads.pack()

app.mainloop()
