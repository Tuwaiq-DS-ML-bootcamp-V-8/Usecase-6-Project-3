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
from matplotlib import rcParams

# Load the data files
expensive_hoods = pd.read_csv('./expensive_hoods.csv')
land_count_by_hood_df = pd.read_csv('./land_count_by_hood.csv')
riyadh_aqqar_df = pd.read_csv('./riyadh_aqqar_df.csv')
neighborhood_purpose_counts = pd.read_csv('./neighborhood_purpose_counts.csv')

# Set up Arabic font in Matplotlib
rcParams['font.sans-serif'] = ['Arial']  # Replace with an Arabic-compatible font available on your system
rcParams['axes.unicode_minus'] = False

# Function to reshape Arabic text for Matplotlib
def reshape_arabic(text):
    return get_display(arabic_reshaper.reshape(text))

# Set the page layout to wide and configure right-to-left text alignment
st.set_page_config(layout="wide")
st.markdown("<style>body {direction: rtl; text-align: right;}</style>", unsafe_allow_html=True)

# Introduction: Setting up the Story
st.title("راكان يبي يفتح محمصة جديدة في الرياض!")
st.write("""
راكان عنده محمصة قهوة في الخبر، وجا بباله يتوسع ويفتح فرع بالرياض. بحكم إنها العاصمة وفيها ناس واجد وكل يوم تزيد زحمتها. بس المشكلة إنه توهق، ما عنده علم بأسعار العقار بالرياض، ولا يدري وش الأحياء الزينة اللي تصلح للقهاوي.

قام يتصل على خويه سعود، اللي له سنين ساكن بالرياض ودايم يشتغل على البيانات والتحليل. قال له سعود: "أبد يا راكان، لا تشيل هم. هات اللي عندك وخله عليّ". وبالفعل، سعود طلع قدها. أخذ بيانات من موقع عقار، وسوا عليها شغل مضبوط، وطلع ٤ نقاط رئيسية تقدر تجاوب على أسئلة راكان وتساعده يختار المكان الأنسب لمشروعه الجديد.
""")

# Apply reshaping to Arabic columns for better display in plots
expensive_hoods['الحي'] = expensive_hoods['الحي'].apply(reshape_arabic)
land_count_by_hood_df['الحي'] = land_count_by_hood_df['الحي'].apply(reshape_arabic)
riyadh_aqqar_df['الحي'] = riyadh_aqqar_df['الحي'].apply(reshape_arabic)
neighborhood_purpose_counts['الحي'] = neighborhood_purpose_counts['الحي'].apply(reshape_arabic)
neighborhood_purpose_counts['الغرض'] = neighborhood_purpose_counts['الغرض'].apply(reshape_arabic)

# Section 1: Premium Neighborhoods
st.header("١. أحياء الهبة وأسعار الأراضي")
st.write("""
أول شي حب سعود يوضح لراكان وين الأحياء اللي أسعارها غالية، وقال له: "هذي المناطق تناسب القهاوي الفخمة اللي تبغى تستهدف راعين القهوة. أسعار الأراضي تختلف من حي لحي، حسب الموقع والبنية التحتية والطلب.
""")

# Plot for high land prices
fig, ax = plt.subplots(figsize=(15, 6))
sns.barplot(data=expensive_hoods, x='الحي', y='سعر المتر', ax=ax)
plt.xticks(rotation=90, fontsize=10, ha='center')
plt.title(reshape_arabic('سعر المتر المربع حسب الحي'), fontweight='bold')
plt.ylabel(reshape_arabic('سعر المتر (ريال)'), fontweight='bold')
st.pyplot(fig)

# Section 2: Land Availability by Neighborhood
st.header("٢. توافر الأراضي حسب الحي")
st.write("""
سعود بعدين راح يشوف عدد الأراضي المتاحة لكل حي. قال لراكان: "إذا كنت تبي خيارات أكثر وتفاوض بالسعر، ركّز على الأحياء اللي فيها أراضي واجد زي النفل والياسمين."
""")

# Plot for land availability
fig, ax = plt.subplots(figsize=(20, 8))
sns.barplot(data=land_count_by_hood_df, x='الحي', y='عدد الأراضي', ax=ax)
plt.xticks(rotation=90, fontsize=10, ha='center')
plt.title(reshape_arabic('عدد الأراضي المتاحة للبيع حسب الحي'), fontweight='bold')
plt.ylabel(reshape_arabic('عدد الأراضي'), fontweight='bold')
st.pyplot(fig)

# Section 3: Relationship Between Land Price and Size
st.header("٣. العلاقة بين سعر المتر والمساحة")
st.write("""
سعود لاحظ بعد إن في بعض الأحياء، كل ما كبرت الأرض قل سعر المتر، وشرح لراكان إن هذي بتكون ميزة لو يبي محل قهوة بمساحة كبيرة توفر جلسات خارجية أو مناطق اجتماعية.
""")

# Scatter plot for price per sqm vs. size
fig, ax = plt.subplots(figsize=(15, 6))
sns.scatterplot(data=riyadh_aqqar_df, x='المساحة', y='سعر المتر', hue='الحي', ax=ax)
plt.title(reshape_arabic('سعر المتر المربع مقابل المساحة حسب الحي'), fontweight='bold')
plt.xlabel(reshape_arabic('المساحة (متر مربع)'), fontweight='bold')
plt.ylabel(reshape_arabic('سعر المتر (ريال)'), fontweight='bold')
plt.legend(title=reshape_arabic('الحي'), loc='upper right', bbox_to_anchor=(1.15, 1))
st.pyplot(fig)

# Section 4: Land Purpose Distribution
st.header("٤. توزيع الأراضي حسب الغرض في كل حي")
st.write("""
أخيراً، وضح سعود لراكان إن بعض الأحياء تكون أغلب أراضيها تجارية، زي العليا، وهذي تناسب المشاريع التجارية اللي تستهدف موظفين المكاتب. أما الأحياء اللي فيها أراضي متعددة الاستخدام، زي الياسمين، فتعطي مرونة للمقاهي اللي تبغى تخدم سكنيين وتجاريين.
""")

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
st.write("""
بهذا التحليل، صار عند راكان صورة أوضح عن الأحياء في الرياض، وايش الأماكن اللي تناسب مشروع القهوة الجديد. الحين يقدر يختار المكان بكل ثقة، ويوسع محمصته من الخبر إلى الرياض.
""")