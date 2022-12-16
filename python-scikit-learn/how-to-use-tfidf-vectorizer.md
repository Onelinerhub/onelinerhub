# How to use TFIDF vectorizer

```python
from sklearn import feature_extraction

docs = [
  'Programming languahe is python.',
  'Programming in python and javascript is good.',
  'Programming also in lua as well as javaascripipt is ok.',
  'Programming in no language is bad',
]

cv = feature_extraction.text.TfidfVectorizer()
X = cv.fit_transform(docs)

words = cv.get_feature_names_out()
vectors = X.toarray()
```

- `from sklearn import` - import module from [lib:scikit-learn](https://onelinerhub.com/python-scikit-learn/how-to-install-scikit-learn-using-pip)
- `docs = [` - sample set of text docs to vectorize
- `.TfidfVectorizer(` - creates TFIDF vectorizer
- `.fit_transform(` - train and process vectorizer to get vectors
- `words` - will contain list of words used for vectors
- `vectors` - will contain final vectors

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

cv = feature_extraction.text.TfidfVectorizer()
X = cv.fit_transform(docs)

print(cv.get_feature_names_out())
print(X.toarray())
```
```
['also' 'and' 'as' 'bad' 'good' 'in' 'is' 'javaascripipt' 'javascript'
 'language' 'languahe' 'lua' 'no' 'ok' 'programming' 'python' 'well']
[[0.         0.         0.         0.         0.         0.
  0.35455723 0.         0.         0.         0.67943473 0.
  0.         0.         0.35455723 0.53567415 0.        ]
 [0.         0.46759408 0.         0.         0.46759408 0.29845925
  0.24400999 0.         0.46759408 0.         0.         0.
  0.         0.         0.24400999 0.36865655 0.        ]
 [0.3169887  0.         0.6339774  0.         0.         0.20232978
  0.16541785 0.3169887  0.         0.         0.         0.3169887
  0.         0.3169887  0.16541785 0.         0.3169887 ]
 [0.         0.         0.         0.50302425 0.         0.32107387
  0.26249892 0.         0.         0.50302425 0.         0.
  0.50302425 0.         0.26249892 0.         0.        ]]

```

