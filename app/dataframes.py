#Import
from github import Github
from pprint import pprint
import requests
import pandas as pd
import time
from urllib.request import urlopen
import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np

#Read data from github

#Archivos json
url="https://raw.githubusercontent.com/mayteet/PI01_DATA05/main/Datasets/netflix_titles.json"
f=requests.get(url)
data=f.json()
# Convertir el archivo de json en un DataFrame
netflix=pd.DataFrame(data)

#Archivos csv
amazon= pd.read_csv("https://raw.githubusercontent.com/mayteet/PI01_DATA05/main/Datasets/amazon_prime_titles.csv")
disney= pd.read_csv("https://raw.githubusercontent.com/mayteet/PI01_DATA05/main/Datasets/disney_plus_titles.csv")
hulu= pd.read_csv("https://raw.githubusercontent.com/mayteet/PI01_DATA05/main/Datasets/hulu_titles.csv") 

#Agregamos la columna de plataform y unimos las tablas
netflix["plataform"]= "netflix"
amazon["plataform"]="amazon"
disney["plataform"]="disney"
hulu["plataform"]="hulu"


#Unimos los dataframes
df=pd.concat([netflix, amazon, disney, hulu]) 

data_all=pd.DataFrame([])
Lista_wrong=["min", "Seasons","Season"]
df_analysis= df[["show_id","rating","plataform"]]

for elemento in Lista_wrong:
    
    # Filtrar el Dataframe por columna rating en el que se encuentre la palabra min, Seasons, Season
    df_analysis_filter= df_analysis.loc[df_analysis["rating"].str.contains(elemento, na=False)]
    data_all=pd.concat([data_all,df_analysis_filter])
    
data_all.rename(columns={'rating':"duration"}, inplace=True)


#Sacamos las variables del dataframe principal
df_analysis_2= df[["show_id","duration","plataform"]]
df_analysis_2=df_analysis_2.dropna(subset="duration")

#Juntamos las columnas
data_all=pd.concat([data_all, df_analysis_2])
data_all

#Limpieza de datos
data_all.rename(columns={'duration':"duration_2"}, inplace=True)


data_all["duration_2"]=data_all["duration_2"].str.replace(" min","")
data_all["duration_2"]=data_all["duration_2"].str.replace(" Seasons","")
data_all["duration_2"]=data_all["duration_2"].str.replace(" Season","")

#Juntamos todo en la tabla principal
df_final= pd.merge(df,data_all, on=["show_id","plataform"],how="left")