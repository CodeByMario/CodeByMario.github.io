import streamlit as st
from pathlib import Path
import os

# Define the directory where your files are located
directory = Path(CodeByMario.github.io
).parent

# Serve the static files
st.experimental_static(directory)

# Display the index.html file
html_file = directory / 'index.html'
if html_file.is_file():
    with open(html_file, 'r', encoding='utf-8') as f:
        st.markdown(f.read(), unsafe_allow_html=True)
