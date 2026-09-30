#%%
from sklearn.datasets import load_iris
from sklearn.cluster import KMeans
import matplotlib.pyplot as plt
import pandas as pd
iris = load_iris()
data = iris.data
df = pd.DataFrame(data , columns=iris.feature_names)

df.head()
# %%
df.info()
# %%
arr = []
for i in range (1,11):
    means= KMeans(n_clusters=i)
    data_train = means.fit(data)
    arr.append(data_train.inertia_)
plt.plot(range(1,11) , arr , c="blue" , marker="*" )
plt.show()
# %%
