import pandas as pd
from matplotlib import pyplot as plt
from services.autovit.analysis.import_export import import_from_excel
import pyautogui
import numpy as np

def screen_size():
    width, height= pyautogui.size()
    return (width/100,height/100)

def start_grafice(marca_selectata):
    df = pd.read_excel('masini.xlsx', f'{marca_selectata}')
    w,h=screen_size()
    fig1, (g1, g2)= plt.subplots(nrows=1, ncols=2)
    fig2, (pc1, pc2, pc3)=plt.subplots(nrows=1, ncols=3)
    fig1.set_size_inches(w/2, h/2)
    fig2.set_size_inches(w/2, h/2)

    df.dropna(subset=['pret'], inplace=True)
    df.dropna(subset=['kilometraj'], inplace=True)
    df.dropna(subset=['tip_vanzator'], inplace=True)
    df.dropna(subset=['combustibil'], inplace=True)
    df.dropna(subset=['cutie_viteze'], inplace=True)
    df.dropna(subset=['model'], inplace=True)

    df['pret'] = df['pret'].apply(lambda x: int(x.replace(" ", "").split(',',1)[0]))
    df['kilometraj'] = df['kilometraj'].apply(lambda x: int(x.replace(" ","").replace("km","")))
    df['tip_vanzator'] = df['tip_vanzator'].apply(lambda x: str(x.split(' ',1)[0]))
    df['combustibil'] = df['combustibil'].apply(lambda x: str(x.split(' ',1)[0]))
    df['cutie_viteze'] = df['cutie_viteze'].apply(lambda x: str(x.split(' ',1)[0]))

    df = df.astype({"pret": 'int32', "kilometraj": 'int32', "tip_vanzator":'string', "combustibil":'string', "cutie_viteze":'string'})
    df=df.loc[df['kilometraj'] < 500000] 
    pret_model(df, g1)
    kilometraj_pret(df, g2)
    fig1.set_facecolor("#68A4A5")
    fig1.tight_layout()
    fig1.show()

    tip_vanzator(df, pc1)
    combustibil(df,pc2)
    cutie_viteze(df, pc3)

    fig2.suptitle('Informatii despre tipurile de vanzatori, combustibilii folositi si cutia de viteze')
    fig2.set_facecolor("#b0a8b9")
    fig2.tight_layout()
    fig2.show()

def pret_model(df, g):
    # df1=df.groupby(['model'])['pret'].mean().round(0)
    df1=df.groupby(['model'])['pret'].mean().astype(int)

    df1.plot(kind='bar', x='model', y='pret', color="#4C8055", ax=g, rot=90) 

    g.set_facecolor("#D9DAD9")
    g.set_xlabel("Modelul masinii")
    g.set_ylabel("Pretul masinii")
    g.set_title("Pretul mediu dupa marca")

def kilometraj_pret(df, g):
    dfg=df.groupby(['kilometraj'])['pret'].mean().astype(int)
    df1=dfg.reset_index()

    df1.plot(kind='line', x='kilometraj', y='pret', color="#4C8055", ax=g, rot=90)
    g.set_facecolor("#D9DAD9")
    g.set_xlabel("Kilometraj")
    g.set_ylabel("Pretul masinii")
    g.set_title("Pretul in functie de kilometraj")

    suma_preturi=0
    count_masini=0
    for x in df['pret']:
        suma_preturi=suma_preturi+x
        count_masini += 1
    pret_mediu_masina=suma_preturi/count_masini

    g.fill_between(x=df1['kilometraj'], y1=df1['pret'], y2=pret_mediu_masina, where=(df1['pret']>pret_mediu_masina), 
                   interpolate=True, color='#B25E57', alpha=0.25, label='pret peste medie')
    g.fill_between(x=df1['kilometraj'], y1=df1['pret'], y2=pret_mediu_masina, where=(df1['pret']<=pret_mediu_masina), 
                   interpolate=True, color='#4C8055', alpha=0.25, label='pret sub medie')
    g.axhline(y=pret_mediu_masina, color='#BF642C', linestyle='--', linewidth=1.35, label='Media pretului unei masini')

def tip_vanzator(df, g):
    dfg = df.groupby(['tip_vanzator'])['pret'].count().astype(int)
    df1 = dfg.reset_index()
    explode_tip_vanzator=[0.05 for x in df1['tip_vanzator']]
    labels_tip_vanzator=[x for x in df1['tip_vanzator']]
    colors_tip_vanzator=['#3C5B6F','#948979','#DFD0B8','#4b4453','#845ec2']

    df1.plot(kind='pie', y='pret', ax=g, autopct='%1.0f%%', labels=labels_tip_vanzator, colors=colors_tip_vanzator,
           shadow=True, explode=explode_tip_vanzator, wedgeprops={'edgecolor':'black'})
    
    g.set_ylabel("")
    g.legend(loc='upper right', bbox_to_anchor=(1.15,1.15), borderaxespad=0)


def combustibil(df, g):
    dfg = df.groupby(['combustibil'])['pret'].count().astype(int)
    df1 = dfg.reset_index()
    explode_combustibil=[0.05 for x in df1['combustibil']]
    labels_combustibil=[x for x in df1['combustibil']]
    colors_combustibil=['#3C5B6F','#948979','#DFD0B8','#4b4453','#845ec2']

    df1.plot(kind='pie', y='pret', ax=g, autopct='%1.0f%%', labels=labels_combustibil, colors=colors_combustibil,
             shadow=True, explode=explode_combustibil, wedgeprops={'edgecolor':'black'})
    
    g.set_ylabel("")
    g.legend(bbox_to_anchor=(1.15,1.15), loc='upper right', borderaxespad=0)


def cutie_viteze(df, g):
    dfg = df.groupby(df['cutie_viteze'])['pret'].count().astype(int)
    df1 = dfg.reset_index()
    explode_cutie_viteze=[0.05 for x in df1['cutie_viteze']]
    labels_cutie_viteze=[x for x in df1['cutie_viteze']]
    colors_cutie_viteze=['#3C5B6F','#948979','#DFD0B8','#4b4453','#845ec2']

    df1.plot(kind='pie', y='pret', ax=g, autopct='%1.0f%%', labels=labels_cutie_viteze, colors=colors_cutie_viteze,
             shadow=True, explode=explode_cutie_viteze, wedgeprops={'edgecolor':'black'})

    g.set_ylabel("")
    g.legend(bbox_to_anchor=(1.15,1.15), loc='upper right', borderaxespad=0)
