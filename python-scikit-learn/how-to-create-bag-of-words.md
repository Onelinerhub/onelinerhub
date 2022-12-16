# How to create bag of words from text

### Bag of words is created based on a chosen vectorizing approach, like [`CountVectorizer`](https://onelinerhub.com/python-scikit-learn/countvectorizer) in our case:

```python
from sklearn import feature_extraction

docs = [
  'Programming languahe is python.',
  'Programming in python and javascript is good.',
  'Programming also in lua as well as javaascripipt is ok.',
  'Programming in no language is bad',
]

cv = feature_extraction.text.CountVectorizer()
bag_of_words = cv.fit_transform(docs)
```

- `from sklearn import` - import module from [lib:scikit-learn](https://onelinerhub.com/python-scikit-learn/how-to-install-scikit-learn-using-pip)
- `docs = [` - sample set of text docs to vectorize
- `.CountVectorizer(` - creates count vectorizer which creates vectors based on words counts
- `.fit_transform(` - train and process vectorizer to get vectors
- `bag_of_words` - will contain our "bag of words" list

group: vectorize

## Example: 
```python
from sklearn import feature_extraction

docs = [
  'Programming languahe is python.',
  'Programming in python and javascript is good.',
  'Programming also in lua as well as javaascripipt is ok.',
  'Programming in no language is bad',
]

cv = feature_extraction.text.CountVectorizer()
bag_of_words = cv.fit_transform(docs)

print(cv.vocabulary_)
```
```
{'programming': 14, 'languahe': 10, 'is': 6, 'python': 15, 'in': 5, 'and': 1, 'javascript': 8, 'good': 4, 'also': 0, 'lua': 11, 'as': 2, 'well': 16, 'javaascripipt': 7, 'ok': 13, 'no': 12, 'language': 9, 'bad': 3}

```

