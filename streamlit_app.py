import streamlit as st
import streamlit.components.v1 as components

# Read the contents of your index.html file
with open('index.html', 'r') as f:
    html_string = f.read()

# Use the components.html function to display the HTML in the app
components.html(html_string, height=800)
