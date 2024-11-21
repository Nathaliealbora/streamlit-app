import streamlit as st
st.title("Bienvenue sur le site web de Nathalie")
arrondissement = st.selectbox("Indiquez votre arrondissement de récupération",
['Brooklyn', 'Bronx', 'Manhattan', 'Queens', 'nan'])

st.write(f"Tu as choisi : {arrondissement}")

if arrondissement == 'Brooklyn':
    st.image('G:/Mon Drive/Colab Notebooks/Streamlit/Images quetes/Brooklyn.jpg')
elif arrondissement == 'Bronx':
    st.image('G:/Mon Drive/Colab Notebooks/Streamlit/Images quetes/Bronx.jpg')
elif arrondissement == 'Manhattan':
    st.image('G:/Mon Drive/Colab Notebooks/Streamlit/Images quetes/Manhattan.jpg')
elif arrondissement == 'Queens':
    st.image('G:/Mon Drive/Colab Notebooks/Streamlit/Images quetes/Queens.jpg')
elif arrondissement == 'nan':
    st.image('G:/Mon Drive/Colab Notebooks/Streamlit/Images quetes/nan.jpg')