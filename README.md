# Predict schizophrenia using brain anatomy


This project was carried out as part of an exam-project of Professor [Edouard Duchesnay](https://github.com/duchesnay) 's Machine Learning material in the MoSEF Data Science Course of Paris 1 Panthéon Sorbonne.
You can find the initial repo here: https://github.com/duchesnay/brain_anatomy_schizophrenia.git
This project was was realised with [José Ángel García Sánchez 👨🏻‍💻](https://github.com/Pse1234)


Predict schizophrenia from brain grey matter (GM). schizophrenia is associated with diffuse and complex pattern of brain atrophy. We will try to learn a predictor of the clinical status (patient with schizophrenia vs. healthy control) using GM measurements on the brain participants.

## Dataset

There are 410 samples in the training set and 103 samples in the test set.

### Input data

Voxel-based_morphometry [VBM](https://en.wikipedia.org/wiki/Voxel-based_morphometry)
using [cat12](http://www.neuro.uni-jena.de/cat/) software which provides:

- Regions Of Interest (`rois`) of Grey Matter (GM) scaled for the Total
  Intracranial Volume (TIV): `[train|test]_rois.csv` 284 features.

- VBM GM 3D maps or images (`vbm3d`) of [voxels](https://en.wikipedia.org/wiki/Voxel) in the
  [MNI](https://en.wikipedia.org/wiki/Talairach_coordinates) space:
  `[train|test]_vbm.npz` contains 3D images of shapes (121, 145, 121).
  This npz contains the 3D mask and the affine transformation to MNI
  referential. Masking the brain provide *flat* 331 695 input features (voxels)
  for each participant.
  
## Running the project locally

### Installation

This starting kit requires Python and the following dependencies:

* `numpy`
* `scipy`
* `pandas`
* `scikit-learn`
* `matplolib`
* `seaborn`
* `jupyter`
* `ramp-workflow`

To run a submission and the notebook you will need the dependencies listed in requirements.txt.
You can install the dependencies with the following command-line:

```
pip install -U -r requirements.txt
```

### Getting started

1. download the data locally:

```
python download_data.py
```

2.Running the model locally:

```
ramp-test --submission starting_kit
```

## Scientific Rationale for Model Selection

### 1. Data preprocessing
#### a. Feature extraction: ROI

We began by choosing to take into account the regions of interest as features of the model. By only choosing these variables without the voxels, this allows us to: 1) Not have any multicollinearity since the two blocks are very redundant, 2) Have a lower dimension compared to the number of observations and thus avoid the overdetermined case. We therefore end up with a dataframe of size [410, 284].

#### b. Scaling

Data scaling can be beneficial in many cases, especially if the characteristics have different units or scales. Here are some of the advantages of data scaling:

Improved performance: data scaling can help improve the performance of many machine learning models, as it can facilitate the search for a good decision boundary. This is particularly important for models that use distance-based measures, such as the SVC (Support Vector Classification) model.
Reduced convergence time: data scaling can also help reduce the convergence time of the model, as it can facilitate the search for a good solution. This can be particularly beneficial for models that use optimization algorithms, such as gradient descent.
Reduced sensitivity to outliers: data scaling can also help reduce the model's sensitivity to outliers, as it can reduce the impact of large values on the model. This can be particularly advantageous for models that are sensitive to outliers, such as linear regression.

### 2. Model : Voting Classifier

An ensemble model is a machine learning model that combines the predictions of several individual models and, in our case, uses a weighted vote to make a final prediction. We chose it because it allows:

Improved performance: ensemble models can often achieve greater accuracy and better performance than a single model, due to the diversity of the individual models.
Better robustness: ensemble models are often more robust and less prone to overfitting than single models, as they combine the predictions of several models and reduce dependence on a single model.
Reduced variance: ensemble models can help reduce the variance of predictions, which can be particularly beneficial when individual models have high variance and a lot of noise in the data.
Improved generalization: ensemble models can often better generalize to unseen data than single models, because they combine the predictions of several models and reduce the dependence on a single model.

Our sub-models are as follows:

An SVC model is a supervised learning algorithm used for classification tasks. It works by finding the hyperplane in a high-dimensional feature space that separates the classes of data to the greatest extent possible. The hyperplane is chosen such that the distance between it and the closest data points of each class is maximized. These closest data points are called "support vectors." This ensures that the model is robust and resistant to noise in the data.
A NuSVC model is a variation of the SVC model that uses the nu parameter to control the number of support vectors and the regularization parameter C to control the complexity of the model. It is a powerful and widely used tool for classification tasks.
Finally, gradient boosting relies on gradient learning that builds a prediction model in sequence, adjusting each new model to correct the errors made by previous models. This process is repeated until the desired number of models is reached. Finally, the predictions of all the models are combined to produce the final prediction. However, it can be quite complex to implement and often requires fine-tuning of the hyperparameters to achieve good performance. We have hyperparameterized the depth and number of estimators.

