#!/usr/bin/env python
# coding: utf-8

# In[53]:


import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt


# In[54]:


antibio_df = pd.read_csv('Antibiotics.csv')


# In[55]:


antibio_df


# In[56]:


antibio_df.info()


# In[57]:


antibio_df['Residual_Splits']= antibio_df['Observation'].str.split()


# In[58]:


antibio_df['Residual_Antibiotics'] = [x[1] for x in antibio_df['Observation'].str.split()]


# In[59]:


antibio_df


# In[63]:


antibio_df['unit'] = [x[-1] for x in antibio_df['Observation'].str.split()]


# In[64]:


antibio_df[antibio_df.loc[:,'Residual_Antibiotics']=='ppm'] 


# In[65]:


updated_val = antibio_df.loc[:,'Residual_Antibiotics']=='ppb'
antibio_df.loc[updated_val, 'Residual_Antibiotics'] = 0


# In[66]:


antibio_df


# In[67]:


antibio_df[antibio_df.loc[:,'unit']=='ppm']


# In[51]:


antibio_df['Residual_Antibiotics'].value_counts()


# In[68]:


filt =antibio_df[antibio_df.loc[:,'unit']=='ppm']


# In[72]:


filt


# In[70]:


antibio_df


# In[ ]:




