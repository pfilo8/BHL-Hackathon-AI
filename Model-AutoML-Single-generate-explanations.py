import os
import pandas as pd
import numpy as np
import shap
import joblib
import matplotlib.pyplot as plt
from sklearn.model_selection import train_test_split


def generate_shap_values(model, x, i):
    med = x.median().values.reshape((1, x.shape[1]))
    shap_model = shap.KernelExplainer(model.predict_proba, med, )
    shap_values = shap_model.shap_values(x.iloc[:i, :], )
    return shap_model, shap_values


RANDOM_STATE = 42
EXPLAIN_OBSERVATION_NO = 100
EXPLAIN_TRAJECTORIES_NO = 30

DATA_PATH = os.path.join('data', 'final_train.csv')

model = joblib.load(os.path.join('results', 'automl-single-model-2021-28-09-21-28-03', 'model.joblib'))

df = pd.read_csv(DATA_PATH, index_col=0)
x, y = df.drop(columns=['Activity']), df['Activity']
y_ = y.astype('category').cat.codes
x_train, x_test, y_train, y_test = train_test_split(x, y, random_state=RANDOM_STATE)

shap_model, shap_values = generate_shap_values(model, x, EXPLAIN_OBSERVATION_NO)
base_value = shap_model.expected_value

fig, axs = plt.subplots(6, 1)
for i in range(6):
    plt.sca(axs[i])
    shap.summary_plot(shap_values[i], x.values[:EXPLAIN_OBSERVATION_NO, :], x.columns, plot_type='dot', show=False)
    plt.gca().set_title(f"Activity type: {model.classes_[i]}")
fig.set_size_inches(9, 30)
fig.tight_layout()
plt.savefig(os.path.join('reports', 'explain', 'SHAP-dot.png'))

plt.figure()
shap.summary_plot(shap_values, x.columns, plot_type='bar', class_names=list(model.classes_), show=False)
plt.title('SHAP Feature Importance', size=24)
plt.tight_layout()
plt.savefig(os.path.join('reports', 'explain', 'SHAP-FI-all.png'))
plt.show()

for i in range(6):
    plt.figure()
    shap.summary_plot(shap_values[i], x.columns, plot_type='bar', show=False)
    plt.title(f"Activity type: {model.classes_[i]}")
    plt.tight_layout()
    plt.savefig(os.path.join('reports', 'explain', f'{model.classes_[i]}.png'), dpi=400)
    plt.show()

for j in range(6):
    if not os.path.exists(os.path.join('reports', 'explain', 'dependence', f'{model.classes_[j]}')):
        os.mkdir(os.path.join('reports', 'explain', 'dependence', f'{model.classes_[j]}'))
    important_features = np.argsort(np.abs(shap_values[j]).mean(0))[-10:][::-1]
    for i, feature in enumerate(important_features):
        shap.dependence_plot(feature, shap_values[j], x.iloc[:EXPLAIN_OBSERVATION_NO, :], show=False)
        plt.title(f'SHAP dependece {x.columns[feature]}', size=18)
        plt.tight_layout()
        plt.savefig(os.path.join('reports', 'explain', 'dependence', f'{model.classes_[j]}',
                                 f'SHAP-dependence{x.columns[feature]}.png'), dpi=300)
        plt.show()

y_pred_all = model.predict(x)
for row_index in range(EXPLAIN_TRAJECTORIES_NO):
    plt.figure()
    shap.multioutput_decision_plot(list(base_value), shap_values,
                                   row_index=row_index,
                                   feature_names=list(x.columns),
                                   legend_labels=list(model.classes_),
                                   legend_location='upper left', show=False
                                   )
    fig.set_size_inches(6, 8)
    plt.title(f"Real class: {y[row_index]}, Pred class: {y_pred_all[row_index]}")
    plt.tight_layout()
    plt.savefig(os.path.join('reports', 'explain', 'decision-plot', f'SHAP-decision{row_index}.png'), dpi=300)
    plt.show()
