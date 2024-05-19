import numpy as np
import pandas as pd
import re
from sklearn.base import BaseEstimator, TransformerMixin
from sklearn.preprocessing import StandardScaler
from sklearn.pipeline import Pipeline
from sklearn.model_selection import train_test_split, cross_val_score, GridSearchCV
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score, classification_report
import pickle

# Set random seed for reproducibility
np.random.seed(42)

# Number of samples
n_samples = 100000

# Generate synthetic data
pressure = np.random.uniform(2, 4, n_samples)  # Pressure in bar
et_time = np.random.uniform(10, 20, n_samples)  # ET time in seconds
t_time = np.random.uniform(10, 20, n_samples)  # T time in seconds

# Generate other parts of the string format
codes = ["C01", "P02", "SDP"]

# Define acceptance criteria
def is_accepted(pressure, et_time, t_time):
    if pressure > 2.5 and et_time <= 18 and t_time <= 15:
        return "Accepted"
    else:
        return "Rejected"

# Apply criteria to generate acceptance column
acceptance = np.array([is_accepted(p, e, t) for p, e, t in zip(pressure, et_time, t_time)])

# Generate final formatted data
data = []
for i in range(n_samples):
    row = f"EE53035    S    {codes[0]},{codes[1]},{codes[2]},ET {et_time[i]:.2f} sec,T {t_time[i]:.2f} sec,P {pressure[i]:.6f} bar"
    data.append(row)

# Create a DataFrame
df = pd.DataFrame({
    'Data': data,
    'Acceptance': acceptance
})

# Save the synthetic data to a CSV file
df.to_csv('synthetic_cts_leak_test_data.csv', index=False)

# Custom transformer for feature extraction
class FeatureExtractor(BaseEstimator, TransformerMixin):
    def fit(self, X, y=None):
        return self
    
    def transform(self, X, y=None):
        def extract_features(data):
            pattern = r"ET (\d+\.\d+) sec,T (\d+\.\d+) sec,P (\d+\.\d+) bar"
            match = re.search(pattern, data)
            if match:
                return [float(match.group(1)), float(match.group(2)), float(match.group(3))]
            else:
                return [None, None, None]
        
        features = X.apply(extract_features)
        return pd.DataFrame(features.tolist(), columns=['ET_Time', 'T_Time', 'Pressure'])

# Define the pipeline
pipeline = Pipeline([
    ('feature_extractor', FeatureExtractor()),
    ('scaler', StandardScaler())
])

# Fit and transform the data using the pipeline
processed_data = pipeline.fit_transform(df['Data'])

# Convert the processed data back to DataFrame
processed_df = pd.DataFrame(processed_data, columns=['ET_Time', 'T_Time', 'Pressure'])

# Convert the acceptance label to binary (1 for Accepted, 0 for Rejected)
processed_df['Acceptance'] = df['Acceptance'].apply(lambda x: 1 if x == "Accepted" else 0)

# Split the data into features and target
X = processed_df[['ET_Time', 'T_Time', 'Pressure']]
y = processed_df['Acceptance']

# Split the data into training, validation, and test sets
X_train, X_temp, y_train, y_temp = train_test_split(X, y, test_size=0.3, random_state=42)
X_val, X_test, y_val, y_test = train_test_split(X_temp, y_temp, test_size=0.5, random_state=42)

# Perform cross-validation to get a better estimate of the model's performance
clf = RandomForestClassifier(random_state=42)
cross_val_scores = cross_val_score(clf, X_train, y_train, cv=5)
print(f'Cross-Validation Scores: {cross_val_scores}')
print(f'Average Cross-Validation Score: {np.mean(cross_val_scores):.4f}')

# Hyperparameter tuning using GridSearchCV
param_grid = {
    'n_estimators': [50, 100, 200],
    'max_features': ['auto', 'sqrt', 'log2'],
    'max_depth': [None, 10, 20, 30],
    'criterion': ['gini', 'entropy']
}

grid_search = GridSearchCV(RandomForestClassifier(random_state=42), param_grid, cv=5, scoring='accuracy')
grid_search.fit(X_train, y_train)

print(f'Best Parameters: {grid_search.best_params_}')
best_clf = grid_search.best_estimator_

# Evaluate the best model on the validation set
y_val_pred = best_clf.predict(X_val)
val_accuracy = accuracy_score(y_val, y_val_pred)
print(f'Validation Accuracy: {val_accuracy:.4f}')
print('Validation Classification Report:')
print(classification_report(y_val, y_val_pred))

# Final evaluation on the test set
y_test_pred = best_clf.predict(X_test)
test_accuracy = accuracy_score(y_test, y_test_pred)
print(f'Test Accuracy: {test_accuracy:.4f}')
print('Test Classification Report:')
print(classification_report(y_test, y_test_pred))

# Save the best model if it meets a certain accuracy threshold
accuracy_threshold = 0.85  # Define an appropriate threshold based on your requirements
if test_accuracy >= accuracy_threshold:
    with open('trained_model1.pkl', 'wb') as file:
        pickle.dump(best_clf, file)
    print('Model saved as trained_model.pkl')

# Save the scaler
with open('scaler.pkl', 'wb') as file:
    pickle.dump(pipeline.named_steps['scaler'], file)
