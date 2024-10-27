import streamlit as st
import pandas as pd
import plotly.express as px

# Setting up Arabic fonts and styling
st.markdown(
    """
    <style>
    body {
        font-family: 'Arial'; 
        font-size: 20px; 
        color: black;
        direction: rtl;
        text-align: right; 
        background-color: #f0f2f6;
        background-image: url("Tuwaiq_mounten.png");
    }
    p, h2, h3 {
        font-size: 20px;
        color: #333;
    }
    h1 {
        text-align: center;
        color: #4830af;
    }
    </style>
    """, 
    unsafe_allow_html=True
)

# Load Data
df = pd.read_csv("df_tuwaiq.csv")
df1 = df["district"].value_counts()

# Logo and title
st.image("logo-h.png")
st.title("ألف مبروك! 🎉 انقبلت بطويق!")
st.markdown("<hr>",unsafe_allow_html=True)
# Introduction message
st.markdown("أكيد فرحتك ما توصف، ومتحمس لبداية رحلة جديدة مليانة معرفة وتحدي! ولو كنت من خارج الرياض أكيد شلت هم السكن. لا تشيل هم! إحنا هنا عشان نسهّل عليك ونساعدك تختار الحي اللي يناسبك والقريب من أكاديمية طويق.")

# Display bar chart for nearby districts
st.markdown("#### أقرب الأحياء للأكاديمية وأحلى الخيارات 🏘️")
fig = px.bar(df1, x=df1.index, y=df1.values, width=1000, height=700, title="عدد الشقق لأقرب 10 أحياء للأكاديمية طويق",  color_discrete_sequence=["#4830af"])
fig.update_layout(title={'x': 0.53, 'xanchor': 'center'}, xaxis_title="الأحياء", yaxis_title="عدد الشقق")
st.plotly_chart(fig)

# Selection for specific district
st.markdown("<hr>",unsafe_allow_html=True)
st.markdown("""
لو محتار في أي حي تبي تسكن، مر تحت واختار الحي اللي لفت نظرك، 
وبيطلع لك تفصيل عن أسعار الشقق في الحي هذا عشان تكون على علم قبل تختار.
""")
st.markdown("#### اختار الحي اللي ودك فيه 🔍")
options = st.selectbox("أختر الحي اللي لفت نظرك", df1.index)
filtered_data = df[df['district'] == options]

# Display price distribution for selected district
st.markdown("""
بعد ما تختار الحي، بنطلع لك رسم بياني يوضح توزيع الأسعار فيه، عشان تعرف حدود الميزانية وتقرر اللي يناسبك.
""")
st.markdown("<hr>",unsafe_allow_html=True)
st.markdown("#### الأسعار كيف شكلها؟ 💸")
fig1 = px.histogram(filtered_data["price"], title="توزيع الأسعار في الحي",color_discrete_sequence=["#4830af"])
fig1.update_layout(title={'x': 0.53, 'xanchor': 'center'}, xaxis_title="الأسعار", yaxis_title="عدد الشقق")
st.plotly_chart(fig1)
st.markdown("<hr>",unsafe_allow_html=True)

# Additional message for important details
st.markdown("""
وهنا جمعنا لك ثلاث معلومات مهمة لازم تنتبه لها في كل شقة:
هل هي مؤثثة؟ فيها مكيف؟ والمطبخ موجود ولا؟ 
_يعني الأشياء اللي بتسهل حياتك كمقيم مؤقت في الرياض!_
""")

# Display pie charts for furnished, AC, and kitchen options
st.markdown("#### أشياء لا تنساها 👀")

furnished = filtered_data["furnished"].value_counts()
fig3 = px.pie(furnished, values=furnished.values, names=furnished.index, title='هل هي مؤثثة؟',color_discrete_sequence=["#CDC1FF", "#4830af"])
fig3.update_traces(labels=("لا", "نعم"))
fig3.update_layout(title={'x': 0.36, 'xanchor': 'center'})

ac = filtered_data["ac"].value_counts()
fig4 = px.pie(ac, values=ac.values, names=ac.index, title='هل هي مكيفة؟',color_discrete_sequence=["#4830af", "#CDC1FF"])
fig4.update_traces(labels=("نعم", "لا"))
fig4.update_layout(title={'x': 0.36, 'xanchor': 'center'})

kitchen = filtered_data["ketchen"].value_counts()
fig5 = px.pie(kitchen, values=kitchen.values, names=kitchen.index, title='هل يوجد مطبخ؟',color_discrete_sequence=["#4830af", "#CDC1FF"])
fig5.update_traces(labels=("نعم", "لا"))
fig5.update_layout(title={'x': 0.36, 'xanchor': 'center'})

col1, col2, col3 = st.columns(3)
with col1:
    st.plotly_chart(fig3, use_container_width=True)
with col2:
    st.plotly_chart(fig4, use_container_width=True)
with col3:
    st.plotly_chart(fig5, use_container_width=True)

# Display number of rooms
st.markdown("<hr>",unsafe_allow_html=True)
st.markdown("#### عدد الغرف 🛏️")
st.markdown("وأخيرًا، بنعطيك فكرة عن عدد الغرف المتاحة في الحي اللي اخترته، عشان تحدد المساحة اللي تحتاجها.")
beds = filtered_data["beds"].value_counts()
fig6 = px.bar(beds, x=beds.index, y=beds.values, title="عدد الغرف",color_discrete_sequence=["#4830af"])
fig6.update_layout(title={'x': 0.53, 'xanchor': 'center'}, xaxis_title="الغرف", yaxis_title="عدد الشقق")
st.plotly_chart(fig6)

# Closing message
st.markdown("بكل هالمعلومات والتفاصيل، تقدر تحصل على صورة شاملة عن السكن المتاح حوالين أكاديمية طويق. تذكر أن الخيارات كثيره، فخذ وقتك واستمتع بتجربة البحث واختيار المكان اللي يناسبك ويعكس احتياجاتك. إن شاء الله تلقى الشقة المثالية وتبدأ رحلتك الجديدة بنجاح وراحة بال!")