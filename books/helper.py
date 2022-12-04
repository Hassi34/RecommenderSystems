
import pandas as pd
from pickle import bytes_types
import numpy as np
from books.loader import load_artifacts

class Helper:
    def __init__(self):
        (self.model, self.books_name, self.final_ratings, self.books_pivot) = load_artifacts()

    def fetch_predictions(self, selected_book: str) -> list[dict]:
        self.recommend_books(selected_book)
        self.predictions = self.final_ratings[self.final_ratings['title'].isin(self.books)][['title', 'image_url']].\
                            drop_duplicates(subset='title', keep='first').to_dict('records')
        for movie in self.predictions:
            if movie['title'] == selected_book:
                self.predictions.remove(movie)
        return self.predictions

    def recommend_books(self, selected_book: str) -> list[str]:
        book_id = np.where(self.books_pivot.index == selected_book)[0][0]
        distance , suggestions = self.model.kneighbors(self.books_pivot.iloc[book_id, :].values.reshape(1, -1),
                                                    n_neighbors=12)
        self.books = self.books_pivot.index[suggestions[0]]
        
        return self.books

