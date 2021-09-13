import pandas as pd
import numpy as np

from src.recommender.base_recommender import BaseRecommender

class UserKnn(BaseRecommender):
    def __init__(self, train: pd.DataFrame):
        super().__init__(train)
        
        self.__ratings = self._train.pivot(index='movie_id', columns='user_id', values='rating')
        self.__sim = self.__ratings.corr(method='pearson')
        
    def predict(self, user, item, k = 5):
        u = user
        i = item
        ratings = self.__ratings
        sim = self.__sim
        ratings_t = ratings.T
        if u not in sim or i not in ratings_t:
            return 0
        sim_users = sim[u][~sim[u].isna()].sort_values(ascending=False).index
        rated_users = ratings_t[i][ratings_t[i] > 0].index
        sim_k = np.intersect1d(sim_users, rated_users)
        top_k = [x for x in sim_users if x in sim_k][:k]
        sum_sim = 0
        dem = 0
        mean_u = ratings[u].mean(skipna = True)
        for v in top_k:
            dem += sim[u][v] * (ratings[v][i] - ratings[v].mean(skipna = True))
            sum_sim += sim[u][v]
        if sum_sim == 0:
            return 0
        return mean_u + (dem/sum_sim)

    def recommend(self, user, k = 5):
        ratings = self.__ratings

        non_rated_movies = ratings[user][ratings[user].isna()].index

        def sort_func(e):
            return e[1]

        r = []
        for index in non_rated_movies:
            r.append((index, self.predict(user, index, k)))

        r.sort(key=sort_func, reverse=True)

        return r