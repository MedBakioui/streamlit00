import streamlit as st
import pandas as pd

st.title("Ma première aplication Streamlit")
st.write("Mon premier texte")

data = pd.DataFrame({
    'Mois':['Janvier', 'Février', 'Mars', 'Avril', 'Mai', 'Juin'],
    'Ventes':[10,20,30,40,50,60]
})

niveaux = st.sidebar.slider("Ton niveaux d'energie " , 0, 50 ,100)

data_filtre = data[data['Ventes'] > niveaux]

col1, col2 = st.columns(2)

with col1:
    st.header("Colonne 1")
    st.write("Je suis à gauche ! 👈")
    st.line_chart(data_filtre.set_index('Mois'))

with col2:
    st.header("Colonne 2")
    st.write("Je suis à droite ! 👉")
    st.line_chart(data.set_index('Mois'))

if st.button("Cliquez moi"):
    st.write("Vous avez cliqué !")



st.write("L'esnergie est a : ", niveaux)


st.write("---") # Une ligne de séparation visuelle
st.header("Mes Données")




if st.checkbox("Afficher les données"):
    st.write(data)

# Coordonnées de Paris, Lyon et Marseille
map_data = pd.DataFrame(
    [[48.8566, 2.3522], [45.7640, 4.8357], [43.2965, 5.3698]],
    columns=['lat', 'lon']
)

st.map(map_data)