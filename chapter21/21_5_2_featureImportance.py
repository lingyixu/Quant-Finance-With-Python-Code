# sklearn: logistic regression
from sklearn.linear_model import LogisticRegression
model = LogisticRegression()
model.fit(X_train, y_train)
score = model.coef_[0]

# sklearn: decision tree
from sklearn.tree import DecisionTreeClassifier
model = DecisionTreeClassifier()
model.fit(X_train, y_train)
score = model.feature_importances_

# SHAP: XGBoost
import shap  # remember to install shap first
from xgboost import XGBRegressor
model = XGBRegressor()
model.fit(X_train, y_train)
explainer = shap.Explainer(model)
score = explainer(X_train)

# Grad-CAM: neural network
from keras.applications.vgg16 import VGG16, preprocess_input
from keras import backend as K
model = VGG16(weights='imagenet', input_shape=(224, 224, 3))
preds = model.predict(preprocess_input(x))  # x is an image in the format of numpy array
label_ind = np.argmax(preds[0])

output = model.output[:, label_ind]
last_conv_layer = model.get_layer('block5_conv3')
grads = K.gradients(output, last_conv_layer.output)[0]
pooled_grads = K.mean(grads, axis=(0, 1, 2))
iterate = K.function([model.input], [pooled_grads, last_conv_layer.output[0]])
pooled_grads_value, conv_layer_output_value = iterate([x])
for i in range(512):
    conv_layer_output_value[:, :, i] *= pooled_grads_value[i]
heatmap = np.mean(conv_layer_output_value, axis=-1)

heatmap = np.maximum(heatmap, 0)
heatmap /= np.max(heatmap)
plt.matshow(heatmap)
plt.show()