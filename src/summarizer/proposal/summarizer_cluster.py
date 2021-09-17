import pandas as pd
import numpy as np

from scipy import cluster

from src.summarizer.base_summarizer import BaseSummarizer

class SummarizerClusters(BaseSummarizer):
    def __init__(self, movies_path):
        super().__init__(movies_path)
    
    def summarize(self, movie_id:int, n_clusters: int) -> list:

        movie_dir = self._movies_path + "{0}".format(movie_id)

        centroid = np.load(movie_dir + "/centroid.npy")

        clusters = np.load(movie_dir + "/clusters.npy")

        aspects_df = pd.read_csv(movie_dir + "/aspects.csv")

        sentences_df = pd.read_csv(movie_dir + "/filtered_sentences.csv")
        
        sentences_df['embeddings'] = pd.read_csv(movie_dir + "/embeddings_sentences.csv").values.tolist()

        sentences_df['score'] = 0.0
        
        for i, row in sentences_df.iterrows():
            score = self.__cosine_similarity(centroid, sentences_df['embeddings'][i])
            sentences_df.at[i, 'score'] = score

        sentences_df.sort_values(by=['score'], ascending=False, inplace=True)

        summary = self.__sentence_selection(sentences_df, 0.9, 5, self.__cuttree(aspects_df, n_clusters, clusters))
        
        return [sentence[0] for sentence in summary] 
        
    def __sentence_selection(self, sorted_sentences_by_score, discard_threshold, number_of_sentences_in_summary, aspects):
        
        
        sorted_sentences_by_score = sorted_sentences_by_score.values.tolist()
        sentences_in_summary = [sorted_sentences_by_score[0]]        
        number_chosen_sentences = len(sentences_in_summary)

        for candidate_sentence in sorted_sentences_by_score[1:]:

            discard = False
            
            for chosen_sentence in sentences_in_summary:

                current_score = self.__cosine_similarity(candidate_sentence[2], chosen_sentence[2])
                
                if current_score >= discard_threshold:
                    discard = True
                    break


            if not discard:

                for a in aspects:
                    if a in candidate_sentence[0].lower():
                        sentences_in_summary.append(candidate_sentence)
                        number_chosen_sentences += 1
                        break

                if number_chosen_sentences >= number_of_sentences_in_summary:
                    return sentences_in_summary

        return sentences_in_summary
    
    def __cuttree(self, aspects_df: pd.DataFrame, n_clusters: int, clusters: np.ndarray) -> list:
        
        aspects_df['cluster'] =  np.squeeze(cluster.hierarchy.cut_tree(clusters, n_clusters=n_clusters))

        r = []
        for i in range(0, n_clusters):
            idxmax = aspects_df[aspects_df['cluster'] == i]['frequency'].idxmax()
            r.append(aspects_df.loc[idxmax]['aspect'])

        return r
    
    def __cosine_similarity(self, centroid_embbeding, sentence_embbeding):

        centroid_norm = np.linalg.norm(centroid_embbeding, ord= 2)
        sentence_embbeding_norm = np.linalg.norm(sentence_embbeding, ord= 2)

        if centroid_norm == 0 or sentence_embbeding_norm == 0:
            return np.nan

        dot_product_embbedings = np.dot(centroid_embbeding, sentence_embbeding)
        cosine_denominator = centroid_norm * sentence_embbeding_norm
        cosine_similarity = dot_product_embbedings / cosine_denominator

        return cosine_similarity