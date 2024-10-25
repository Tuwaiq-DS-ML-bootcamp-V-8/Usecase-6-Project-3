

import streamlit as st
import pandas as pd
import plotly.express as px

# Load the dataset
df = pd.read_csv('FilteredRiyadhVillasAqar.csv')

# Streamlit app title
st.title("اختلاف اسعار الفلل بأختلاف العوامل")

st.write("""
كلنا نعرف ان سعر الفله او البيت تختلف بأختلاف عوامل كثيرة مثل المنطقة ومساحة الارض وعوامل اخرى مثل 
عمر المبنى
وجود حديقة خارجية 
وجود مسبح 
الا اخره ....

         
لكن هل فكرت بالعوامل الاخرى مثل عرض الشارع المقابل         
اتجاه الواجه الامامية 
وكيف راح تأثر على السعر اذا ماقارنا اراضي بنفس المساحة وبنفس المنطقة لكن الشارع المقابل واتجاه الواجهة الامامية يختلف""")



# Step 1: Filter by Location
st.header("حدد اي منطقة في الرياض")
selected_location = st.selectbox('منطقة', df['location'].unique())

st.write("اولا, حدد المنطقة في الرياض اللي على اساسها الرسم يظهر اختلاف الاسعار بتغير عامل اتجاه المبنى عرض الشارع")


filtered_df = df[df['location'] == selected_location]

# Display an animated bar chart showing the relationship between location and price
if not filtered_df.empty:
    st.subheader(f"اختلاف الاسعار في منطقة {selected_location}")
    fig = px.bar(filtered_df, x='front', y='price', animation_frame='streetWidth', animation_group='front', 
                 title=f'اختلاف الاسعار بتغير عاملين اتجاه المبنى و عرض الشارع {selected_location}',
                 labels={'price': 'Price (SAR)', 'front': 'Property Front', 'streetWidth': 'width of street'})
    fig.update_layout(
    width=800,  # Set the width in pixels
    height=800  # Set the height in pixels
    )
    st.plotly_chart(fig)
else:
    st.write("لايوجد بيانات")
