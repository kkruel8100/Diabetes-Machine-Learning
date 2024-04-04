# Import dependencies
import numpy as np
import matplotlib.pyplot as plt
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.model_selection import RandomizedSearchCV
from sklearn.linear_model import LinearRegression
from sklearn.neighbors import KNeighborsClassifier
from sklearn.linear_model import LogisticRegression
from sklearn.svm import SVC
from sklearn.tree import DecisionTreeClassifier
from sklearn.ensemble import RandomForestClassifier
from sklearn.ensemble import ExtraTreesClassifier
from sklearn.ensemble import AdaBoostClassifier
from xgboost import XGBClassifier
from sklearn.metrics import classification_report, confusion_matrix, accuracy_score
import warnings
warnings.filterwarnings("ignore")
warnings.simplefilter(action="ignore", category=FutureWarning)

# Establish target names
target_names = ["negative", "positive"]

# Create hypertuning parameter grids for each model that will be hypertuned
param_grid_lr = {
    "max_iter": [100, 200, 300, 400, 500],
    "solver": ["lbfgs", "liblinear", "sag", "saga"],
    "C": np.arange(1, 500),
}

param_grid_adaboost = {
    "n_estimators": [50, 100, 200, 300, 400, 500],
    "learning_rate": np.arange(1, 500),
}

param_grid_xgboost = {
    "n_estimators": [50, 100, 200, 300, 400, 500],
    "max_depth": np.arange(1, 5),
    "max_leaves": np.arange(1, 5),
    "min_child_weight": np.arange(1, 5),
    "subsample": np.arange(0.1, 1, 0.1),
}

# Create model function
def test_model(model, data):
    X_train_scaled, X_test_scaled, y_train, y_test = data
    reg = model.fit(X_train_scaled, y_train)
    reg_pred = reg.predict(X_test_scaled)
    print(f"Untuned Model: {type(reg).__name__}")
    print(f"Train Accuracy: {reg.score(X_train_scaled, y_train)}")
    print(f"Test Accuracy: {reg.score(X_test_scaled, y_test)}\n")


#  Create a hypertuning function
def hypertune_model(model, data, param_grid):
    # establish X and y
    X_train_scaled, X_test_scaled, y_train, y_test = data
    # establish param
    param_grid = param_grid
    random_clf = RandomizedSearchCV(model, param_grid, random_state=42, verbose=3)
    random_clf.fit(X_train_scaled, y_train)
    random_tuned_pred = random_clf.predict(X_test_scaled)
    random_clf.best_estimator_
    print(f"Tuned Model: {model}")
    print(f"Best parameters: {random_clf.best_params_}")
    print(classification_report(y_test, random_tuned_pred, target_names=target_names))
    print(f"Train Accuracy: {random_clf.score(X_train_scaled, y_train)}")
    print(f"Test Accuracy: {random_clf.score(X_test_scaled, y_test)}\n")
    plt.show()


#  Creare a pipeline function
def run_pipeline(df):
    # Step Define x and y
    # Create X and y variables
    X = df.drop(columns=["Diabetes_binary"])
    y = df["Diabetes_binary"]

    # Step Split the data
    X_train, X_test, y_train, y_test = train_test_split(X, y, random_state=42)

    # Step Standard scaler
    scaler = StandardScaler().fit(X_train)
    X_train_scaled = scaler.transform(X_train)
    X_test_scaled = scaler.transform(X_test)
    data = [X_train_scaled, X_test_scaled, y_train, y_test]

    # Set random state
    random_state = 42

    test_models = [
        # SVC(C=1.0, random_state=random_state),
        LinearRegression(),
        KNeighborsClassifier(),
        LogisticRegression(random_state=random_state),
        DecisionTreeClassifier(random_state=random_state),
        RandomForestClassifier(random_state=random_state),
        ExtraTreesClassifier(random_state=random_state),
        AdaBoostClassifier(random_state=random_state),
        XGBClassifier(),
    ]

    #  Run the models and get a report per model
    for model in test_models:
        test_model(model, data)

    #  Hypertune the models and print reports and scores
    hypertune_model(LogisticRegression(), data, param_grid_lr)
    hypertune_model(AdaBoostClassifier(), data, param_grid_adaboost)
    hypertune_model(XGBClassifier(), data, param_grid_xgboost)

