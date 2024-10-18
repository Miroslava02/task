#!/usr/bin/env python
# coding: utf-8

# In[6]:


data = pd.read_csv("C:\\ffff\data.csv") 


# In[ ]:


#по техническим причинам не получилось открыть файл, поэтому далее представлен код, без выгрузки результатов


# In[2]:


import pandas as pd
import seaborn as sn


# In[ ]:


data['receiving_data'] = pd.to_datetime(data['receiving_data'], format = (%d.%m.%Y)) #форматирование времени


# In[ ]:


#сумма выручки за июль 2021


# In[ ]:


data_filtered = data[(data['receiving_date'] >= '01.07.21') & (data['receiving_date'] <= '31.07.21')] 


# In[ ]:


sum_not_expired = data_filtered.query('status!="ПРОСРОЧЕНО"')['sum'].sum()


# In[ ]:


#график


# In[ ]:


data.plot()


# In[ ]:


#менеджеры, принёсшие больше всего прибыли в сентябре 2021


# In[ ]:


data_filtered = data[(data['receiving_date'] >= '01.09.21') & (data['receiving_date'] <= '30.09.21')]


# In[ ]:


sales_df = data_filtered.group_by(['sale']).sum()


# In[ ]:


str = sales_df[sales_df['sum']==sales_df['sum'].max()]


# In[ ]:


#преобладающие типы сделок в октябре 2021


# In[ ]:


data_filtered = data[(data['receiving_date'] >= '01.10.21') & (data['receiving_date'] <= '31.10.21')]


# In[ ]:


new_current_comparison = data_filtered.group_by(['new/current']).count()


# In[ ]:


data_filtered = data[(data['receiving_date'] >= '01.06.21') & (data['receiving_date'] <= '30.06.21')]


# In[ ]:


#оригиналы, полученные в июне


# In[ ]:


originals = data_filtered.query('document=="оригинал"')['document'].count()


# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:


#ЗАДАНИЕ 


# In[ ]:


data['manager_bonus'] = data['sum'] # новый столбец для подсчёта бонусов


# In[ ]:


data_filtered = data[data['receiving_date'] <= '01.07.21'] #фильтрация данных по времени (до 1-ого июня)


# In[ ]:


# столбец бонусов согласно условиям
data_filtered.loc[(data_filtered['status'] == "ОПЛАЧЕНО") & (data_filtered['document'] == "оригинал") & (data_filtered['new/current']=='новая'), 'manager_bonus'] = data_filtered.loc['sum']*0.07
data_filtered.loc[(data_filtered['status'] != "ПРОСРОЧЕНО") & (data_filtered['document'] == "оригинал") & (data_filtered['new/current']=='текущая') & (data_filtered['sum']>=10000), 'manager_bonus'] = data_filtered.loc['sum']*0.05
data_filtered.loc[(data_filtered['status'] != "ПРОСРОЧЕНО") & (data_filtered['document'] == "оригинал") & (data_filtered['new/current']=='текущая') & (data_filtered['sum']<10000), 'manager_bonus'] = data_filtered.loc['sum']*0.03


# In[ ]:


#таблица с бонусами менеджеров


# In[ ]:


df = data_filtered.group_by(['sale']).sum()


# In[ ]:




