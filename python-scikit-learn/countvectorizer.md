# Countvectorizer

```python
from sklearn import feature_extraction

docs = [
  'Programming languahe is python.',
  'Programming in python and javascript is good.',
  'Programming also in lua as well as javaascripipt is ok.',
  'Programming in no language is bad',
]

cv = feature_extraction.text.CountVectorizer()
X = cv.fit_transform(docs)

words = cv.get_feature_names_out()
vectors = X.toarray()
```

- `from sklearn import` - import module from [lib:scikit-learn](https://onelinerhub.com/python-scikit-learn/how-to-install-scikit-learn-using-pip)
- `docs = [` - sample set of text docs to vectorize
- `.CountVectorizer(` - creates count vectorizer which creates vectors based on words counts
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

cv = feature_extraction.text.CountVectorizer()
X = cv.fit_transform(docs)

print(cv.get_feature_names_out())
print(X.toarray())
```
```
['also' 'and' 'as' 'bad' 'good' 'in' 'is' 'javaascripipt' 'javascript'
 'language' 'languahe' 'lua' 'no' 'ok' 'programming' 'python' 'well']
[[0 0 0 0 0 0 1 0 0 0 1 0 0 0 1 1 0]
 [0 1 0 0 1 1 1 0 1 0 0 0 0 0 1 1 0]
 [1 0 2 0 0 1 1 1 0 0 0 1 0 1 1 0 1]
 [0 0 0 1 0 1 1 0 0 1 0 0 1 0 1 0 0]]

```

