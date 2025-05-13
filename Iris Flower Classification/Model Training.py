# Initialize and train K-Nearest Neighbors classifier
model = KNeighborsClassifier(n_neighbors=3)
model.fit(X_train, y_train)
