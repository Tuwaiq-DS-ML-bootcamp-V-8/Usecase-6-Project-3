"""
import streamlit as st
import pandas as pd
import plotly.express as px

# Load the dataset
df = pd.read_csv('FilteredRiyadhVillasAqar.csv')

df.dropna(subset=['price'], inplace=True)

# Streamlit app title
st.title("Riyadh Real Estate Price")

# Sidebar for user inputs
st.sidebar.header('Filter Property Features')

# User inputs for filtering (interactive)
selected_location = st.sidebar.selectbox('حدد اي منطقة في الرياض', df['location'].unique())
selected_front = st.sidebar.selectbox('حدد اتجاه واجهة المبنى', df['front'].unique())
#lounges = st.sidebar.slider('Number of Lounges', int(df['lounges'].min()), int(df['lounges'].max()), 1)
street_width = st.sidebar.slider('حدد عرض الشارع المقابل', float(df['streetWidth'].min()), float(df['streetWidth'].max()), 10.0)
property_age = st.sidebar.slider('حدد عمر المبنى', int(df['propertyAge'].min()), int(df['propertyAge'].max()), 10)

# More filters for binary features
driver_room = st.sidebar.selectbox('Driver Room', df['driverRoom'].unique())
tent = st.sidebar.selectbox('Tent', df['tent'].unique())
patio = st.sidebar.selectbox('Patio', df['patio'].unique())
maid_room = st.sidebar.selectbox('Maid Room', df['maidRoom'].unique())
elevator = st.sidebar.selectbox('Elevator', df['elevator'].unique())
furnished = st.sidebar.selectbox('Furnished', df['furnihsed'].unique())
pool = st.sidebar.selectbox('Pool', df['pool'].unique())
basement = st.sidebar.selectbox('Basement', df['basement'].unique())

# Build filter conditions based on user input
filtered_df = df[
    (df['location'] == selected_location) &
    (df['front'] == selected_front) &
    #(df['lounges'] == lounges) &
    (df['streetWidth'] == street_width) |
    (df['propertyAge'] == property_age) |
    (df['driverRoom'] == driver_room) |
    (df['tent'] == tent) |
    (df['patio'] == patio) |
    (df['maidRoom'] == maid_room) |
    (df['elevator'] == elevator) |
    (df['furnihsed'] == furnished) |
    (df['pool'] == pool) |
    (df['basement'] == basement)
]

# Display line chart of price if the filtered DataFrame is not empty
if not filtered_df.empty:
    # Sort by price to display a smooth line
    filtered_df = filtered_df.sort_values(by='price')
    
    # Create the line chart using Plotly
    fig = px.line(filtered_df, x=filtered_df.price, y='count', title='تغير السعر')
    st.plotly_chart(fig)
else:
    st.write("لايوجد بيانات")
"""




import streamlit as st
import pandas as pd
import plotly.express as px

# Load the dataset
df = pd.read_csv('FilteredRiyadhVillasAqar.csv')

# Streamlit app title
st.title("Riyadh Real Estate Price")

st.write("""
Welcome to the Riyadh Real Estate Price Explorer! This app allows you to progressively filter properties based on various factors and view the price trends dynamically.
Start by selecting a **Location** and continue adjusting the filters as you scroll down.
""")



# Step 1: Filter by Location
st.header("حدد اي منطقة في الرياض")
selected_location = st.selectbox('منطقة', df['location'].unique())

st.write("First, select a location to start narrowing down the available properties. The chart below will update to reflect the price trends for the selected location.")
filtered_df = df[df['location'] == selected_location]

# Display the updated line chart after filtering by location
if not filtered_df.empty:
    filtered_df = filtered_df.sort_values(by='price')
    fig = px.line(filtered_df.price, x=filtered_df.price.index, y='price', title=f'Price Trend for Location: {selected_location}')
    st.plotly_chart(fig)
else:
    st.write("لايوجد بيانات")

# Step 2: Filter by Front
st.header("حدد خيارات واجهة المبنى")
selected_front = st.selectbox('الخيارات', filtered_df['front'].unique())

# Filter the data based on the selected front
filtered_df = df[df['front'] == selected_front]

# Display the updated line chart after filtering by front
if not filtered_df.empty:
    filtered_df = filtered_df.sort_values(by='price')
    fig = px.line(filtered_df.price, x=filtered_df.price.index, y='price', title=f'Price Trend for Front: {selected_front}')
    st.plotly_chart(fig)
else:
    st.write("لايوجد بيانات")

st.write("""
---
### Step 2: Select Front
Now, refine your search further by selecting the **Front** of the property. This will further narrow down the properties that match your location and front preferences.
""")

st.header("حدد عرض الشارع المقابل")
street_width = st.slider('حدد عرض الشارع المقابل', float(df['streetWidth'].min()), float(df['streetWidth'].max()), 10.0)

# Filter the data based on the streetWidth
filtered_df = df[df['streetWidth'] <= street_width]

# Display the updated line chart after filtering by street_width
if not filtered_df.empty:
    filtered_df = filtered_df.sort_values(by='price')
    fig = px.line(filtered_df.price, x=filtered_df.price.index, y='price', title=f'Price Trend for street_width: {street_width}')
    st.plotly_chart(fig)
else:
    st.write("لايوجد بيانات")

# Add more steps for other factors in a similar manner (e.g., Street Width, Property Age, etc.)


