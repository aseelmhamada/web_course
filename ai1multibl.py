#%%
import pandas as pd
from sklearn.linear_model import LinearRegression
data = pd.read_csv("fridge_price_predictor_dataset_real_brands.csv")

# %%
data.info()
# %%
data.isnull().sum().sum()
# %%
object_data = data.select_dtypes(include="object")
object_data.info()
# %%
numberical_data = data.select_dtypes(exclude="object")
numberical_data.info()

# %%
object_data = object_data.fillna(object_data.mode().loc[0])
object_data.info()
# %%
numberical_data = numberical_data.fillna(numberical_data.median())
numberical_data.info()
# %%
new_data = pd.concat([numberical_data , object_data],axis=1)
new_data.info()
# %%
new_data.duplicated().sum()
# %%
new_data.head()
# %%
from sklearn.preprocessing import LabelEncoder
le = LabelEncoder()
for col in new_data.select_dtypes(exclude="object").columns:
    new_data[col] = le.fit_transform(new_data[col])
new_data.head()
# %%
x_data = new_data.drop("price" , axis = 1)
y_data = new_data["price"].values
model = LinearRegression()
model.fit(x_data,y_data)
# %%+