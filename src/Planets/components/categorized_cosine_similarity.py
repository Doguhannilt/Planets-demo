from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity
import pandas as pd

class CosineSimilarityCalculator:

    def cosine_similarity(self, tfidf_matrix):
        return cosine_similarity(tfidf_matrix, tfidf_matrix)

    def group_similar_values(self, y, similarity_threshold=0.2):
        tfidf_vectorizer = TfidfVectorizer()
        tfidf_matrix = tfidf_vectorizer.fit_transform(y)

        cosine_sim = self.cosine_similarity(tfidf_matrix)

        assigned_numbers = {}
        number_counter = 1

        for i in range(len(y)):
            if i not in assigned_numbers:
                assigned_numbers[i] = number_counter
                number_counter += 1
            for j in range(i+1, len(y)):
                if cosine_sim[i][j] >= similarity_threshold:
                    assigned_numbers[j] = assigned_numbers[i]

        
        groups = {}
        for key, value in assigned_numbers.items():
            if value not in groups:
                groups[value] = []
            groups[value].append(y[key])

        result_df = pd.DataFrame({'Group': list(groups.keys()), 'Values': list(groups.values())})

        return result_df

