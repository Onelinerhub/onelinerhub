# How do I use Python and Keras to perform binary classification?
// plain

Using Python and Keras to perform binary classification consists of the following steps:

1. Import the necessary packages.
```
import numpy as np
import pandas as pd
from keras.models import Sequential
from keras.layers import Dense
from keras.wrappers.scikit_learn import KerasClassifier
```

2. Load the data and preprocess it.
```
#load data
dataset = pd.read_csv('data.csv')

#split into input (X) and output (Y) variables
X = dataset.iloc[:,0:8].values
Y = dataset.iloc[:,8].values
```

3. Define the model.
```
#define the keras model
def create_model():
    #create model
    model = Sequential()
    model.add(Dense(12, input_dim=8, activation='relu'))
    model.add(Dense(8, activation='relu'))
    model.add(Dense(1, activation='sigmoid'))

    #compile model
    model.compile(loss='binary_crossentropy', optimizer='adam', metrics=['accuracy'])
    return model
```

4. Create the model.
```
model = create_model()
```

5. Fit the model to the data.
```
model.fit(X, Y, epochs=150, batch_size=10)
```

6. Evaluate the model.
```
scores = model.evaluate(X, Y)
print("\n%s: %.2f%%" % (model.metrics_names[1], scores[1]*100))
```

7. Make predictions.
```
predictions = model.predict(X)
rounded = [round(x[0]) for x in predictions]
print(rounded)
```

## Output example

```
accuracy: 85.25%
[0.0, 1.0, 0.0, 1.0, 0.0, 0.0, 1.0, 1.0, 1.0, 0.0]
```

## Helpful links
- [Keras Documentation](https://keras.io/)
- [Using Keras for Binary Classification](https://machinelearningmastery.com/binary-classification-tutorial-with-the-keras-deep-learning-library/)

onelinerhub: [How do I use Python and Keras to perform binary classification?](https://onelinerhub.com/python-keras/how-do-i-use-python-and-keras-to-perform-binary-classification)