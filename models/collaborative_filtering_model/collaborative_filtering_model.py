# collaborative_filtering_model.py

from surprise import SVD, Dataset, Reader
from surprise.model_selection import train_test_split
import pandas as pd

class CollaborativeFilteringRecommender:
    def __init__(self, user_item_ratings):
        reader = Reader(rating_scale=(1, 5))
        self.data = Dataset.load_from_df(user_item_ratings, reader)
        self.trainset, self.testset = train_test_split(self.data, test_size=.25)

    def train(self):
        self.algo = SVD()
        self.algo.fit(self.trainset)

    def predict(self, user_id, item_id):
        prediction = self.algo.predict(user_id, item_id)
        return prediction.est

    def get_top_n_recommendations(self, user_id, n=10):
        anti_testset = self.trainset.build_anti_testset()
        predictions = self.algo.test([x for x in anti_testset if x[0] == user_id])
        top_n = sorted(predictions, key=lambda x: x.est, reverse=True)[:n]
        return [(pred.iid, pred.est) for pred in top_n]
