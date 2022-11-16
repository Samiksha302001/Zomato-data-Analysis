#!/usr/bin/env python
# coding: utf-8

# # Exploratory Data Analysis
# 
# This notebook focusses on the first step of any data science project: exploring the data.<br>
# *Exploratory Data Analysis* or EDA is to get familiar to our data, identifying important columns, perform data manipulation and 
# asking interesting questions from our data using visualization tools.

# ###  Data Description  
# #### Zomato is an Indian restaurant aggregator and food delivery start-up founded by Deepinder Goyal and Pankaj Chaddah in 2008. Zomato provides information, menus and user-reviews of restaurants as well as food delivery options from partner restaurants in select cities.
# 
# ### Problem Statement
# In this session, we are going to analyze the restaurant business data. We want to study the food habbits of zomato users, their preferances, ratings etc.
# 
# ### Data description:
# The collected data has been stored in the Comma Separated Value file Zomato.csv. Each restaurant in the dataset is uniquely identified by its Restaurant Id. Every Restaurant contains the following variables:
# 
# • Restaurant Id: Unique id of every restaurant across various cities of the world
# 
# • Restaurant Name: Name of the restaurant
# 
# • Country Code: Country in which restaurant is located
# 
# • City: City in which restaurant is located
# 
# • Address: Address of the restaurant
# 
# • Locality: Location in the city
# 
# • Locality Verbose: Detailed description of the locality
# 
# • Longitude: Longitude coordinate of the restaurant's location
# 
# • Latitude: Latitude coordinate of the restaurant's location
# 
# • Cuisines: Cuisines offered by the restaurant
# 
# • Average Cost for two: Cost for two people in different currencies 👫
# 
# • Currency: Currency of the country
# 
# • Has Table booking: yes/no
# 
# • Has Online delivery: yes/ no
# 
# • Is delivering: yes/ no
# 
# • Switch to order menu: yes/no
# 
# • Price range: range of price of food
# 
# • Aggregate Rating: Average rating out of 5
# 
# • Rating color: depending upon the average rating color
# 
# • Rating text: text on the basis of rating of rating
# 
# • Votes: Number of ratings casted by people
# 
# There is another dataset which has the country codes in it

# 
# ### Objective: 
# #### Our goal in this notebook is to explore the data provided in Zomato csv and to analyze which restaurants have poor ratings in Zomato and why?

# In[58]:


import pandas as pd                                 # Importing pandas
import numpy as np                                  # Importing numpy
import matplotlib.pyplot as plt                     # Importing matplotlib for visualization

get_ipython().run_line_magic('matplotlib', 'inline')
import seaborn as sns                               # Importing seaborn for visualization


# ### Loading the datasets 

# The csv file has encoding ISO-8859-1.
# Encoding defines what kind of characters(ASCII or non ASCII or something different) can be stored in a file.  

# In[2]:


zomato_df = pd.read_csv('zomato.csv', encoding='ISO-8859-1')    # Reading file zomato.csv


# ### Inspecting Data

# In[3]:


zomato_df.head()                                                  # Visualizing top 5 rows


# In[4]:


country_df = pd.read_excel('Country-Code.xlsx')                         # Reading country code excel file


# In[5]:


zomato_data = pd.merge(zomato_df, country_df, on = 'Country Code')      # Pandas Merge function to join two dataframes
zomato_data.head()


# ### Data Exploration

# **Description of the numeric columns of dataset**

# In[6]:


zomato_data[['Average Cost for two', 'Price range', 'Aggregate rating', 'Votes']].describe()


# **Observation**<br>
# There are 9551 rows in all columns and there are no missing data in numeric columns. <br>
# **Average Cost for two** <br>
# The Standard Deviation is very high on 'Average Cost for two'. 
# It is for different countries having different currency. <br>
# There are 15 countries in this dataset and their currencies are not standardized. <br>
# Look at the maximum of average price for two : 800000.

# In[7]:


zomato_data[zomato_data['Average Cost for two'] == 800000]             # Extract rows which meet a specific condition


# On comparing 800000 Indonesian Rupiah to INR it is 3800INR, which is slightly high end.

# **Info of the dataset**

# In[8]:


zomato_data.info()                                          # Checking the info of the dataset


# **Observation** <br>
# There are no missing values in any columns except in cuisines. <br>
# Most of the rows are of datatype object i.e. they are categorical.

# **Missing values Imputation**

# In[9]:


# Filling the missing values in Cuisines

zomato_data['Cuisines'].fillna("Others", inplace=True)


# In[10]:


# Filling any numeric missing values

zomato_data['Aggregate rating'].fillna(zomato_data['Aggregate rating'].mean(), inplace=True)


# In[11]:


zomato_data.shape                                    # Number of rows and columns in a dataframe


# **Correlation plot of numeric columns**

# In[12]:


correlation = zomato_data[['Average Cost for two', 'Price range', 'Aggregate rating', 'Votes']].corr()
correlation


# In[13]:


sns.heatmap(correlation, vmin = -1, vmax = 1)                # Creating heatmap of the correlation matrix


# **Observation** <br>
# There is some correlation between *Price range* and *Aggregate rating* <br> 
# The rest of the columns have no correlation. <br>
# 
# If the Price range is higher, people should rate the restaurant higher.

# **Distribution of Aggregate Rating**

# In[14]:


sns.distplot(zomato_data['Aggregate rating']);


# **Observation**:  <br>
# A lot of restaurants are rated 0. After this most of the restaurants have been rated between 3 and 4.

# ### Bivariate Analysis
# 
# Here we check the relationship between two variables.

# In[15]:


# Relationship between Aggregate Ratings and Votes

sns.scatterplot(x=zomato_data['Aggregate rating'], y= zomato_data['Votes'])


# **Observation**: As the quality of food gets better, the aggregate ratings increases and the number of voters also increase.

# In[16]:


# Relationship between Aggregate Ratings and Votes

sns.lineplot(x=zomato_data['Aggregate rating'], y= zomato_data['Votes'])


# **Obeservation** : Here we can see the same inference. Aggregate Ratings and Votes have an increasing trend.

# In[17]:


# Relationship between Price range and Aggregate Ratings

sns.violinplot(x='Price range', y='Aggregate rating', data = zomato_data)


# **Observation 1** <br>
# Here we can clearly see that with increase in Price range, the median of ratings also increase.

# **Question: Which countries have the highest number of restaurants in Zomato?**

# In[18]:


"""
The background is whitegrid
The figure size is 14*6 
The x-axis labels are written with a rotation of 45 degree
setting the title to "# of Restaurants registered in Zomato in different Countries 
"""

sns.set_style('whitegrid')
plt.figure(figsize = (14,6))
sns.countplot(x= 'Country', data=zomato_data)
plt.xticks(rotation=45)
plt.title("# of Restaurants registered in Zomato in different Countries ");


# **Observation** <br>
# Most of the reataurants are from India. <br>
# India - 8652 <br>
# World - 9551

# ### Zomato India <a id='india'></a>  <br>
# 
# #### Objective: Our goal is to analyze which restaurants have poor ratings in Zomato and why?

# The number of restaurants registered in Zomato is highest in India.
# So lets look at the data of these restaurants.

# In[19]:


zomato_india = zomato_data[zomato_data['Country'] == 'India']    # Filter the country by India and create a new dataframe
zomato_india.head()


# **We have aggregate ratings and Rating text as two column of interest.**

# In[20]:


zomato_india.groupby('Rating text').mean()              # Perform groupby using Rating text


# **Excellent and Very Good** food ratings are provided in restaurants which are slightly premium cost and high price range.
# They also have huge number of votes. This can be due to high quality food or ambience due to which the price is high and so the ratings are good. 

# In[21]:


# Relationship between Average Cost for two and Rating text

sns.boxplot(y = 'Average Cost for two', x = 'Rating text', data = zomato_india)


# Ratings improve as the average cost for two increases.

# In[22]:


# Relationship between Price range and Rating text

sns.boxplot(y = 'Price range', x = 'Rating text', data = zomato_india)


# **Excellent and Very Good** restaurants have very high price.  <br>
# **Average and Poor** have the lowest price range.

# ### Lets identify restaurants which have high price range and low ratings

# In[23]:


zomato_india['Price range'].value_counts()


# In[24]:


# Lets have a look at the expensive restaurants

exp_india_restaurant = zomato_india[zomato_india['Price range'] == 4]
exp_india_restaurant


# In[25]:


# Lets check the ratings of these restaurants

exp_india_restaurant['Rating text'].value_counts()


# **As the price range is high, most of the ratings are good.**  <br>
# So if price is high, why will be there be 5 poor ratings?

# In[26]:


# Low rated expensive restaurants

exp_india_restaurant[exp_india_restaurant['Rating text'] == 'Poor']


# In[27]:


list_of_cuisines = exp_india_restaurant[exp_india_restaurant['Rating text'] == 'Poor']['Cuisines']
list_of_cuisines.values


# **Observations**: These are 5 restaurants which are really expensive but do not have good ratings. <br>
# **Lets have a look at what is their cuisines.**

# In[28]:


text = ' '.join([j for j in list_of_cuisines.values])
text


# **North Indian** is the most popular cuisine. So we can infer that these North Indian restaurants in Gurgaon and Noida which do not provide authentic North Indian dishes and that is why customers are unhappy and rate them poorly.

# ### Lets look at all the restaurants which have poor ratings.

# In[30]:


bad_rated_restaurants = zomato_india[zomato_india['Rating text'] == 'Poor']
bad_rated_restaurants


# In[31]:


bad_rated_restaurants.shape


# In[32]:


bad_rated_restaurants['Has Online delivery'].value_counts()


# In[33]:


bad_rated_restaurants['Is delivering now'].value_counts()


# **Many of these restaurants are not available for delivery most of the time. Hence people provide poor rating to them.**

# ### City wise Analysis of Poor Rated restaurants

# In[34]:


sns.countplot(x = 'City', data = bad_rated_restaurants)


# **Why are ratings of New Delhi, Noida and Gurgaon bad?**

# In[35]:


# Total no. of bad restaurants

bad_rated_restaurants['City'].value_counts()


# In[36]:


# Total number of restaurants

top_3_cities = zomato_india['City'].value_counts().head(3)
top_3_cities


# In[37]:


sns.barplot(y = top_3_cities, x = top_3_cities.index)


# **Hence we cannot conclude that these 3 cities have significantly large number of bad restaurants as the total number of restaurants is also high.**

# ### Let's make our plots interactive using Plotly-express

# In[63]:


# pip3 install plotly
import plotly.express as px
# import plotly_express as px
# import plotly.plotly as py
pip install plotly


# In[64]:


# Scatter Plot

px.scatter(zomato_data, x="Average Cost for two", y="Votes", size="Votes", color="Rating text", log_x=True, size_max=60,hover_name='City')


# **Observation**: We can see how the Average Cost for two and the Votes are related and in which cities. 

# In[45]:


# Scatter Plot

px.scatter_matrix(zomato_data, dimensions=['Average Cost for two', 'Price range', 'Aggregate rating', 'Votes'], color='Rating text')


# **Observation** : There is not much correlation between the variables.

# In[46]:


# Box plot of Rating text and Average Cost for two

px.box(zomato_india, x="Rating text", y="Average Cost for two", color="Price range", notched=True)


# **Observation**: Good and Very Good food have very high cost as compared to excellent and other types of food.

# In[47]:


# Relationship between Online Delivery and Aggregate rating

px.histogram(zomato_data, x="Has Online delivery", y="Aggregate rating", histfunc="avg")


# **Observations**: Restaurants which have online delivery have better ratings.

# In[48]:


px.histogram(zomato_data, x="Has Table booking", y="Aggregate rating", histfunc="avg")


# **Observations**: Restaurants which have table booking available have more ratings in general.

# In[49]:


px.histogram(zomato_data, x="Is delivering now", y="Aggregate rating", histfunc="avg")


# **Observation**: Restaurants which are delivering now have better ratings than the one which are not.

# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:




