# use 'pipstall scikit-learn' rather than 'pip install sklearn'
# https://scikit-learn.org/stable/auto_examples/datasets/plot_iris_dataset.html

from sklearn.datasets import load_iris
from sklearn.model_selection import train_test_split
from sklearn.svm import SVC

# Load the Iris flower dataset (already labeled)
iris = load_iris()
X = iris.data  # Features (measurements of the flowers)
y = iris.target  # Labels (type of flower)

# Split data into training and testing sets
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2)

# Train a Support Vector Machine (SVM) classifier
clf = SVC()
clf.fit(X_train, y_train)

# Use the trained model to predict the class of a new flower
new_flower = [[5.1, 3.5, 1.4, 0.2]]  # Features of a new flower
predicted_class = clf.predict(new_flower)

# Show the predicted class
print("Predicted flower type:", iris.target_names[predicted_class[0]])
