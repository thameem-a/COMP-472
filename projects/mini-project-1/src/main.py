from sklearn import datasets
from sklearn.linear_model import LogisticRegression
from sklearn.model_selection import train_test_split
from sklearn import metrics
import numpy as np
# import matplotlib.pyplot as plt

# load digits approx 1.8k 8x8 images
digitImg = datasets.load_digits()

# digitImg.data.shape -> (number of images, flattened image pixel count)
# digitImg.images.shape -> (number of images, width of image, height of image)

# https://www.geeksforgeeks.org/understanding-logistic-regression/
# https://scikit-learn.org/stable/auto_examples/classification/plot_digits_classification.html

# Normalize
# Flatten images
data = digitImg.images.reshape((len(digitImg.images), -1))
data = np.array([[i/d.max() for i in d]for d in data]) # i pray no empty images - Normalized to values between 0 and 1

# Split data into 80% train and 20% test subsets
X_train, X_test, y_train, y_test = train_test_split(
    data, digitImg.target, test_size=0.2, shuffle=False
)

clf = LogisticRegression(random_state=0).fit(X_train, y_train)
predicted = clf.predict(X_test)

print(
    f"Classification report for classifier {clf}:\n"
    f"{metrics.classification_report(y_test, predicted)}\n"
)
