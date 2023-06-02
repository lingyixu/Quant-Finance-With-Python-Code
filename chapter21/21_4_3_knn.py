from sklearn.neighbors import KNeighborsClassifier
knn = KNeighborsClassifier(n_neighbors=n).fit(X_train, y_train)
knn.predict(X_test)
knn.predict_proba(X_test)