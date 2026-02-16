import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score

data = pd.read_csv("data.csv")

X = data[["hours", "attendance", "previous_marks", "assignment_score"]]
y = data["result"]
X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42
)

model = LogisticRegression(max_iter=1000)
model.fit(X_train, y_train)
y_pred = model.predict(X_test)
accuracy = accuracy_score(y_test, y_pred)
def predict_result(hours, attendance, previous_marks, assignment_score):
    prediction = model.predict([[hours, attendance, previous_marks, assignment_score]])
    probability = model.predict_proba([[hours, attendance, previous_marks, assignment_score]])
    return prediction[0], probability
