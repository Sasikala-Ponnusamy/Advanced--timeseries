from src.data_loader import load_data
from src.preprocessing import preprocess
from src.train import train_model
from src.evaluate import evaluate
from src.explainability import explain

df = load_data("data/store_sales.csv")
X, y, scaler = preprocess(df)

split = int(len(X) * 0.8)
X_train, X_test = X[:split], X[split:]
y_train, y_test = y[:split], y[split:]

model = train_model(X_train, y_train)
y_pred = model.predict(X_test)

rmse, mape = evaluate(y_test, y_pred)
print("RMSE:", rmse)
print("MAPE:", mape)

explain(model, X_train, X_test)
