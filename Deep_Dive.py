

import streamlit as st
import pandas as pd
import plotly.express as px

# Load the dataset
df = pd.read_csv('FilteredRiyadhVillasAqar.csv')



# Example of embedding HTML
st.markdown("""
    <h1 style='text-align: center; color: blue;'>اختلاف اسعار الفلل بأختلاف العوامل</h1>
    <h1>
كلنا نعرف ان سعر الفله او البيت تختلف بأختلاف عوامل كثيرة مثل المنطقة ومساحة الارض وعوامل اخرى مثل 
عمر المبنى
وجود حديقة خارجية 
وجود مسبح 
الا اخره ....

         
لكن هل فكرت بالعوامل الاخرى مثل عرض الشارع المقابل         
اتجاه الواجه الامامية 

وكيف راح تأثر على السعر اذا ماقارنا اراضي بنفس المساحة وبنفس المنطقة لكن الشارع المقابل واتجاه الواجهة الامامية يختلف
</h1>
    <hr>
    <h2 style='color: green;'>اولا: حدد اي منطقة في الرياض"</h2>
    """, unsafe_allow_html=True)



# Step 1: Filter by Location
st.header("اولا: حدد اي منطقة في الرياض")
selected_location = st.selectbox('حدد المنطقة', df['location'].unique())
# Step 2: Sidebar for space
selected_space = st.sidebar.selectbox('حدد مساحة الفله', df['space'].unique())

st.write("اولا, حدد المنطقة في الرياض اللي على اساسها الرسم يظهر اختلاف الاسعار بتغير عامل اتجاه المبنى عرض الشارع")


filtered_df = df[df['location'] == selected_location]

# Display an animated bar chart showing the relationship between location and price
if not filtered_df.empty:
    st.subheader(f"اختلاف الاسعار في منطقة {selected_location}")
    fig = px.bar(filtered_df, x='front', y='price', animation_frame='streetWidth', animation_group='front', 
                 title=f'اختلاف الاسعار بتغير عاملين اتجاه المبنى و عرض الشارع {selected_location}',
                 labels={'price': '', 'front': 'Property Front', 'streetWidth': 'width of street'},
                 text='price'  # Add price labels on top of the bars
                 )
                 
    # Automatically show the price text on top of each bar
    # Customize the layout of the chart
    # Customize the layout: remove y-axis, increase bar height
    # Price (SAR)
    # Ensure that the price is shown on top of the bars
    fig.update_traces(texttemplate='%{y:.2f}', textposition='outside')
    fig.update_layout(
    width=800,  # Set the width in pixels
    height=600,  # Set the height in pixels
    bargap=0.1,  # Adjust the gap between bars (lower values = wider bars)
    barmode='group',  # Ensures that the bars are grouped together
    yaxis=dict(showgrid=False, zeroline=False, showline=False, showticklabels=False),  # Hide y-axis
    xaxis=dict(tickangle=-45),  # Tilt x-axis labels for better visibility
)
    st.plotly_chart(fig)
else:
    st.write("لايوجد بيانات")
