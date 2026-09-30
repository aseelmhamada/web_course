#%%
import pandas as pd
data = pd.read_csv("train-selected-columns.csv")
data.head()
# %%
data.info()
# %%
object_data = data.select_dtypes(include="object")
object_data.isnull().sum()
# %%
object_data = object_data.fillna(object_data.mode().loc[0])
object_data.info()
# %%
numerical_data = data.select_dtypes(exclude="object")
numerical_data = numerical_data.fillna(numerical_data.median())
numerical_data.info()
# %%
new_data =pd.concat([numerical_data ,object_data],axis = 1)
new_data.info()
# %%
new_data.duplicated().sum()
new_data = new_data.drop_duplicates()
# %%
new_data.head()
# %%
new_data = new_data.drop(["PassengerId" , "Fare", "Name" , "Ticket" ], axis = 1)
new_data.info()
# %%
new_data.head()
# %%
from sklearn.preprocessing import LabelEncoder
gender_encode = LabelEncoder()
Parch_encode = LabelEncoder()
Age_encode = LabelEncoder()
new_data["Sex"] = gender_encode.fit_transform(new_data["Sex"])
new_data["Parch"] =Parch_encode.fit_transform(new_data["Parch"])
new_data["Age"] = Age_encode.fit_transform(new_data["Age"])
new_data.head()

# %%
Parch_encode.classes_
# %%
from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import train_test_split
x_data = new_data.drop("Survived",axis=1)
y_data = new_data["Survived"]
model = RandomForestClassifier(n_estimators=150)
x_train , x_test , y_train ,y_test= train_test_split(x_data, y_data ,test_size=0.2 , random_state=42)
model.fit(x_train , y_train)
model.predict(x_test)

# %%
model.score(x_train , y_train)
# %%
new_item =pd.DataFrame([[ 3 , 32 , 0 , 0 , 1 ]],
columns= x_data.columns)
prediction= model.predict(new_item)
if prediction[0]==0:
    print("Not Survived  ")
else:
    print("Survived")