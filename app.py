import streamlit as st
import seaborn as sns
import pandas as pd
import matplotlib.pyplot as plt
import os

taxis = sns.load_dataset("taxis")

PRENOM = "Nathalie"

def afficher_image(arrondissement):
    dossier_images = r"G:\Mon Drive\Colab Notebooks\Streamlit\Images"
    images = {
        "Bronx": "image_1.jpg",      
        "Brooklyn": "image_2.jpg",   
        "Manhattan": "image_3.jpg",  
        "nan": "image_4.jpg",        
        "Queens": "image_5.jpg"      
    }


    if arrondissement in images:
        image_path = os.path.join(dossier_images, images[arrondissement])
        if os.path.exists(image_path):
            st.image(image_path, caption=f"Image pour {arrondissement}")
        else:
            st.warning(f"Image non disponible pour l'{arrondissement}.")
    else:
        st.warning(f"Image non disponible pour l'{arrondissement}.")

st.title(f"Bienvenue sur l'application de {PRENOM} - Choix de l'arrondissement")

arrondissement = st.selectbox("Choisissez un arrondissement de récupération", taxis["pickup"].dropna().unique())

afficher_image(arrondissement)


st.write("Voici les données du taxi pour l'arrondissement choisi :")
data_filtrée = taxis[taxis["pickup"] == arrondissement]
st.dataframe(data_filtrée)


fig, ax = plt.subplots()
sns.histplot(data_filtrée, x="fare", kde=True, ax=ax)
ax.set_title(f"Distribution des tarifs pour l'{arrondissement}")
st.pyplot(fig)



