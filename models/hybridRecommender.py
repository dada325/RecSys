from content_based_model import ContentBasedRecommender
from collaborative_filtering_model import CollaborativeFilteringRecommender
from knowledge_based_model import KnowledgeBasedRecommender
from network import neural_combiner
import pandas as pd

class HybridRecommender:
    def __init__(self, item_data, user_item_ratings):
        self.content_model = ContentBasedRecommender(item_data)
        self.collab_model = CollaborativeFilteringRecommender(user_item_ratings)
        self.knowledge_model = KnowledgeBasedRecommender(item_data)
        self.neural_combiner = NeuralCombiner()

    def train(self):
        # Train content and collab models
        self.collab_model.train()

    def recommend(self, user_id, user_interactions, user_preference=None):
        # Fetch recommendations from individual models
        collab_score = self.collab_model.get_top_n_recommendations(user_id, 1)[0][1] if self.collab_model.get_top_n_recommendations(user_id) else 0
        content_score = self.content_model.recommend_items(user_profile)[0][1] if self.content_model.recommend_items(user_profile) else 0
        knowledge_score = 1 if user_preference and self.knowledge_model.recommend_by_preference(user_preference).shape[0] > 0 else 0

        # Using the neural network to get a combined recommendation score
        combined_score = self.neural_combiner.predict([[collab_score, content_score, knowledge_score]])

        # Sort and return the final recommendations. For now, returning the combined score for the demonstration.
        return combined_score[0]
