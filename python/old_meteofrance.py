import re
import wget
import gzip
import os
import shutil
y=[18,19]
m=list(range(1,13))
for year in y:
    for month in m:
        if month <10:
            wget.download('http://192.168.76.159/data/meteo/synop/synop.20'+str(year)+'0'+str(month)+'.csv.gz', out='../hist_data_meteo_france/')
        else:
            wget.download('http://192.168.76.159/data/meteo/synop/synop.20'+str(year)+str(month)+'.csv.gz', out='../hist_data_meteo_france/')
files = os.listdir('../hist_data_meteo_france/')
reg=re.compile('synop\.([0-9][0-9][0-9][0-9][0-9][0-9])\.',re.IGNORECASE)
for file in files:
    if re.search(reg,file):
        with gzip.open('../hist_data_meteo_france/'+file) as gz:
            with open('../hist_data_meteo_france/'+file[:16], 'wb') as f_out:
                shutil.copyfileobj(gz, f_out)
        os.remove('../hist_data_meteo_france/'+file)
files = os.listdir('../hist_data_meteo_france/')
reg=re.compile('synop\.([0-9][0-9][0-9][0-9][0-9][0-9])\.',re.IGNORECASE)
for file in files:
    if re.search(reg,file):
        currf=pd.read_csv("../hist_data_meteo_france/"+file,sep=";")
ligneutile=currf[currf["numer_sta"]==7481].to_csv("../data_meteo_france/"+re.search(reg,file).group(1)+"lyon.csv",index=False)