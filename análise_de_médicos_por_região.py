#!/usr/bin/env python
# coding: utf-8

# In[122]:


import pandas as pd
low_memory=False
import matplotlib.pyplot as plt
get_ipython().run_line_magic('matplotlib', 'inline')
pd.options.display.max_columns = 80
pd.options.display.max_rows = 90


# In[123]:


filename = r'C:/Users/Gustavo/Desktop/EPLBD/medicos1.csv'
df = pd.read_csv(filename, delimiter=',', 
                 encoding='UTF8',
                 error_bad_lines=False)


# In[124]:


''' Análise feita por Gustavo Henrique Nascimento
    Esta análise tem como principal objetivo fazer um comparativo sobre a proporção de médicos ativos nas regiões do Brasil.
    Os dados desta análise foram retirados do portal do CFM (link "http://portal.cfm.org.br/index.php?option=com_estatistica&buscarPor=R&ufEstatistica=&regiaoEstatistica=S&situacaoEstatistica=A&detalheSituacaoEstatistica=&sexoEstatistica=")
    e foram atualizados no dia 03/07/2020
    
    Análise baseada no 
    
    '''


# In[125]:


df.shape


# In[126]:


for par in enumerate(df.columns): print (par)


# In[127]:


df.sample(7)


# In[128]:


df.head(27)


# In[ ]:





# In[129]:


ax = df [['Capital','Região']].plot(figsize=(10,10), kind='barh')
ax.set_yticklabels(df['UF'])


# In[130]:


ax = df [['Interior','Região']].plot(figsize=(10,10), kind='barh')
ax.set_yticklabels(df['UF'])


# In[131]:


ax = df [['Total','Região']].plot(figsize=(10,10), kind='barh')
ax.set_yticklabels(df['UF'])

