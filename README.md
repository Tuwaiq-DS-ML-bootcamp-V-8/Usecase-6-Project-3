# Usecase-6-Project-3
# Apartment Data Analysis Project in Riyadh



## Team Members:
- *Mohammed Abdullah*
- *Arwa Al-Khathlan*
- *Abdullah Al-Haqbani*
- *Faris Alhamdan*
## Stream Link:
https://usecase-6-project-3-jgd47k3gndt5qejdqtzsmr.streamlit.app/


  ## Introduction:
  Saudi Arabia’s Vision 2030 aims to increase the population of Riyadh to ten million people. This makes the city an attractive place for job seekers and tourists, increasing the demand for apartments for sale or rent. This project aims to analyze apartment data in Riyadh to provide insights into their density and prices, helping to understand the housing market and guide investment and housing decisions.

  ## Dataset Overview
### 1. *Data Source*  
   The data comes from *Aqar*, a platform that collects information about available properties in Saudi Arabia.

### 2. *Data Fields*  
   The data includes the following columns:

   - *price*: The price of the apartment.
   - *beds*: The number of bedrooms in the apartment.
   - *livings*: The number of living rooms.
   - *wc*: The number of bathrooms.
   - *area*: The size of the apartment in square meters.
   - *street_width*: The width of the street where the apartment is located.
   - *age*: The age of the apartment or building.
   - *kitchen*: Indicates if the apartment has a kitchen (yes/no).
   - *ac*: Indicates if there is air conditioning in the apartment (yes/no).
   - *furnished*: Indicates if the apartment is furnished (yes/no).
   - *district*: The neighborhood where the apartment is located in Riyadh.
   - *advertiser_type*: The type of advertiser, either an individual or a company.
   - *review*: The available ratings or reviews for the apartment.
   - *onMarket*: The number of days the apartment has been listed on the market.
   - *isRent*: Indicates if the apartment is for rent or sale.

### 3. *Data Usage*
   The data will be used to analyze the following aspects:

   - *Average price per district*: Calculate the average price of apartments in each district of Riyadh to show price differences by area.
   - *Apartment density in each district*: Identify neighborhoods with the highest number of apartments.
   - *Factors affecting prices*: Analyze various factors that may influence apartment prices, such as size, street width, apartment age, and availability of features like kitchens, air conditioning, and furniture.

## EDA Steps Applied

1. *Data Exploration*:
   - Checked the shape of the dataset to see the number of rows and columns.
   - Displayed the first few rows of the data to get an overview.

2. *Data Cleaning*:
   - Removed duplicates to ensure unique representation of each apartment.
   - Handled missing values by filling or removing them.
   - Converted data types to ensure accurate analysis.

3. *Data Visualization*:
   - Created a *Bar* chart to display the ratings of ten different neighborhoods.
   - Used a *Heatmap* to analyze the factors affecting price.
   - Used a *Boxplot* to calculate the average apartment prices for each neighborhood, helping to identify variance and outliers.
   - Created a Barplot to calculate the density of apartments for each neighborhood.

