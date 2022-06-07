#Import
import streamlit as st
import betstats
from time import sleep

l=""
ligas = ['','B1 - Divisão A Belga', 'D1 - Bundesliga 1 Alemã', 'D2 - Bundesliga 2 Alemã','E1 - EFL Championship','E2 - Inglaterra Liga 1'
      ,'E3 - Inglaterra Liga 2','EC - National League','I2 - Séria B Italiana','N1 - Eredivisie Neerlandês',
      'P1 - Primeira Liga Portuguesa','SC2 - Primeira Divisão Escocesa', 'SC3 - Segunda Divisão Escocesa',
      'SP1 - La Liga Espanhola','SP2 - Segunda Divisão Espanhola','T1 -Super Liga Turca']

placeholder = st.empty()
#selectbox
options= st.selectbox('Select the League',ligas)

if options!="":
      l=options.split()[0]
      name = options.split()[2]
      placeholder.empty()

st.write('You selected:', options)

try:
    #Obtendo Dados e figuras
    var,descritive , vo, opp =betstats.liga(l)
    var["Metrics"] = var.index.astype(str)
    var = var.reset_index()
    var = var.drop("index",axis=1)
    var = var.set_index("Metrics")
    var = var.drop("count",axis=0)

    #Header
    st.image("https://tv2play.hu/assets/4/6/461830e3-7fe8-45ff-8737-19598e45748c/fileAsset/premier_league_cover.jpg")
    st.title('**Premier League Analysis**')
    st.text('by: Bruno Brasil')

    #body
    # Primeira parte
    st.write('Report from Premier League in order to beat the Betting Houses.')
    st.subheader('Historical and Current Bet Peformance')
    st.image('fig1.png')
    st.subheader('Performance Summary')
    st.table(var)

    # Segunda Parte
    st.subheader('Statistical Analysis')
    st.image('fig2.png')
    st.subheader('Descritive Analysis')
    st.table(descritive)
    st.subheader(vo)
    st.write(opp)

    # Terceira parte
    st.subheader('Strategy Results')
    st.image("fig3.png")

except:
    pass
