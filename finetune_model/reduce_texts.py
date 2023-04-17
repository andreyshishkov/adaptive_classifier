from nltk import word_tokenize


def reduce_texts(texts, max_length):
    preprocessed_texts = []
    for text in texts:
        tokens = word_tokenize(text)
        tokens = tokens[:max_length]
        preprocessed_text = ' '.join(tokens)
        preprocessed_texts.append(preprocessed_text)
    return preprocessed_texts
