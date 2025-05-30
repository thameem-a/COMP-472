# Logistic Regression

## Code Explanation

**Step 1.)** Import ~1800 images of hand-written digits, along with the actual values (MNIST dataset).

**Step 2.)** Verification and normalization procedure (flattens matrix into vector and verifies dataset to some extent)

**Step 3.)** Split data into training and testing (80% for training, 20% for testing--randomly shuffled)

**Step 4.)** Train the classifier without a "random start state"

**Step 5.)** Predict labels of the digits using the training data

**Step 6.)** Evaluate performance using confusion matrix and classification report

**Step 7.)** Visualize using matplotlib

## `sklearn` Handwritten Digit Dataset

There is approximately 1800 (greyscale?) images that are actually a 8x8 2D-`np.array` that contains integer values. The higher the integer, the darker the pixel is. Each of these images are associated with their actual written value.

## `normalize_images`

While testing and experimenting, the regression model could not handle large values within a large data set and has reported a warning that the max iterations have been reached. This required us to normalize the data set to only contain values between 0 and 1.

## `sklearn.model_selection.train_test_split`

As described by the assignment, it is required to have a ratio of 80:20 for training data to test data. Thankfully, the `scikit-learn` package comes with this handy function to partition the image data if given the correct ratio.

## `LogisticRegression`

### Background

Logistic Regression is a regression/statistical model used for classification of instances. It classifies by predicting the probability of a given instance being in a certain class. In our case, we want the model to classify handwritten data images to a digit. Therefore, our instances will be the test and train data that we are feeding it and the classes are the digits that each image represents.

#### Types

There are 3 types of Logistic Regression

1. Binomial: Only 2 classes are available for the model to predict: like a pass or fail.

2. **Multinomial**: 3 or more classes are available for the model to predict. Moreover, the classes are in a unordered fashion. This is likely what we are using in our assignment as the order of the digits do not pose significance.

3. Ordinal: 3 or more classes are available for the model to predict. Moreover the classes are in a ordered fashion where the last dependent variable poses more significance than the first one: like low, medium or high.

#### 

