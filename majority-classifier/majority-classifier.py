import numpy as np

def majority_classifier(y_train, X_test):
    """
    Predict the most frequent label in training data for all test samples.
    """
    # Write code here
    # Find the most frequent label in the training set
    y_train, X_test = np.asarray(y_train), np.asarray(X_test)
    
    unique_labels, counts = np.unique(y_train, return_counts=True)
    majority_label = unique_labels[np.argmax(counts)]

    # Create an array of predictions, all set to the majority label
    # The length matches the number of samples in X_test
    y_pred = np.full(X_test.shape[0], majority_label, dtype=y_train.dtype)

    return y_pred