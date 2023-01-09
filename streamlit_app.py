import streamlit as st
import pandas as pd
import datetime
import altair as alt
import numpy as np
import dask.dataframe as dd
from google.cloud import storage

st.set_page_config(page_title="Cosmetic Products Sales",
                page_icon = ":cosmetic:",
                layout="wide",
                initial_sidebar_state='expanded')


with open('style.css') as f:
    st.markdown(f'<style>{f.read()}</style>', unsafe_allow_html=True)

st.title(":bar_chart: Products Sales Dashboard")
st.markdown("##")
