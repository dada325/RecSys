# content_based_model.py

import pandas as pd
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import linear_kernel

class ContentBasedRecommender:
    def __init__(self, item_data):
        self.item_data = item_data
        self.item_ids = item_data['item_id'].tolist()
        self.tfidf_vectorizer = TfidfVectorizer(stop_words='english')
        self.item_profiles = self.tfidf_vectorizer.fit_transform(item_data['description'])

    def _get_item_profile(self, item_id):
        idx = self.item_ids.index(item_id)
        return self.item_profiles[idx:idx+1]

    def recommend_items(self, user_profile, top_n=10):
        # Compute the cosine similarity between the user profile and all item profiles
        cosine_similarities = linear_kernel(user_profile, self.item_profiles)

        # Get the top recommendations
        item_indices = cosine_similarities.argsort().flatten()[-top_n:]
        recommended_items = [(self.item_ids[idx], cosine_similarities[0, idx]) for idx in item_indices]

        return sorted(recommended_items, key=lambda x: -x[1])

    def create_user_profile(self, user_interactions):
        # User interactions is a list of item_id that the user has interacted with
        user_item_profiles = [self._get_item_profile(item_id) for item_id in user_interactions]
        user_profile = sum(user_item_profiles)
        return user_profile

# Example usage:
if __name__ == "__main__":
    data = {
        'item_id': [1, 2, 3],
        'description': ['sci-fi book', 'romance novel', 'mystery thriller']
    }
    item_data = pd.DataFrame(data)

    model = ContentBasedRecommender(item_data)

    # Suppose user has interacted with items 1 and 3
    user_profile = model.create_user_profile([1, 3])

    recommendations = model.recommend_items(user_profile)
    print(recommendations)
