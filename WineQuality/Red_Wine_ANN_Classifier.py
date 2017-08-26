
# coding: utf-8

# ## Initialization

# In[1]:


import pandas as pd
import numpy as np
import keras


# ## Importing the Data

# In[2]:


dataset = pd.read_csv("winequality-red.csv")
dataset.shape


# In[3]:


dataset.head()


# ## Creating X and Y

# In[5]:


X = dataset.iloc[:, 0:11].values
Y = dataset.iloc[:, 11].values


# In[6]:


X


# In[7]:


Y


# ## Preprocess the Data

# In[8]:


from sklearn.preprocessing import LabelEncoder, OneHotEncoder, StandardScaler


# In[9]:


le_Y = LabelEncoder()


# In[10]:


Y = le_Y.fit_transform(Y)
Y


# In[11]:


Y = Y.reshape(len(Y), 1)
ohe_Y = OneHotEncoder(categorical_features = [0])


# In[12]:


Y = ohe_Y.fit_transform(Y).toarray()
Y


# In[13]:


sc_X = StandardScaler()


# In[14]:


X = sc_X.fit_transform(X)
X


# ## Create Train and Test Data

# In[15]:


from sklearn.model_selection import train_test_split
X_train, X_test, Y_train, Y_test = train_test_split(X, Y, test_size = 0.2, random_state = 4)


# In[16]:


X_train.shape


# In[17]:


X_test.shape


# In[18]:


Y_train.shape


# In[19]:


Y_test.shape


# ## Create and train the Classifier

# In[20]:


from keras.models import Sequential
from keras.layers import Dense


# In[63]:


clf_ann = Sequential()

# First Hidden Layer
clf_ann.add(Dense(output_dim = 36, init = 'uniform', activation = 'relu', input_dim = 11))

# Second Hidden Layer
clf_ann.add(Dense(output_dim = 72, init = 'uniform', activation = 'relu'))

clf_ann.add(Dense(output_dim = 108, init = 'uniform', activation = 'relu'))

clf_ann.add(Dense(output_dim = 144, init = 'uniform', activation = 'relu'))

clf_ann.add(Dense(output_dim = 180, init = 'uniform', activation = 'relu'))

clf_ann.add(Dense(output_dim = 216, init = 'uniform', activation = 'relu'))

# Output Layer
clf_ann.add(Dense(output_dim = 6, init = 'uniform', activation = 'softmax'))

clf_ann.compile(optimizer = 'adam', loss = 'categorical_crossentropy', metrics = ['accuracy'])

clf_ann.fit(X_train, Y_train, batch_size = 10, nb_epoch = 100)


# In[64]:


Y_pred = clf_ann.predict(X_test)
Y_pred = (Y_pred > 0.5)


# ## Check the Accuracy

# In[65]:


from sklearn.metrics import accuracy_score
accuracy_score(Y_pred, Y_test)


# In[ ]:




