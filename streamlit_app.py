# Streamlit live coding script
import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import plotly.express as px
import plotly.graph_objects as go
from urllib.request import urlopen
import json
from copy import deepcopy

df = pd.read_csv('mpg.csv')
st.title('Intoduction to streamlit')
st.header('This is a header')

print("Plotly version:", px.__version__)
