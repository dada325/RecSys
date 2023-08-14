
import tensorflow as tf
from tensorflow import keras

class NeuralCombiner:
    def __init__(self):
        self.model = keras.Sequential([
            keras.layers.Dense(8, activation='relu', input_shape=(3,)), # 3 input scores
            keras.layers.Dense(4, activation='relu'),
            keras.layers.Dense(1, activation='sigmoid')  # Final score between 0 and 1
        ])
        self.model.compile(optimizer='adam', loss='mean_squared_error')

    def train(self, training_data, labels):
        self.model.fit(training_data, labels, epochs=50)

    def predict(self, input_scores):
        return self.model.predict(input_scores)
