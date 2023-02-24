#!/usr/bin/env python
# coding: utf-8

# In[2]:


import pandas as pd


# In[3]:


makers = pd.Series(['BMW','Toyota','Honda','Toyota'])


# In[4]:


makers


# In[5]:


makers.value_counts()


# In[6]:


colours = pd.Series(['red','yellow','black'])


# In[7]:


colours


# In[8]:


# for data frame which is 2Dimensional
cars_data_1 = pd.DataFrame({'car maker':makers,'colour':colours })


# In[9]:


cars_data_1


# In[10]:


#import data
df1 = pd.read_csv('car-sales.csv')


# In[11]:


df1


# In[137]:


df1.to_csv('exporteed_car_sales.csv',index=False)


# In[138]:


df2 = pd.read_csv("exporteed_car_sales.csv")


# In[139]:


df2


# ##Describe Data

# In[15]:


#Attributes
df1.dtypes


# In[16]:


#functions
# df1.to_csv()


# In[17]:


df1.columns


# In[18]:


df1.index


# In[19]:


df1.describe()


# In[20]:


df1.info()


# In[21]:


df1.mean()


# In[22]:


#mean of series
car_series = pd.Series([1003,456,4789,4456,876])


# In[23]:


car_series


# In[24]:


car_series.mean()


# In[25]:


df1.sum()


# In[26]:


df1["Odometer (KM)"].sum()


# In[27]:


len(df1)


# In[28]:


#selecting and viewing data


# In[29]:


df1.head(7)


# In[30]:


df1.tail(6)


# In[31]:


#.loc & .iloc
animals = pd.Series(['dog','cat','elephant','zebra','panda'])


# In[32]:


animals


# In[33]:


animals = pd.Series(['dog','cat','elephant','zebra','panda'], index=[8,40,5,7,40])


# In[34]:


animals


# In[35]:


animals.loc[40]


# In[36]:


animals.loc[5]


# In[37]:


df1.loc[3]


# In[38]:


#iloc
animals.iloc[0]


# we can see that from above example that iloc refers to position no matter if you have already changed the index

# In[39]:


df1.iloc[3]


# In[40]:


df1.iloc[:4]


# In[41]:


df1.loc[:4]


# In[42]:


df1['Colour']
# or 
df1.Colour


# In[43]:


df1['Make']
#or
df1.Make


# In[44]:


#df1.Odometer (KM) this will give error 

df1['Odometer (KM)']


# In[45]:


df1[df1['Make'] == 'Honda']


# In[46]:


df1[df1['Make']=='Toyota']


# In[47]:


df1[df1['Odometer (KM)']<=60000]


# In[48]:


pd.crosstab(df1['Make'],df1['Doors'])


# In[49]:


pd.crosstab(df1['Make'],df1['Doors']).plot(kind='bar')


# In[50]:


#group by
df1.groupby(['Make']).mean()


# In[51]:


pd.crosstab(df1['Make'],df1['Colour'])


# In[52]:


df1['Odometer (KM)'].plot()


# In[53]:


df1['Odometer (KM)'].hist()


# In[54]:


df1['Price'] = df1['Price'].replace('[\$\,\.]', '', regex=True).astype(int)


# In[55]:


df1['Price'] = df1['Price']//100


# In[56]:


df1['Price']


# In[57]:


df1['Price'].plot()


# In[58]:


df1['Price'].hist()


# # Manipulating data

# In[59]:


# temporary lowered the string
df1['Make'].str.lower()


# In[60]:


# in pandas for saving the cahnges you have to reassign it 
df1['Make'] = df1['Make'].str.lower()


# In[61]:


df1['Make']


# In[71]:


car_missing_data = pd.read_csv('car-sales-missing-data.csv')


# In[72]:


car_missing_data.head(7)


# In[73]:


car_missing_data['Odometer'].mean()


# In[74]:


car_missing_data['Odometer'].fillna(car_missing_data['Odometer'].mean())


# In[81]:


#we can see that the changes is not saved
car_missing_data


# In[82]:


# here we have used inplace for save the changes we have made
car_missing_data['Odometer'].fillna(car_missing_data['Odometer'].mean() , inplace=True)


# In[83]:


car_missing_data


# In[87]:


#drop rows which consist na values
#we can also use inplace to make our change permanent i.e. car_missing_data.dropna(inplace=True)
car_missing_data.dropna()


# In[94]:





# In[96]:


#we are assigning the dropped dataset(drop na)in to another dataframe so that we can have our original and changed(where we dropped the na) data
car_missing_data = pd.read_csv('car-sales-missing-data.csv')
car_missing_data_dropped = car_missing_data.dropna()


# In[101]:


car_missing_data.head(8)


# In[109]:


# for adding column in datasets
seat_column = pd.Series([5,5,5,5,5])
df1['Seats'] = seat_column


# In[110]:


df1


# In[111]:


#but, this will only fill top 5 cells of the'seat' column of our dataset, for filling the other remaining cells we use fillna
#replace the na with value 5 and use inplace to save change
df1.fillna(5 , inplace=True)


# In[112]:


df1


# In[113]:


# column using python list
fuel = [7.5,9.4,6.5,8.4,4.9,7.2,9.3,8.6,5.1,8.1]
df1['fuel per 100KM'] = fuel


# In[114]:


df1


# In[115]:


# above, we uses list to make column but the length of list and dataset should be equal otherwise it will show error


# In[116]:


df1['total_fuel_used']= (df1['Odometer (KM)']/100)*df1['fuel per 100KM']


# In[117]:


df1


# In[118]:


df1['wheels'] = 4


# In[119]:


df1


# In[121]:


df1['Passes road safety'] = True
df1


# In[124]:


df1.dtypes


# In[132]:


df1.drop('wheels',axis=1,inplace=True)


# In[133]:


df1


# In[145]:


df1_shuffled = df1.sample(frac=1)


# In[146]:


df1_shuffled


# In[149]:


df1_shuffled.reset_index(drop=True)


# In[150]:


df1['Odometer (Miles)'] = df1['Odometer (KM)'].apply(lambda x:x/1.6)


# In[151]:


df1


# In[2]:


pip install pandoc


# In[ ]:




