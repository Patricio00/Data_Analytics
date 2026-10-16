import streamlit as st
import pandas as pd

st.title ('Manejo de Dataframes')
st.sidebar.title('Herramientas')

archivo = st.sidebar.file_uploader ('Seleccione su archivo')
