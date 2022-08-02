import streamlit as st
import pandas as pd


st.title('Mantenimiento predictivo 🚀')
# ----------- Sidebar
st.sidebar.image('img/Turbofan.png', use_column_width=True)
st.sidebar.title('¡Bienvenid@!')
page = st.sidebar.selectbox('Menú de opciones', ['Principal', "Predicción", "Recalibrado"])

st.sidebar.markdown("""---""")
st.sidebar.write("By [Ignacio Sigüenza Sierra](https://github.com/nachosiguenza)")
st.sidebar.image("img/CUNEF.png", width=75)
st.sidebar.markdown("""""")

if page == "Recalibrado":
    st.markdown("""Hola mundo""")

if page == 'Predicción':
    unit_number = st.number_input('unit_number')
    cycles = st.number_input('cycles')

    setting1 = st.number_input('set1')
    setting2 = st.number_input('set2')
    setting3 = st.number_input('set3')

    sensor1 = st.number_input('s1')
    sensor2 = st.number_input('s2')
    sensor3 = st.number_input('s3')
    sensor4 = st.number_input('s4')
    sensor5 = st.number_input('s5')
    sensor6 = st.number_input('s6')
    sensor7 = st.number_input('s7')
    sensor8 = st.number_input('s8')
    sensor9 = st.number_input('s9')
    sensor10 = st.number_input('s10')
    sensor11 = st.number_input('s11')
    sensor12 = st.number_input('s12')
    sensor13 = st.number_input('s13')
    sensor14 = st.number_input('s14')
    sensor15 = st.number_input('s15')
    sensor16 = st.number_input('s16')
    sensor17 = st.number_input('s17')
    sensor18 = st.number_input('s18')
    sensor19 = st.number_input('s19')
    sensor20 = st.number_input('s20')
    sensor21 = st.number_input('s21')


else:
    st.markdown("""
    Esta aplicación web conforma la última etapa del presente proyecto de **optimización** de **mantenimiento** en **equipamiento industral**, su **puesta en producción**.
    Desde ella se pueden realizar **predicciones** para distintos valores de los **sensores** situados
    en el interior de los **motores Turbofan** de la NASA 🧑🏻‍🚀, por medio de la interfaz de usuario.
    
    Asímismo, se puede llevar a cabo un **reentrenamiento** 📈 con **nuevos conjuntos de datos/batch** para **corregir** una posible **desviación** del modelo (**sesgo de varianza**),
    imitando lo que se llevaría a cabo en un entorno puramente productivo.

    La arquitectura de la página web ha sido desarrollada íntegramente en **Python**, por medio del framework de frontend **Streamlit**, y
    **MLflow** para cubrir las necesidades a nivel de backend (REST API, base de datos), al margen de su utilización en el **tracking** de los **experimentos/modelos de ML**. 🤖

    Finalmente, añadir que el presente dashboars tiene una **finalidad puramente académica/demostrativa**, pero podría ser **adaptada**
    e **implementada** con facilidad a un **entorno industrial**. 🏭
    """
    )
