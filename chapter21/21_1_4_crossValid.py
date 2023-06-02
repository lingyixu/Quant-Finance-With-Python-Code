from sklearn import datasets, linear_model
from sklearn.model_selection import cross_validate

diabetes = datasets.load_diabetes()
X = diabetes.data[:150]
y = diabetes.target[:150]

alpha_list = [0.0, 0.1, 0.2, 0.5, 1.0]
score_list = []

for alpha in alpha_list:
    model = linear_model.Lasso(alpha=alpha)
    cv_results = cross_validate(model, X, y, cv=5)
    score = cv_results['test_score'].mean()
    score_list.append(score)

opt_idx = np.argmax(score_list)
print('best model parameter: alpha={}'.format(alpha_list[opt_idx]))