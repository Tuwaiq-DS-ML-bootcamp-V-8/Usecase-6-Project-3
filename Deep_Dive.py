import streamlit as st
import pandas as pd

# Load the dataset
df = pd.read_csv('RiyadhVillasAqar.csv')


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

# Display price statistics if the filtered DataFrame is not empty
if not filtered_df.empty:
    min_price = filtered_df['price'].min()
    max_price = filtered_df['price'].max()
    avg_price = filtered_df['price'].mean()

    # Display results on the screen
    st.write(f"### Price Statistics After Filtering:")
    st.write(f"- Minimum Price: {min_price:.2f} SAR")
    st.write(f"- Maximum Price: {max_price:.2f} SAR")
    st.write(f"- Average Price: {avg_price:.2f} SAR")
else:
    st.write("No properties match your filter criteria.")



