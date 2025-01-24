import numpy as np
import pandas as pd
import matplotlib.pyplot as plot
import seaborn as sns

data = [10,12,14,13,100,15,16,14,13]
Q1 = np.percentile(data,25)
Q2 = np.percentile(data,75)
IQR = Q2 - Q1
lower_bound = Q1 - 1.5 * IQR
upper_bound = Q2 + 1.5 * IQR
outliers = [x for x in data if x < lower_bound or x > upper_bound]
# Output the results
print (f"Q1 (25th percentile): {Q1}")
print(f"Q2 (75th percentile) : {Q2}")
print (f"IQR: {IQR}")
print(f"Lower Bound: {lower_bound }")
print(f"Upper Bound: {upper_bound}")
print(f"Outliers: {outliers}")
plot.plot(data)
plot.show()

#_-----------------------------_

import numpy as np
import pandas as pd

np.random.seed(10)
data = pd.DataFrame({
    'value': np.concatenate([np.random.normal(0, 1, 100), np.random.normal(0, 1, 10)])
})
Q1 = data['value'].quantile(0.25)
Q3 = data['value'].quantile(0.75)
IQR = Q3 - Q1
lower_bound = Q1 - 1.5 * IQR
upper_bound = Q3 + 1.5 * IQR

outliers = [x for x in data['value'] if x < lower_bound or x > upper_bound]

print(f"Q1 (25th percentile): {Q1}")
print(f"Q3 (75th percentile): {Q3}")
print(f"IQR: {IQR}")
print(f"Lower Bound: {lower_bound}")
print(f"Upper Bound: {upper_bound}")
print(f"Outliers: {outliers}")
