import streamlit as st
st.title('Mantenimiento predictivo 🚀')
# ----------- Sidebar
st.sidebar.title('¡Bienvenid@!')
page = st.sidebar.selectbox('Menú de opciones', ['Principal', "Predicción", "Recalibrado"])

st.sidebar.markdown("""---""")
st.sidebar.write("By [Ignacio Sigüenza Sierra](https://github.com/nachosiguenza)")
st.sidebar.image("img/CUNEF.png", width=150)

if page == "Recalibrado":
    st.markdown("""Hola mundo""")

if page == 'Predicción':
    print('Hola')

else:
    st.markdown("""
    Esta aplicación web conforma la última etapa del presente proyecto de **optimización** de **mantenimiento** en **equipamiento industral**, su **puesta en producción**.
    Desde ella se pueden realizar **predicciones** para distintos valores de los **sensores** situados
    en el interior de los **motores Turbofan** de la NASA 🧑🏻‍🚀, por medio de la interfaz de usuario.
    
    Asímismo, se puede llevar a cabo un **reentrenamiento** con **nuevos conjuntos de datos/batch** para **corregir** una posible **desviación** del modelo (**sesgo de varianza**),
    imitando lo que se llevaría a cabo en un entorno puramente productivo.

    La arquitectura de la página web ha sido desarrollada íntegramente en **Python**, por medio del framework de frontend **Streamlit**, y
    **MLflow** para cubrir las necesidades a nivel de backend (REST API, base de datos), al margen de su utilización en el **tracking** de los **experimentos/modelos de ML** 🤖

    Finalmente, añadir que el presente dashboars tiene una **finalidad puramente académica/demostrativa**, pero podría ser **adaptada**
    e **implementada** con facilidad a un **entorno industrial** 🏭
    """
    )
