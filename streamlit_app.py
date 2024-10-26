#Import all relevant libraries
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from scipy.stats import zscore
from ydata_profiling import ProfileReport
from bidi.algorithm import get_display  # Fixes Arabic display
import arabic_reshaper  # Reshapes Arabic characters for display
import streamlit as st

expensive_hoods = pd.read_csv('./expensive_hoods.csv')
land_count_by_hood_df = pd.read_csv('./land_count_by_hood.csv')
neighborhood_purpose_counts = pd.read_csv('./neighborhood_purpose_counts.csv')

st.title('Welcome to the Seattle Real Estate Analysis App')