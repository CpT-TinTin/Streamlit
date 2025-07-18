
import streamlit as st
import pandas as pd
st.markdown(" # Streamlit App for DataFrame Display")
st.header("Data Visualization")
st.badge("Ceva nou")
st.caption("Data Visualization12")
st.latex(r'''
    a + ar + a r^2 + a r^3 + \cdots + a r^{n-1} =
    \sum_{k=0}^{n-1} ar^k =
    a \left(\frac{1-r^{n}}{1-r}\right)
    ''')


if st.button("Say hello"):
    st.write("Hello there!")
else:
    st.write("Goodbye")

st.page_link("app.py", label="Home")
st.page_link("pages/Despreeu.py", label="Despre Mine")
st.page_link("pages/page_2.py", label="Page 2")
st.page_link("http://www.google.com", label="Google", icon="🌎")
st.page_link("pages/page_3.py", label="Form Page", icon="📄")