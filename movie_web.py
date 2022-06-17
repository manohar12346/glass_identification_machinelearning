import numpy as np
import pandas as pd
import streamlit as st
import pickle
st.title('MOVIE RECCAMENDATION SYSTEM')
st.subheader('PIck one movie and get five movie that you love')


# In[90]:



data=pd.read_csv("tmdb_5000_movies.csv")
data1=pd.read_csv("tmdb_5000_credits.csv")
data.head()


# In[91]:


data1.head()




# In[92]:


data=data[['genres','keywords','overview','tagline','title']]
data.head()


# In[93]:


da=data.merge(data1,on='title')
da.dropna(inplace=True)
da.head()


# In[94]:


da['genres'][0]


# In[95]:


import  ast # for converting str into list
def genres_key(obj):
    st=[]
    for i in ast.literal_eval(obj):
        st.append(i['name'])
    return st
    
    


# In[96]:


da['genres']=da['genres'].apply(genres_key)


# In[97]:


da['keywords'][0]


# In[98]:


da['keywords']=da['keywords'].apply(genres_key)


# In[99]:


da['keywords'][0]


# In[100]:


def cast(obj):
    st=[]
    j=0
    for i in ast.literal_eval(obj):
        st.append(i['name'])
        j=j+1
        if j==4:
            break
    return st
        


# In[101]:


da['cast'][0]


# In[102]:


da['cast']=da['cast'].apply(cast)


# In[103]:


da['cast'][0]


# In[104]:


da['crew'][0]


# In[105]:


def direct_crew(obj):
    st=""
    for i in ast.literal_eval(obj):
        if i['job']=='Director':
            return [i['name']]


# In[106]:


da['crew']=da['crew'].apply(direct_crew)


# In[107]:


da['crew'][0]


# In[108]:


da.dropna(inplace=True)
da.head()


# In[109]:


da['cast']=da['cast'].apply(lambda x:[i.replace(" ","") for i in x])
da['keywords']=da['keywords'].apply(lambda x:[i.replace(" ","") for i in x])
da['genres']=da['genres'].apply(lambda x:[i.replace(" ","") for i in x])
da['crew']=da['crew'].apply(lambda x:[i.replace(" ","") for i in x])


# In[110]:


da.head()


# In[111]:


da['cast']=da['cast'].apply(lambda x:" ".join(x))
da['crew']=da['crew'].apply(lambda x:" ".join(x))
da['keywords']=da['keywords'].apply(lambda x:" ".join(x))
da['genres']=da['genres'].apply(lambda x:" ".join(x))


# In[112]:


da['crew'].isnull().sum()


# In[113]:


da.head()


# In[114]:


da['descr']=da['genres']+" "+da['cast']+" "+da['crew']+" "+da['keywords']+" "+da['overview']
da=da[['movie_id','title','descr']]


# In[115]:


da['descr'][0]


# In[116]:


da['descr']=da['descr'].apply(lambda x:str(x).lower())


# In[117]:


da.head()


# In[118]:


from sklearn.feature_extraction.text import CountVectorizer
cv = CountVectorizer(max_features=5000,stop_words='english')# for bag of words it actually takes 5000 common words and for each and evry movie it is gona see the count of common words this is known as vector
vector=cv.fit_transform(da['descr']).toarray()
vector.shape


# In[119]:


from sklearn.metrics.pairwise import cosine_similarity
similarity=cosine_similarity(vector)# it first finds distance and then based on distance it is going to find similarity
similarity


# In[120]:


def find_index(t):
    for i in range(len(da['title'])):
        if t==da.iloc[i]['title']:
                return i
                 
                
                


# In[121]:


def recom(o,similarity):
    ans=[]
    c=similarity[o]
    d=list(similarity[o])
    c=sorted(c,reverse=True)
    
    for i in range(5):
        ii=d.index(c[i])
        ans.append(da.iloc[ii]['title'])
    return ans
        
        


# In[122]:


x='Newlyweds'
f=find_index(x)
print(f)
df=recom(f,similarity)
df


# In[123]:


import pickle 


# In[124]:


pickle.dump(similarity,open('similarit.pkl','wb'))


# In[125]:


pickle.dump(dict(da),open('da.pkl','wb'))


# In[126]:





# In[ ]:






da=pd.DataFrame(da)
option=st.selectbox(
    'Select the movie',
     da['title'].values())
st.button("Reccomend")