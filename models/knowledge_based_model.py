# knowledge_based_model.py

import pandas as pd

class KnowledgeBasedRecommender:
    def __init__(self, item_data):
        self.item_data = item_data

    def recommend_by_preference(self, user_preference, n=10):
        # Filter items by user's preference
        recommended_items = self.item_data[self.item_data['description'].str.contains(user_preference)]
        return recommended_items.head(n)
