from sklearn.linear_model import LinearRegression

def run_baseline_model(features):
    model = LinearRegression()
    model.fit(features.X, features.y)
    predictions = model.predict(features.X)
    return predictions