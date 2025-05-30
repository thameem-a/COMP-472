from sklearn import datasets
from sklearn.linear_model import LogisticRegression
from sklearn.model_selection import train_test_split
from sklearn import metrics
import numpy as np
import matplotlib.pyplot as plt

def normalize_images(data):
    """Normalize 8x8 grayscale image arrays to have values between 0 and 1."""
    return np.array([[i/d.max() for i in d]for d in data]) # i pray no empty images - Normalized to values between 0 and 1

def visualize_sample(images, labels, index):
    """Display a sample image from the dataset."""
    plt.gray()
    plt.matshow(images[index])
    plt.title(f"Label: {labels[index]}")
    plt.show()

def main():
    
    # Step 1) Load digits approx 1.8k 8x8 images
    digitImg = datasets.load_digits()
    
    # Print dataset shape for verification
    print(f"Digits data shape: {digitImg.images.shape} (Images), {digitImg.data.shape} (Flattened Data)")


    # digitImg.data.shape -> (number of images, flattened image pixel count)
    # digitImg.images.shape -> (number of images, width of image, height of image)

    # https://www.geeksforgeeks.org/understanding-logistic-regression/
    # https://scikit-learn.org/stable/auto_examples/classification/plot_digits_classification.html

    # Step 2) Flatten and Normalize the images
    flat_data = digitImg.images.reshape((len(digitImg.images), -1))
    normalized_data = normalize_images(flat_data)

    # Step 3) Split dataset into 80% train and 20% test subsets
    X_train, X_test, y_train, y_test = train_test_split(
        normalized_data, digitImg.target, test_size=0.2, shuffle=True #Setting shuffle=True to gives a more random distribution
    )

    # Step 4) Train a Logistic Regression classifier
    clf = LogisticRegression(random_state=0).fit(X_train, y_train)
    
    # Step 5) Pedrict the test labels
    predicted = clf.predict(X_test)

    # Step 6) Evaluate performance 
    print(
        f"\nClassification report for classifier {clf}:\n"
        f"\n{metrics.classification_report(y_test, predicted)}\n"
    )
    print(
        f"\nConfusion matrix:\n{metrics.confusion_matrix(y_test, predicted)}\n"
    )
    
    #Step 7) Visualize a sample image
    visualize_sample(digitImg.images, digitImg.target, index=0)  # Display the first image as an example, change index to see others

if __name__ == "__main__":
    main()
