import os
from collections import Counter
import MeCab  # mecab-python3 기반

def load_stopwords():
    current_dir = os.path.dirname(os.path.abspath(__file__))
    stopword_path = os.path.join(current_dir, "data", "stopwords.txt")
    with open(stopword_path, 'r', encoding='utf-8') as f:
        return set(f.read().splitlines())

def extract_keywords(text, stopwords):
    tagger = MeCab.Tagger("-Owakati")  # 단어 단위로만 자르기 (POS 없이)
    words = tagger.parse(text).strip().split()
    keywords = [word for word in words if word not in stopwords and len(word) > 1]
    return keywords

def get_top_keywords(reviews, top_n=20):
    stopwords = load_stopwords()
    all_keywords = []
    for review in reviews:
        all_keywords.extend(extract_keywords(review, stopwords))
    counter = Counter(all_keywords)
    return [{"keyword": word, "count": count} for word, count in counter.most_common(top_n)]