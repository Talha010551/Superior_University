import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import LabelEncoder
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score

train = pd.read_csv("train.csv")
test = pd.read_csv("test.csv")

print("Train shape:", train.shape)
print("Test shape:", test.shape)
print(train.head())

train.fillna({"HomePlanet":"Unknown", "Destination":"Unknown", "CryoSleep":False, "VIP":False, "Age":train["Age"].median()}, inplace=True)
test.fillna({"HomePlanet":"Unknown", "Destination":"Unknown", "CryoSleep":False, "VIP":False, "Age":test["Age"].median()}, inplace=True)

spending_cols = ["RoomService","FoodCourt","ShoppingMall","Spa","VRDeck"]
for col in spending_cols:
    train[col].fillna(0, inplace=True)
    test[col] = test[col].fillna(0)

train["TotalSpend"] = train[spending_cols].sum(axis=1)
test["TotalSpend"] = test[spending_cols].sum(axis=1)

cat_cols = ["HomePlanet", "Destination", "CryoSleep", "VIP"]

le = LabelEncoder()
for col in cat_cols:
    train[col] = le.fit_transform(train[col].astype(str))
    test[col] = le.transform(test[col].astype(str))

X = train[["HomePlanet","CryoSleep","Destination","Age","VIP","TotalSpend"]]
y = train["Transported"].astype(int) 

X_train, X_val, y_train, y_val = train_test_split(X, y, test_size=0.2, random_state=42)

model = RandomForestClassifier(n_estimators=200, random_state=42)
model.fit(X_train, y_train)

y_pred = model.predict(X_val)
print("Validation Accuracy:", accuracy_score(y_val, y_pred))

model.fit(X, y)
test_pred = model.predict(test[["HomePlanet","CryoSleep","Destination","Age","VIP","TotalSpend"]])

submission = pd.DataFrame({
    "PassengerId": test["PassengerId"],
    "Transported": test_pred.astype(bool)   
})
submission.to_csv("submission.csv", index=False)

print("Submission file created: submission.csv")

