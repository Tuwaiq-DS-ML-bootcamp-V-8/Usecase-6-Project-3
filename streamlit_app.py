import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import streamlit as st
from matplotlib import rcParams
from bidi.algorithm import get_display
import arabic_reshaper
import plotly.express as px
from PIL import Image  # Import Image from Pillow

# Set the page layout to wide
st.set_page_config(layout="wide")

# Custom CSS for larger text, spacing, and rounded rectangle boxes
st.markdown("""
    <style>
        body {direction: rtl; text-align: right;}
        .title-box, .section-box {
            background-color: #f9f9f9;
            border-radius: 10px;
            padding: 20px;
            margin-bottom: 20px;
            box-shadow: 0px 4px 12px rgba(0, 0, 0, 0.1);
        }
        .title {
            font-size: 28px;
            font-weight: bold;
            color: #333333;
            margin-bottom: 10px;
        }
        .header {
            font-size: 24px;
            font-weight: bold;
            color: #333333;
            margin-top: 10px;
            margin-bottom: 15px;
        }
        .text {
            font-size: 18px;
            color: #555555;
            line-height: 1.6;
            margin-top: 5px;
            margin-bottom: 5px;
        }
    </style>
""", unsafe_allow_html=True)

# Set up Arabic font in Matplotlib
rcParams['font.sans-serif'] = ['Arial']
rcParams['axes.unicode_minus'] = False

# Function to reshape Arabic text for Matplotlib
def reshape_arabic(text):
    return get_display(arabic_reshaper.reshape(text))

# Introduction with enhanced readability
st.markdown('<div class="title-box"><div class="title">راكان يبي يفتح محمصة جديدة في الرياض!</div>', unsafe_allow_html=True)
st.markdown("""
<div class="text">
راكان عنده محمصة قهوة في الخبر، وجا بباله يتوسع ويفتح فرع بالرياض. بحكم إنها العاصمة وفيها ناس واجد وكل يوم تزيد زحمتها. بس المشكلة إنه توهق، ما عنده علم بأسعار العقار بالرياض، ولا يدري وش الأحياء الزينة اللي تصلح للقهاوي.
<br><br>
قام يتصل على خويه سعود، اللي له سنين ساكن بالرياض ودايم يشتغل على البيانات والتحليل. قال له سعود: "أبد يا راكان، لا تشيل هم. هات اللي عندك وخله عليّ". وبالفعل، سعود طلع قدها. أخذ بيانات من موقع عقار، وسوا عليها شغل مضبوط، وطلع ٤ نقاط رئيسية تقدر تجاوب على أسئلة راكان وتساعده يختار المكان الأنسب لمشروعه الجديد.
</div>
</div>
""", unsafe_allow_html=True)

# Load the data files
expensive_hoods = pd.read_csv('./expensive_hoods.csv')
land_count_by_hood_df = pd.read_csv('./land_count_by_hood.csv')
riyadh_aqqar_df = pd.read_csv('./riyadh_aqqar_df.csv')
neighborhood_purpose_counts = pd.read_csv('./neighborhood_purpose_counts.csv')

# Apply reshaping to Arabic columns for better display in plots
expensive_hoods['الحي'] = expensive_hoods['الحي'].apply(reshape_arabic)
land_count_by_hood_df['الحي'] = land_count_by_hood_df['الحي'].apply(reshape_arabic)
riyadh_aqqar_df['الحي'] = riyadh_aqqar_df['الحي'].apply(reshape_arabic)
neighborhood_purpose_counts['الحي'] = neighborhood_purpose_counts['الحي'].apply(reshape_arabic)
neighborhood_purpose_counts['الغرض'] = neighborhood_purpose_counts['الغرض'].apply(reshape_arabic)

# Section 1: Premium Neighborhoods
st.markdown('<div class="section-box"><div class="header">١. الأحياء الفاخرة وأسعار الأراضي</div>', unsafe_allow_html=True)
st.markdown("""
<div class="text">
أول شي حب سعود يوضح لراكان وين الأحياء اللي أسعارها غالية، وقال له: "هذي المناطق تناسب القهاوي الفخمة اللي تبغى تستهدف راعين القهوة". أسعار الأراضي تختلف من حي لحي، حسب الموقع والبنية التحتية والطلب.
</div>
</div>
""", unsafe_allow_html=True)

image_q1 = Image.open("./images/q1.png")
st.image(image_q1, use_column_width=True)

# Section 2: Land Availability by Neighborhood
st.markdown('<div class="section-box"><div class="header">٢. توافر الأراضي حسب الحي</div>', unsafe_allow_html=True)
st.markdown("""
<div class="text">
سعود بعدين راح يشوف عدد الأراضي المتاحة لكل حي. قال لراكان: "إذا كنت تبي خيارات أكثر وتفاوض بالسعر، ركّز على الأحياء اللي فيها أراضي واجد زي المهدية والنرجس."
</div>
</div>
""", unsafe_allow_html=True)

# Plot for land availability
image_q1 = Image.open("./images/q2.png")
st.image(image_q1, use_column_width=True)

# Section 3: Relationship Between Land Price and Size
st.markdown('<div class="section-box"><div class="header">٣. العلاقة بين سعر المتر والمساحة</div>', unsafe_allow_html=True)
st.markdown("""
<div class="text">
سعود لاحظ بعد إن في بعض الأحياء، كل ما كبرت الأرض قل سعر المتر، وشرح لراكان إن هذي بتكون ميزة لو يبي محل قهوة بمساحة كبيرة توفر جلسات خارجية أو مناطق اجتماعية.
</div>
</div>
""", unsafe_allow_html=True)


# Plot for land availability
image_q3 = Image.open("./images/q3.png")
st.image(image_q3, use_column_width=True)

# Section 4: Land Purpose Distribution
st.markdown('<div class="section-box"><div class="header">٤. توزيع الأراضي حسب الغرض في كل حي</div>', unsafe_allow_html=True)
st.markdown("""
<div class="text">
أخيراً، وضح سعود لراكان إن بعض الأحياء تكون أغلب أراضيها تجارية، زي النرجس، وهذي تناسب المشاريع التجارية اللي تستهدف موظفين المكاتب. أما الأحياء اللي فيها أراضي متعددة الاستخدام، زي الرمال، فتعطي مرونة للمقاهي اللي تبغى تخدم سكنيين وتجاريين.
</div>
</div>
""", unsafe_allow_html=True)

# Stacked bar chart for land purpose by neighborhood
purpose_counts_pivot = neighborhood_purpose_counts.pivot(index="الحي", columns="الغرض", values="عدد العقارات")
fig, ax = plt.subplots(figsize=(20, 8))
purpose_counts_pivot.plot(kind='bar', stacked=True, ax=ax)
plt.title(reshape_arabic('توزيع الأراضي حسب الغرض في كل حي'), fontweight='bold')
plt.xlabel(reshape_arabic('الحي'), fontweight='bold')
plt.ylabel(reshape_arabic('عدد العقارات'), fontweight='bold')
plt.legend(title=reshape_arabic('الغرض'), bbox_to_anchor=(1.05, 1), loc='upper left')
st.pyplot(fig)

# Conclusion
st.markdown("""
<div class="section-box">
    <div class="text">
        بهذا التحليل، صار عند راكان صورة أوضح عن الأحياء في الرياض، وايش الأماكن اللي تناسب مشروع القهوة الجديد. 
        الحين يقدر يختار المكان بكل ثقة، ويوسع محمصته من الخبر إلى الرياض.
    </div>
</div>
""", unsafe_allow_html=True)
