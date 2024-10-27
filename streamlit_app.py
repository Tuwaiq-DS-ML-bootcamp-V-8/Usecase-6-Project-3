import streamlit as st
from PIL import Image
import pandas as pd 
import plotly.express as px
import plotly.graph_objects as pg
import requests
from streamlit_lottie import st_lottie

# load dataframe (villa)
villa = pd.read_csv("Cleaning.csv")
villa.drop(columns='Unnamed: 0', inplace=True)
vill_with_apart = villa[villa['apartments'] <= 5]
vill_with_apart = vill_with_apart[vill_with_apart['price'] <= 6000000]

# load dataframe(real estate)
apdf = pd.read_csv("data/apartments in Riyadh Saudi Arabia/realEstate_cleaned.csv")
apdf.drop(columns="Unnamed: 0",inplace=True)


# Load the image
image = Image.open('avg_lands.png')
# Load the image
image2 = Image.open('with_aparts.png')
# Load the image
image3 = Image.open('imgg.png')
image4 = Image.open('riyadhh.png')

# Load animation image(1)

# --  asset url: https://lottie.host/04339cb6-0438-4aa6-a4e7-c37a49e040dc/VCfxjdvdmg.json
def load_lot(url):
    r= requests.get(url)
    if r.status_code !=200:
        return None
    return r.json()
 
lot_cod1 = load_lot("https://lottie.host/04339cb6-0438-4aa6-a4e7-c37a49e040dc/VCfxjdvdmg.json")   

# Load animation image(2)

# --  asset url: https://lottie.host/96099f2a-5cda-4f0d-82df-e8ad2fb2fcda/aKOav2Rv6Y.json

def load_lot2(url):
    r= requests.get(url)
    if r.status_code !=200:
        return None
    return r.json()
     
lot_cod2 = load_lot2("https://lottie.host/96099f2a-5cda-4f0d-82df-e8ad2fb2fcda/aKOav2Rv6Y.json")    





# Center the title using Markdown
st.markdown("<h1 style='text-align: center;'>بين الحلم و اللإستثمار </h1>", unsafe_allow_html=True)
# Center the image using Streamlit's layout

# Center the image using Streamlit's layout
col1, col2, col3 = st.columns([1,4, 1])  # Create three columns

with col1:
    st.write("")  # Empty space in the first column

with col2:
    st_lottie(lot_cod1,height=300,key='coding')
    
    #st.image(image4, width=400)  # Center the image in the second column

with col3:
    st.write("")  # Empty space in the third column


st.markdown("<h5 style='text-align: center;'> أبو خالد رجلاً طموحاً، يعيش حياة مليئة بالتحديات والتطلعات الكبيرة. لديه ثلاثة أطفال ، وكان دائماً يطمح لتوفير أفضل حياة لهم. في أحد الأيام، جاءه قرار مفاجئ؛ الانتقال إلى مدينة الرياض، المدينة الكبيرة التي تحفل بالفرص. لم يكن الانتقال سهلاً، لكنه كان يرى في الرياض بوابة لمستقبل مشرق له ولعائلته .</h5>", unsafe_allow_html=True)


# Center the image using Streamlit's layout
col1, col2, col3 = st.columns([1,13, 1])  # Create three columns

with col1:
    st.write("")  # Empty space in the first column

with col2:
    st.image(image, width=650)  # Center the image in the second column

with col3:
    st.write("")  # Empty space in the third column

st.markdown("<h5 style='text-align: center;'>بعد وصوله إلى الرياض، بدأ أبو خالد يفكر في حلمه القديم: بناء فيلته الخاصة. كان يحلم بمساحة خضراء واسعة تحيط بها، وغرف لكل أطفاله الثلاثة، في مكان استراتيجي يسهل عليه الوصول إلى عمله وكل احتياجاته. لكن حين بدأ البحث عن الأراضي في وسط الرياض، صُدم بالأسعار! كانت تكاليف الأراضي مرتفعة جداً، ولم تكن مجرد شراء الأرض هو ما يقلقه؛ بل تكاليف البناء الإضافية التي ستتبعها. هذا الأمر دفعه لإعادة التفكير في خطته.</h5>", unsafe_allow_html=True)
# Center the image using Streamlit's layout
col1, col2, col3 = st.columns([1,13, 1])  # Create three columns

with col1:
    st.write("")  # Empty space in the first column
# creat bar chart
top_5_locations = vill_with_apart.groupby('location')['price'].mean().nlargest(5).reset_index()

# Plotting with Plotly
fig1 = px.bar(top_5_locations, 
             x='location', 
             y='price', 
             color='price', 
             color_continuous_scale='Reds',
             title='متوسط سعر الفلل في الرياض(فلل مع شقق)',
             labels={'price': 'Average Price', 'location': 'Location'},
             text='price')

# Show the plot
fig1.update_traces(texttemplate='%{text:.2f}', textposition='outside')
fig1.update_layout(xaxis=dict(title='Location'), 
                  yaxis=dict(title='Average Price with apart'),
                  showlegend=False)

with col2:
    st.plotly_chart(fig1)
    #st.image(image2, width=650)  # Center the image in the second column

with col3:
    st.write("")  # Empty space in the third column
    
st.markdown("<h5 style='text-align: center;'> بعد تفكير طويل، قرر أن يستبعد فكرة شراء الأرض والبناء بنفسه. وبدلاً من ذلك، بدأ يفكر في شراء فيلا جاهزة. بحث كثيراً، قرر ان تكون الفلة في شرق الرياض، لقربها من عمله و مناسبه لميزانيته</h5>", unsafe_allow_html=True)
col1, col2, col3 = st.columns([1,13, 1])  # Create three columns

with col1:
    st.write("")  # Empty space in the first column


# Group by district and calculate the average price
district_price = apdf.groupby('district')['price'].mean().reset_index()
district_price = district_price.sort_values(by='price', ascending=False)
# create bar chart for Distribution of Property Prices
fig2 = px.bar(district_price, 
             x='district', 
             y='price', 
             title='Average Property Price by District',
             labels={'price': 'Average Price', 'district': 'District'},
             color='price', 
             color_continuous_scale='Viridis')

# Show the plot
fig2.update_layout(xaxis_title='District', yaxis_title='Average Price', xaxis_tickangle=-45)

with col2:
    st.plotly_chart(fig2)
    #st.image(image3, width=650)  # Center the image in the second column

with col3:
    st.write("")  # Empty space in the third column
st.markdown("<h5 style='text-align: center;'>في خضم البحث، لفت انتباهه شيء آخر. وجد أن بعض الفلل المعروضة للبيع تحتوي على شقق للإيجار، وأن أسعار الإيجارات في شرق الرياض كانت مشجعة جداً. فقد بلغ متوسط الإيجار لتلك الشقق حوالي 52,000 ريال سنوياً. هذه الفكرة كانت مغرية لأبو خالد؛ فمن خلال شراء فيلا جاهزة تحتوي على شقة للإيجار، يمكنه أن يؤمن مصدر دخل إضافي يغطي جزءاً من تكاليف الشراء. </h5>", unsafe_allow_html=True)
st_lottie(lot_cod2,height=300,key='o')

st.markdown("<h5 style='text-align: center;'>وبالفعل، بعد دراسة متأنية وتفكير عميق، قرر أبو خالد أن يسكن في إحدى تلك الفلل. ليس فقط لأنه وجد ما يناسب عائلته، بل لأنه أيضاً وجد فرصة استثمارية ممتازة. استقر في الفلة الجديدة، واستأجر الشقة، وبدأ يشعر بأن حلمه يتحقق بطريقة لم يكن يتوقعها. وهكذا، تمكن أبو خالد من تأمين سكن لعائلته والاستثمار في نفس الوقت، مما جعله يشعر بالرضا والطمأنينة تجاه مستقبله ومستقبل أطفاله.بين الحلم والاستثمار </h5>", unsafe_allow_html=True)


