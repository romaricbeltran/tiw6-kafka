import pandas as pd
from datetime import date
today = date.today()
# YYmmdd
UTC = "00"
d1 = today.strftime("%Y%m%d")
file = pd.read_csv('archive/'+d1+UTC+'lyon.txt')
fileinteret = file[["numer_sta","date","pmer","ff","t","u","vv"]].to_csv('archive/select'+d1+UTC+'lyon.csv', index=False)
