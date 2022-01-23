#!/usr/bin/env python
# coding: utf-8

# In[323]:


import pandas as pd
data=pd.read_csv("tmdb_5000_movies.csv")
data1=pd.read_csv("tmdb_5000_credits.csv")
data.head()


# In[324]:


data1.head()




# In[325]:


data=data[['genres','keywords','overview','tagline','title']]
data.head()


# In[326]:


da=data.merge(data1,on='title')
da.dropna(inplace=True)
da.head()


# In[327]:


da['genres'][0]


# In[328]:


import  ast # for converting str into list
def genres_key(obj):
    st=[]
    for i in ast.literal_eval(obj):
        st.append(i['name'])
    return st
    
    


# In[329]:


da['genres']=da['genres'].apply(genres_key)


# In[330]:


da['keywords'][0]


# In[331]:


da['keywords']=da['keywords'].apply(genres_key)


# In[332]:


da['keywords'][0]


# In[333]:


def cast(obj):
    st=[]
    j=0
    for i in ast.literal_eval(obj):
        st.append(i['name'])
        j=j+1
        if j==4:
            break
    return st
        


# In[334]:


da['cast'][0]


# In[335]:


da['cast']=da['cast'].apply(cast)


# In[336]:


da['cast'][0]


# In[337]:


da['crew'][0]


# In[338]:


def direct_crew(obj):
    st=""
    for i in ast.literal_eval(obj):
        if i['job']=='Director':
            return [i['name']]


# In[339]:


da['crew']=da['crew'].apply(direct_crew)


# In[340]:


da['crew'][0]


# In[341]:


da.dropna(inplace=True)
da.head()


# In[342]:


da['cast']=da['cast'].apply(lambda x:[i.replace(" ","") for i in x])
da['keywords']=da['keywords'].apply(lambda x:[i.replace(" ","") for i in x])
da['genres']=da['genres'].apply(lambda x:[i.replace(" ","") for i in x])
da['crew']=da['crew'].apply(lambda x:[i.replace(" ","") for i in x])


# In[343]:


da.head()


# In[344]:


da['cast']=da['cast'].apply(lambda x:" ".join(x))
da['crew']=da['crew'].apply(lambda x:" ".join(x))
da['keywords']=da['keywords'].apply(lambda x:" ".join(x))
da['genres']=da['genres'].apply(lambda x:" ".join(x))


# In[345]:


da['crew'].isnull().sum()


# In[346]:


da.head()


# In[347]:


da['descr']=da['genres']+" "+da['cast']+" "+da['crew']+" "+da['keywords']+" "+da['overview']
da=da[['movie_id','title','descr']]


# In[348]:


da['descr'][0]


# In[349]:


da['descr']=da['descr'].apply(lambda x:str(x).lower())


# In[350]:


da.head()


# In[370]:


from sklearn.feature_extraction.text import CountVectorizer
cv = CountVectorizer(max_features=5000,stop_words='english')# for bag of words it actually takes 5000 common words and for each and evry movie it is gona see the count of common words this is known as vector
vector=cv.fit_transform(da['descr']).toarray()
vector.shape


# In[352]:


from sklearn.metrics.pairwise import cosine_similarity
similarity=cosine_similarity(vector)# it first finds distance and then based on distance it is going to find similarity
similarity


# In[353]:


def find_index(t)
    for i in range(len(da['title'])):
        if t==da.iloc[i]['title']:
                return i
                 
                
                


# In[367]:


def recom(o,similarity):
    ans=[]
    c=similarity[o]
    d=list(similarity[o])
    c=sorted(c,reverse=True)
    
    for i in range(5):
        ii=d.index(c[i])
        ans.append(da.iloc[ii]['title'])
    return ans
        
        


# In[371]:


x='Gandhi'
f=find_index(x)
print(f)
df=recom(f,similarity)
df


# In[362]:





# In[365]:





# In[ ]:




