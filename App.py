import streamlit as st
import pandas as pd

st.title ('Manejo de Dataframes')
st.sidebar.title('Herramientas')

archivo = st.sidebar.file_uploader ('Seleccione su archivo')
if archivo is None :
  st.write('Cargue el archivo a leer')
else :
  datos = pd.read_csv (archivo)
  st.write(datos)
