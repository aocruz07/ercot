#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd
import matplotlib.pyplot as plt
from statsmodels.tsa.api import ExponentialSmoothing, SimpleExpSmoothing, Holt


# In[88]:


df = pd.read_csv("temps.txt", sep="\t", index_col=0)
df


# In[6]:


df.plot(figsize=(20,10), legend=False)


# In[40]:


fit1996 = SimpleExpSmoothing(df["1996"], initialization_method="heuristic").fit(
    smoothing_level=0.2, optimized=False
)
df['1996'].plot(figsize=(20,10))
fit1996.fittedvalues.plot(figsize=(20,10))


# In[101]:


fitted_list = []
alpha = 0.5
for col in df.columns:
    fit = SimpleExpSmoothing(df[col], initialization_method="heuristic").fit(smoothing_level=alpha, optimized=False)
    fit_df = pd.DataFrame(fit.fittedvalues, columns=[col])
    fitted_list.append(fit_df)
fitted_concat = pd.concat(fitted_list, axis=1)
fitted_concat.plot(figsize=(20,10), legend=False)
#fitted_concat['1996'].plot(figsize=(20,10), legend=True, color="black")
#fitted_concat['2005'].plot(figsize=(20,10), legend=True, color="red")
#fitted_concat['2015'].plot(figsize=(20,10), legend=True, color="green")


# In[ ]:




