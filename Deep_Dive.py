

import streamlit as st
import pandas as pd
import plotly.express as px

# Load the dataset
df = pd.read_csv('FilteredRiyadhVillasAqar.csv')



# Example of embedding HTML
st.markdown("""
    <h1 style='text-align: center; color: blue;'>اختلاف اسعار الفلل بأختلاف العوامل</h1>
    <h1>
            مرحبا
            
أن كلنا نعرف أن اسعار الفلل تختلف بأختلاف عوامل كثيرة مثل المنطقة ، عمر المبنى، مساحة الفله وما إلى ذلك.

      بعد تحليل عميق في إحدى البيانات الخاصة ببيع الفلل من موقع  في مدينة الرياض، حبينا نسوي مقارنة مختلفه شوي وهي العلاقة بين سعر الفله وتأثير اتجاه واجهة الفله و موقعها على السعر.      
    </h1>
    <hr>
    <h2 style='color: black;'>اولاً: خلونا نبدأ نحدد المنطقة بالرياض بالضبط."</h2>
    """, unsafe_allow_html=True)



# Step 1: Filter by Location
#st.header("اولا: حدد اي منطقة في الرياض")
selected_location = st.selectbox('حدد المنطقة', df['location'].unique())
# Step 2: Sidebar for space (sorted in ascending order)
#sorted_space = sorted(df['space'].unique())  # Sort the space values in ascending order
#selected_space = st.selectbox('حدد مساحة الفله', sorted_space)

st.write("راح تشوف بالاسفل رسم تفاعلي يتغير كلما غيرت بقيم مساحة الارض.")

st.write("غير قيم المساحة من خلال الشريط اسفل الرسم وشوف كيف يتغير السعر لكل فئة من فئات اتجاه الواجهة")


filtered_df = df[ (df['location'] == selected_location)]

# Display an animated bar chart
if not filtered_df.empty:
    st.subheader(f"اختلاف الاسعار في منطقة {selected_location}")
    fig = px.bar(filtered_df, x='front', y='price', animation_frame='space', animation_group='front', 
                 title=f'اختلاف الاسعار بتغير عاملين واجهة الفه و مساحتها {selected_location}',
                 labels={'price': '', 'front': 'واجهة الفله', 'space': 'مساحة الفله'},
                 text='price'  # Add price labels on top of the bars
                 )
    
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

st.markdown("""
بالنهاية...
هذه المقارنة قد تكون بسيطة لكن تظهر أن واجهة المبنى (الفله في تحليلنا) قد تأثر على سعر المبنى اذا ماقارنا فلل بنفس المساحة ونفس المنطقة لكن اتجاه الواجهة يختلف.

اتجاه الواجهة له اهمية اذا ما تم اختياره بالاتجاه المناسب بناء على موقع المبنى في المدينة.

في تحليلنا، استخدمنا اشهر موقع لبيع العقارات وحصرنا المقارنة على جميع الفلل المعروضة في الموقع.")
""", unsafe_allow_html=True)