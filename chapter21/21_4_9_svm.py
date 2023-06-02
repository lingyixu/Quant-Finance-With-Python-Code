from sklearn import svm
model = svm.SVC()
model.fit(X_train, y_train)
model.support_vectors_
model.predict(X_test)