# Cosine similarity

```python
from sklearn import metrics
cs = metrics.pairwise.cosine_similarity([[1, 2], [4, 5], [7, 19]])
```

- `from sklearn import` - import module from [lib:scikit-learn](https://onelinerhub.com/python-scikit-learn/how-to-install-scikit-learn-using-pip)
- `.cosine_similarity(` - calculate cosine similarity (L2-normalized dot product of vectors)

## Example: 
```python
from sklearn import metrics

cs = metrics.pairwise.cosine_similarity([[1, 2], [4, 5], [7, 19]])
print(cs)
```
```
[[1.         0.97780241 0.99388373]
 [0.97780241 1.         0.9486833 ]
 [0.99388373 0.9486833  1.        ]]

```

