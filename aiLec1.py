#%%
import pandas as pd
data = pd.read_csv("salary_dataset.csv")
data.head()
# %%
data.info()
# %%
data.duplicated().sum()
# %%
from sklearn.linear_model import LinearRegression
data_x =data["YearsExperience"].values
data_x = data_x.reshape(-1,1)
data_y =data["Salary"].values
model = LinearRegression()
model.fit(data_x ,data_y)


# %%
model.predict([[3.2]])
# %%
model.score(data_x,data_y)
# %%
