import streamlit as st

# ----------- Sidebar
page = st.sidebar.selectbox('Page Navigation', ['Principal', "Predicción", "Recalibrado"])

st.sidebar.markdown("""---""")
st.sidebar.write("By [Ignacio Sigüenza Sierra](https://github.com/nachosiguenza)")
st.sidebar.image("../img/CUNEF.gif", width=100)