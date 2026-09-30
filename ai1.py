#%%
import numpy as np
#هنا استدعيت مكتبة السكيتليرن و عشان عندي قيمة مقابل قيمة اخترنا لينير
from sklearn.linear_model import LinearRegression
x_data = np.array([[50],[100],[150],[250],[400]])
y_data = np.array([150,350,550,950,1200])

# %%
#بدي ادرب المودل على هادي داتا
model = LinearRegression()
dir(model)
# %%odel.fit(x_data,
model.fit(x_data, y_data)
# %%
model.predict([[600]])
# %%
model.score(x_data ,y_data)
# %%
 