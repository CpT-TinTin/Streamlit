import streamlit as st
import pandas as pd
import numpy as np

st.title("Streamlit Demo Page")

st.write("This page demonstrates various Streamlit functions:")

if st.button("Click me!"):
    st.success("Button clicked!")

number = st.slider("Pick a number", 0, 100, 25)
st.write(f"You selected: {number}")

data = pd.DataFrame(
    np.random.randn(20, 3),
    columns=['A', 'B', 'C']
)
st.line_chart(data)

st.sidebar.header("Sidebar Example")
option = st.sidebar.selectbox("Choose an option", ["Option 1", "Option 2", "Option 3"])
st.sidebar.write(f"You selected: {option}")