import numpy as np


def encode(sentence, dim=500):
    """This function mimics encoding a sentence into a n-dimensional embedding.
    In a real case scenario encoding could be done using something like 
    sentence_transformers: https://www.sbert.net/index.html
    """
    return np.random.rand(dim).tolist()
