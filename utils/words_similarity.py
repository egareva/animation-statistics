from nltk.util import ngrams


def jaccard_similarity(word1: str, word2: str, n: int = 2) -> float:
    """ Функция схожести двух строк по n-граммам """
    word1_bigrams = list(ngrams(word1, n))
    word2_bigrams = list(ngrams(word2, n))

    intersection = len(list(set(word1_bigrams).intersection(set(word2_bigrams))))
    union = (len(set(word1_bigrams)) + len(set(word2_bigrams))) - intersection

    return float(intersection) / union
