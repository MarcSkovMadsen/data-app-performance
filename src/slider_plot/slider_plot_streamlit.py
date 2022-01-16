import plotly.express as px


def plot(count):
    x = [str(i) for i in range(0, count)]
    y = list(range(0, count))
    return px.bar(x=x, y=y)


import streamlit as st

count = st.sidebar.slider(label="Count", min_value=1, max_value=50, value=10)
st.write(plot(count))