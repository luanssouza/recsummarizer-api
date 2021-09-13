import pandas as pd
import numpy as np

class BaseRecommender(object):
    def __init__(self, train: pd.DataFrame):
        self._train = train
        
    def predict(self, user, item, k = 5):
        '''

        '''
        pass
    
    def recommend(self, user, k = 5):
        '''
        
        '''
        pass