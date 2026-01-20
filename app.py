import streamlit as st
import pandas as pd
import numpy as np

st.set_page_config(page_title="My First Streamlit App", layout="centered")

st.title("🚀 My First Streamlit Application")
st.write("This is a simple interactive Streamlit app.")

# User input
name = st.text_input("Enter your name:")
age = st.slider("Select your age", 1, 100, 25)

if st.button("Submit"):
    st.success(f"Hello {name}! You are {age} years old.")

st.divider()

# Data example
st.subheader("📊 Random Data Example")
data = pd.DataFrame(
    np.random.randn(10, 3),
    columns=["A", "B", "C"]
)

st.dataframe(data)
st.line_chart(data)
