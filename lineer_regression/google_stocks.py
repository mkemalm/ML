import pandas as pd
import quandl, math
import numpy as np
from sklearn import preprocessing,model_selection
from sklearn.linear_model import LinearRegression

#load dataset
quandl.ApiConfig.api_key="XXXXXX"
df = quandl.get('WIKI/GOOGL')

#features
df = df[['Adj. Open',  'Adj. High' ,  'Adj. Low',  'Adj. Close', 'Adj. Volume']]
df['HL_PCT'] = (df['Adj. High'] - df['Adj. Close'])/df['Adj. Close']*100.0
df['PCT_change'] = (df['Adj. Close'] - df['Adj. Open'])/df['Adj. Open']*100.0
df = df[['Adj. Close','HL_PCT','PCT_change','Adj. Volume']]

#label
forecast_col = 'Adj. Close'
df.fillna(-99999, inplace=True)
forecast_out = int(math.ceil(0.01*len(df)))
df['label'] = df[forecast_col].shift(-forecast_out)
df.dropna(inplace=True)

#train model
x = np.array(df.drop(['label'],1))
y = np.array(df['label'])
x = preprocessing.scale(x)
x_train, x_test, y_train, y_test = model_selection.train_test_split(x,y,test_size=0.2)
clf = LinearRegression()
clf.fit(x_train,y_train)

#accuracy
clf.score(x_test,y_test)
