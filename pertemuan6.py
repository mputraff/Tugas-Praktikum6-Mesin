# %% [1]
# Import library
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

from sklearn.model_selection import train_test_split
from sklearn.tree import DecisionTreeClassifier
from sklearn.metrics import classification_report, confusion_matrix
from sklearn import tree

# %% [2]
# Load dataset
df = pd.read_csv('company_esg_financial_dataset.csv')
print("5 data pertama:")
print(df.head())

# %% [3]
# Tampilkan nama kolom
print("\nDaftar kolom dalam dataset:")
for col in df.columns:
    print(f"- '{col}'")

# %% [4]
# Hapus kolom identitas perusahaan
df = df.drop(columns=['CompanyID', 'CompanyName'])

# %% [5]
# Buat kolom ESG_Category dari ESG_Overall
def categorize_esg(score):
    if score >= 70:
        return 'High'
    elif score >= 50:
        return 'Medium'
    else:
        return 'Low'

df['ESG_Category'] = df['ESG_Overall'].apply(categorize_esg)

# %% [6]
# Tangani missing values
df = df.dropna()

# %% [7]
# Ubah kolom kategorikal ke numerik (one-hot encoding)
df = pd.get_dummies(df, columns=['Industry', 'Region'])

# %% [8]
# Pisahkan fitur dan target
target_column = 'ESG_Category'
x = df.drop(columns=[target_column])
y = df[target_column]

# %% [8.1]
# Split data training dan testing
x_train, x_test, y_train, y_test = train_test_split(x, y, test_size=0.3, random_state=10)

# %% [9]
# Decision Tree Classifier
model = DecisionTreeClassifier(criterion='entropy')
model.fit(x_train, y_train)
y_pred = model.predict(x_test)

# %% [10]
# Classification Report
print("\nClassification Report:")
print(classification_report(y_test, y_pred))

# %% [11]
# Confusion Matrix
cm = confusion_matrix(y_test, y_pred)
fig, ax = plt.subplots(figsize=(7, 7))

sns.set(font_scale=1.4)
sns.heatmap(cm, ax=ax, annot=True, annot_kws={"size": 16}, cmap='Blues')

plt.xlabel('Predictions', fontsize=18)
plt.ylabel('Actuals', fontsize=18)
plt.title('Confusion Matrix', fontsize=18)
plt.show()

# %% [12]
# Visualisasi Decision Tree
fig, ax = plt.subplots(figsize=(25, 20))
tree.plot_tree(model, feature_names=x.columns, class_names=model.classes_, filled=True)
plt.show()

# %% [13]
# Contoh prediksi manual
# Buat satu dummy row dari template kolom x
example_data = x.iloc[0].copy()

# Update nilai beberapa kolom numerik secara manual
example_data.update({
    'Year': 2022,
    'Revenue': 5000000,
    'ProfitMargin': 10.0,
    'MarketCap': 2000000,
    'GrowthRate': 15.0,
    'ESG_Overall': 85.0,
    'ESG_Environmental': 80.0,
    'ESG_Social': 70.0,
    'ESG_Governance': 75.0,
    'CarbonEmissions': 35000.0,
    'WaterUsage': 20000.0,
    'EnergyConsumption': 70000.0,
})

# Pastikan semua kolom one-hot tetap terisi
prediction_input_df = pd.DataFrame([example_data])
prediction = model.predict(prediction_input_df)
print("Prediksi untuk data baru:", prediction[0])
