import pandas as pd
import numpy as np
phoneDataSet = {
    'Phone': ['iPhone 5', 'iPhone 6', 'iPhone8', 'Galaxy S9', 'Galaxy Note 10'],
    'Phone ID.': [12, 9, np.nan, 78, 1, np.nan],
    'Phone Price': [204, np.nan, 501, 800, np.nan],
}
data = pd.DataFrame(phoneDataSet)
data = data.replace(np.nan, 0)
print(data)
