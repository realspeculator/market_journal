import pandas as pd
import os
import numpy as np
from IPython.display import display

# Change This
TODAYS_DATE = "2023-10-26"

files_list = os.listdir("../../../live_portfolio/2023/010_2023/")
files_list.remove(".DS_Store") # Remove Mac's .DS_Store file.

def build_files_url(files_names):
    
    return "https://raw.githubusercontent.com/realspeculator/live_portfolio/main/2023/010_2023/" + files_names

def get_net_lq_value(url):
    
    df1 = pd.read_csv(url)
    net_lq = df1[df1["DATE"] == "Net Liquidating Value"].iloc[0,1]
    net_lq = float(net_lq.replace("$", "").replace(",", ""))
    
    return net_lq

urls = list(map(build_files_url, files_list))

repo_url = [i for i in urls if TODAYS_DATE in i][0]
df1 = pd.read_csv(repo_url)

# Positions
pos_start = np.where(df1['DATE'] == "Equities")[0][0] + 1

pos_end = (np.where(df1['DATE'] == "Profits and Losses")[0][0])


# Trades done today
trades_start = np.where(df1['DATE'] == "Account Trade History")[0][0] + 1
trades_end = np.where(df1['DATE'] == "Equities")[0][0] - 1

# Profit and Loss YTD

pnl_start = np.where(df1['DATE'] == "Profits and Losses")[0][0] + 1
pnl_end = np.where(df1['DATE'] == "Forex Account Summary")[0][0] - 1

pos_df = df1.iloc[pos_start+1:pos_end]
pos_df.columns = df1.iloc[pos_start].values
pos_df = pos_df.dropna(axis=1,how='all')

trades_df = df1.iloc[trades_start:trades_end]
trades_df.columns = df1.iloc[trades_start].values
trades_df = trades_df.dropna(axis=1,how='all').iloc[1:]

pnl_df = df1.iloc[pnl_start:pnl_end]
pnl_df.columns = df1.iloc[pnl_start].values
pnl_df = pnl_df.dropna(axis=1,how='all').iloc[1:]
