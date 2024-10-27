# Aqar Analysis

**Team Members**: Faisal Alkulaib, Ghadah Alsulami, Muhannad Alahmadi, Ghada Mohammed, Sara Altamimi

## Introduction (Problem, Objectives)
This project aims to analyze and understand the distribution and pricing trends of residential and commercial land across neighborhoods in Riyadh. By examining key factors such as location, purpose (residential or commercial), and average price per square meter, the goal is to identify the neighborhoods with the highest land demand and the characteristics influencing land value. This analysis will provide valuable insights for investors, urban planners, and policymakers in the real estate market.

## Dataset Overview and Source
We utilized one dataset for this analysis:
- **Riyadh Aqaar Dataset**: This dataset includes land listings in Riyadh, detailing neighborhood locations, land count, pricing, purpose (residential/commercial), and area measurements.

## List of EDA Steps
The following Exploratory Data Analysis (EDA) steps were applied:
1. **Data Loading and Overview:**: Load the dataset and view the first few rows to understand its structure..
2. **Missing Values Check:**: Identify columns with missing values and determine an appropriate handling strategy.
3. **Summary Statistics:**: Generate summary statistics (mean, median, etc.) for numerical features and value counts for categorical features.
4. **Data Cleaning:**: Standardize or clean any inconsistent values in columns.
5. **Feature Correlation Analysis:**: Calculate and visualize correlations between numerical features to understand relationships.
6. **Visualization of Key Features:**:Plot distributions for numerical features and bar charts for categorical features to get insights.

## Final Insights and Charts
1. **Top 10 neighborhoods in Riyadh with the highest average land prices per square meter**:This chart shows the top 10 neighborhoods with the highest land prices. It highlights that the most expensive neighborhoods are "Thulaim" and "Al-Yasmeen."

   <img width="625" alt="image" src="https://github.com/user-attachments/assets/4212e558-ee20-4755-b5dc-acac0e31a8d4">

2. **The neighborhoods in Riyadh with the highest number of land plots listed for sale**: "حي النرجس" and "حي المهدية" leading, each having over 100 listings. This high availability suggests these areas might be experiencing increased development or expansion, attracting sellers looking to capitalize on demand. Neighborhoods like "حي ظهرة لبن," "حي الرمال," and "حي عريض" also have a significant number of listings, indicating they are popular or in-demand areas for land transactions. The abundance of listings in these neighborhoods could point to competitive pricing opportunities for buyers, as well as potential for future growth and infrastructure development in Riyadh.
  <img width="625" alt="image" src="https://github.com/user-attachments/assets/3d375980-26c9-4ce2-bd0f-064fa99f0379">

4. **The relationship between land area and price per square meter**: This scatter plot shows the relationship between land area and price per square meter in various neighborhoods in Riyadh. Smaller plots generally have a higher price per square meter, while larger plots tend to be more affordable per square meter. This pattern indicates that buyers are willing to pay a premium for smaller plots, possibly due to their availability in more desirable or accessible locations.
![image](https://github.com/user-attachments/assets/f397ceaf-ca41-4755-98ff-29d511753d98)

   
6. **The distribution of land types in Riyadh neighborhoods**: This chart shows the distribution of land types in Riyadh neighborhoods based on their intended use, indicating that residential plots make up the majority in most neighborhoods, especially in "Al-Mahdiyah" and "Al-Narjis," reflecting high demand or availability of residential land in these areas. Mixed-use plots (residential and commercial) appear in moderate proportions, particularly in neighborhoods like "Al-Rimal" and "Dhahrat Laban," while purely commercial plots are less prevalent, which may reflect the predominantly residential nature of most of these neighborhoods.
![image](https://github.com/user-attachments/assets/d35655ef-c9f7-48f6-b73f-f78f5837b79d)


For a live, interactive experience, explore our [Aqar Analysis Streamlit App](https://usecase-6-project-3-phn4sparwclq7lawgvqobu.streamlit.app/) to dive into the insights and visualizations.
