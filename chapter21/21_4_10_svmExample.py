from pandas_datareader import data
from sklearn import svm
from sklearn.metrics import accuracy_score, confusion_matrix, classification_report

# prepare data
df_price_train = data.get_data_yahoo('SPY', start='2012-03-01', end='2021-02-28')['Adj Close']
df_ret_train = np.log(df_price_train/df_price_train.shift(1)).dropna()
X_train = df_ret_train.values.reshape(-1, 1)[:-1]
y_train = np.where(df_ret_train>0, 1, 0)[1:]

df_price_test = data.get_data_yahoo('SPY', start='2021-03-01', end='2021-03-31')['Adj Close']
df_ret_test = np.log(df_price_test/df_price_test.shift(1)).dropna()
X_test = df_ret_test.values.reshape(-1, 1)[:-1]
y_test = np.where(df_ret_test>0, 1, 0)[1:]

# train the model
model = svm.SVC()
model.fit(X_train, y_train)
y_pred_train = model.predict(X_train)

# test the model
y_pred_test = model.predict(X_test)

# model performance on train set
print(accuracy_score(y_train, y_pred_train))  # accuracy
print(confusion_matrix(y_train, y_pred_train))  # confusion matrix
print(classification_report(y_train, y_pred_train, digits=4))  # full classification report

# model performance on test set
print(accuracy_score(y_test, y_pred_test))  # accuracy
print(confusion_matrix(y_test, y_pred_test))  # confusion matrix
print(classification_report(y_test, y_pred_test, digits=4))  # full classification report