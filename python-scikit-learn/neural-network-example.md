# Neural network example

```python
from sklearn import neural_network

X = [[0., 0.], [1., 1.]]
y = [0, 1]

nn = neural_network.MLPClassifier(solver='lbfgs')
nn.fit(X, y)

y_pred = nn.predict(X)
```

- `from sklearn import` - import module from [lib:scikit-learn](https://onelinerhub.com/python-scikit-learn/how-to-install-scikit-learn-using-pip)
- `.MLPClassifier(` - creates multi-layer perceptron neural network model
- `.fit(` - train transformation model
- `.predict(` - predict target variable based on given features dataset

group: neural

## Example: 
```python
from sklearn import neural_network
X = [[0., 0.], [1., 1.]]
y = [0, 1]
nn = neural_network.MLPClassifier(solver='lbfgs')
nn.fit(X, y)

print(nn.predict(X))
```
```
[0 1]

```

