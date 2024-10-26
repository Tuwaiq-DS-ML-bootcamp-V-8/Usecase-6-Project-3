import streamlit as st
import pandas as pd
import plotly.express as px

# Load the dataset
df = pd.read_csv('FilteredRiyadhVillasAqar.csv')

# Apply custom CSS for specific elements
st.markdown("""
    <style>
    @import url('https://fonts.googleapis.com/css2?family=Amiri:wght@400;700&family=Cairo:wght@400;700&display=swap');
    body {
        font-family: 'Amiri', serif;  /* Set Arabic-friendly font */
    }
    h1, h2 {
        font-family: 'Cairo', sans-serif;
        color: #FF6347;
    }
    p {
        font-size: 18px;
        color: #333333;
    }
    </style>
    """, unsafe_allow_html=True)

# Page Title
st.title("اختلاف اسعار الفلل بأختلاف العوامل")

# Improved layout and text
st.write("""
    مرحبا
    أن كلنا نعرف أن اسعار الفلل تختلف بأختلاف عوامل كثيرة مثل المنطقة ، عمر المبنى، مساحة الفله وما إلى ذلك.
    بعد تحليل عميق في إحدى البيانات الخاصة ببيع الفلل من موقع في مدينة الرياض، حبينا نسوي مقارنة مختلفه شوي وهي العلاقة بين سعر الفله وتأثير اتجاه واجهة الفله و موقعها على السعر.
""")

# Add an image for better visual appeal
st.image("image2.png", caption="Real Estate Data", use_column_width=True)

# Step 1: Filter by Location
selected_location = st.selectbox('حدد المنطقة', df['location'].unique())

st.write("راح تشوف بالاسفل رسم تفاعلي يتغير كلما غيرت بقيم مساحة الارض.")
st.write("غير قيم المساحة من خلال الشريط اسفل الرسم وشوف كيف يتغير السعر لكل فئة من فئات اتجاه الواجهة")

# Filter DataFrame based on selection
filtered_df = df[df['location'] == selected_location]

# Display the bar chart if data is available
if not filtered_df.empty:
    st.subheader(f"اختلاف الاسعار في منطقة {selected_location}")
    
    fig = px.bar(filtered_df, x='front', y='price', animation_frame='space', animation_group='front',
                 title=f'اختلاف الاسعار بتغير عاملين واجهة الفه و مساحتها {selected_location}',
                 labels={'price': 'Price (SAR)', 'front': 'واجهة الفله', 'space': 'مساحة الفله'},
                 text='price')
    
    fig.update_traces(texttemplate='%{y:.2f}', textposition='outside')
    
    fig.update_layout(
        width=800,
        height=600,
        font=dict(
            family="Cairo, sans-serif",
            size=16,
            color="black"
        ),
        title=dict(
            text=f'اختلاف الاسعار بتغير عاملين واجهة الفه و مساحتها {selected_location}',
            font=dict(size=24, family="Cairo, sans-serif", color="#FF6347")
        ),
        bargap=0.1,
        barmode='group',
        yaxis=dict(showgrid=False, zeroline=False, showline=False, showticklabels=False),
        xaxis=dict(tickangle=-45)
    )
    
    st.plotly_chart(fig)
else:
    st.write("لايوجد بيانات")

# Final message with proper formatting
st.markdown("""
    <h1 style='color: black; font-size: 26px; text-align: center'>           
    بالنهاية
    هذه المقارنة قد تكون بسيطة لكن تظهر أن واجهة المبنى (الفله في تحليلنا) قد تأثر على سعر المبنى اذا ماقارنا فلل بنفس المساحة ونفس المنطقة لكن اتجاه الواجهة يختلف.
    </h1>
""", unsafe_allow_html=True)
