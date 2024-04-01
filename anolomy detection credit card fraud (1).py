{
  "nbformat": 4,
  "nbformat_minor": 0,
  "metadata": {
    "colab": {
      "name": "Anomaly Detection - Credit Card Fraud.ipynb",
      "version": "0.3.2",
      "provenance": [],
      "collapsed_sections": [],
      "include_colab_link": 'true'
    },
    "kernelspec": {
      "name": "python3",
      "display_name": "Python 3"
    },
    "accelerator": "TPU"
  },
  "cells": [
    {
      "cell_type": "markdown",
      "metadata": {
        "id": "view-in-github",
        "colab_type": "text"
      },
      "source": [
        "<a href=\"https://colab.research.google.com/github/mfavaits/YouTube-Series-on-Machine-Learning/blob/master/Anomaly_Detection_Credit_Card_Fraud.ipynb\" target=\"_parent\"><img src=\"https://colab.research.google.com/assets/colab-badge.svg\" alt=\"Open In Colab\"/></a>"
      ]
    },
    {
      "cell_type": "code",
      "metadata": {
        "id": "yeHM1o2KVaG4",
        "colab_type": "code",
        "colab": {}
      },
      "source": [
        "import numpy as np #linear algebra library of Python\n",
        "import pandas as pd # build on top of numpy for data analysis, data manipulation and data visualization"
      ],
      "execution_count": 0,
      "outputs": []
    },
    {
      "cell_type": "markdown",
      "metadata": {
        "id": "h9VDKOcHxjiS",
        "colab_type": "text"
      },
      "source": [
        "Now let's mount Google drive so that we can upload the diabetes.csv file. You can find the code in the 'Code snippets' tab of Colab"
      ]
    },
    {
      "cell_type": "code",
      "metadata": {
        "id": "rZAb8UyBZOyk",
        "colab_type": "code",
        "outputId": "658a89ef-e9f4-48b6-8023-9fc2f48ddb03",
        "colab": {
          "base_uri": "https://localhost:8080/",
          "height": 34
        }
      },
      "source": [
        "from google.colab import drive\n",
        "drive.mount('/content/gdrive')"
      ],
      "execution_count": 0,
      "outputs": [
        {
          "output_type": "stream",
          "text": [
            "Drive already mounted at /content/gdrive; to attempt to forcibly remount, call drive.mount(\"/content/gdrive\", force_remount=True).\n"
          ],
          "name": "stdout"
        }
      ]
    },
    {
      "cell_type": "markdown",
      "metadata": {
        "id": "NJBkAU_OyxNG",
        "colab_type": "text"
      },
      "source": [
        "First thing that we do is take a look at the shape of the dataframe (df.shape) and take a look at first 5 lines through df.head()"
      ]
    },
    {
      "cell_type": "code",
      "metadata": {
        "id": "TPjSc1H1XGhq",
        "colab_type": "code",
        "outputId": "9b7864a3-f592-4b4b-8504-17351bf8a0d8",
        "colab": {
          "base_uri": "https://localhost:8080/",
          "height": 284
        }
      },
      "source": [
        "df=pd.read_csv('/content/gdrive/My Drive/Colab Notebooks/creditcard.csv') #import file from Google Drive and create a pandas dataframe df\n",
        "df.head() #shows first 5 lines including column namesdf.shape # number of rows and columns of dataframe"
      ],
      "execution_count": 0,
      "outputs": [
        {
          "output_type": "execute_result",
          "data": {
            "text/html": [
              "<div>\n",
              "<style scoped>\n",
              "    .dataframe tbody tr th:only-of-type {\n",
              "        vertical-align: middle;\n",
              "    }\n",
              "\n",
              "    .dataframe tbody tr th {\n",
              "        vertical-align: top;\n",
              "    }\n",
              "\n",
              "    .dataframe thead th {\n",
              "        text-align: right;\n",
              "    }\n",
              "</style>\n",
              "<table border=\"1\" class=\"dataframe\">\n",
              "  <thead>\n",
              "    <tr style=\"text-align: right;\">\n",
              "      <th></th>\n",
              "      <th>Time</th>\n",
              "      <th>V1</th>\n",
              "      <th>V2</th>\n",
              "      <th>V3</th>\n",
              "      <th>V4</th>\n",
              "      <th>V5</th>\n",
              "      <th>V6</th>\n",
              "      <th>V7</th>\n",
              "      <th>V8</th>\n",
              "      <th>V9</th>\n",
              "      <th>V10</th>\n",
              "      <th>V11</th>\n",
              "      <th>V12</th>\n",
              "      <th>V13</th>\n",
              "      <th>V14</th>\n",
              "      <th>V15</th>\n",
              "      <th>V16</th>\n",
              "      <th>V17</th>\n",
              "      <th>V18</th>\n",
              "      <th>V19</th>\n",
              "      <th>V20</th>\n",
              "      <th>V21</th>\n",
              "      <th>V22</th>\n",
              "      <th>V23</th>\n",
              "      <th>V24</th>\n",
              "      <th>V25</th>\n",
              "      <th>V26</th>\n",
              "      <th>V27</th>\n",
              "      <th>V28</th>\n",
              "      <th>Amount</th>\n",
              "      <th>Class</th>\n",
              "    </tr>\n",
              "  </thead>\n",
              "  <tbody>\n",
              "    <tr>\n",
              "      <th>0</th>\n",
              "      <td>0.0</td>\n",
              "      <td>-1.359807</td>\n",
              "      <td>-0.072781</td>\n",
              "      <td>2.536347</td>\n",
              "      <td>1.378155</td>\n",
              "      <td>-0.338321</td>\n",
              "      <td>0.462388</td>\n",
              "      <td>0.239599</td>\n",
              "      <td>0.098698</td>\n",
              "      <td>0.363787</td>\n",
              "      <td>0.090794</td>\n",
              "      <td>-0.551600</td>\n",
              "      <td>-0.617801</td>\n",
              "      <td>-0.991390</td>\n",
              "      <td>-0.311169</td>\n",
              "      <td>1.468177</td>\n",
              "      <td>-0.470401</td>\n",
              "      <td>0.207971</td>\n",
              "      <td>0.025791</td>\n",
              "      <td>0.403993</td>\n",
              "      <td>0.251412</td>\n",
              "      <td>-0.018307</td>\n",
              "      <td>0.277838</td>\n",
              "      <td>-0.110474</td>\n",
              "      <td>0.066928</td>\n",
              "      <td>0.128539</td>\n",
              "      <td>-0.189115</td>\n",
              "      <td>0.133558</td>\n",
              "      <td>-0.021053</td>\n",
              "      <td>149.62</td>\n",
              "      <td>0</td>\n",
              "    </tr>\n",
              "    <tr>\n",
              "      <th>1</th>\n",
              "      <td>0.0</td>\n",
              "      <td>1.191857</td>\n",
              "      <td>0.266151</td>\n",
              "      <td>0.166480</td>\n",
              "      <td>0.448154</td>\n",
              "      <td>0.060018</td>\n",
              "      <td>-0.082361</td>\n",
              "      <td>-0.078803</td>\n",
              "      <td>0.085102</td>\n",
              "      <td>-0.255425</td>\n",
              "      <td>-0.166974</td>\n",
              "      <td>1.612727</td>\n",
              "      <td>1.065235</td>\n",
              "      <td>0.489095</td>\n",
              "      <td>-0.143772</td>\n",
              "      <td>0.635558</td>\n",
              "      <td>0.463917</td>\n",
              "      <td>-0.114805</td>\n",
              "      <td>-0.183361</td>\n",
              "      <td>-0.145783</td>\n",
              "      <td>-0.069083</td>\n",
              "      <td>-0.225775</td>\n",
              "      <td>-0.638672</td>\n",
              "      <td>0.101288</td>\n",
              "      <td>-0.339846</td>\n",
              "      <td>0.167170</td>\n",
              "      <td>0.125895</td>\n",
              "      <td>-0.008983</td>\n",
              "      <td>0.014724</td>\n",
              "      <td>2.69</td>\n",
              "      <td>0</td>\n",
              "    </tr>\n",
              "    <tr>\n",
              "      <th>2</th>\n",
              "      <td>1.0</td>\n",
              "      <td>-1.358354</td>\n",
              "      <td>-1.340163</td>\n",
              "      <td>1.773209</td>\n",
              "      <td>0.379780</td>\n",
              "      <td>-0.503198</td>\n",
              "      <td>1.800499</td>\n",
              "      <td>0.791461</td>\n",
              "      <td>0.247676</td>\n",
              "      <td>-1.514654</td>\n",
              "      <td>0.207643</td>\n",
              "      <td>0.624501</td>\n",
              "      <td>0.066084</td>\n",
              "      <td>0.717293</td>\n",
              "      <td>-0.165946</td>\n",
              "      <td>2.345865</td>\n",
              "      <td>-2.890083</td>\n",
              "      <td>1.109969</td>\n",
              "      <td>-0.121359</td>\n",
              "      <td>-2.261857</td>\n",
              "      <td>0.524980</td>\n",
              "      <td>0.247998</td>\n",
              "      <td>0.771679</td>\n",
              "      <td>0.909412</td>\n",
              "      <td>-0.689281</td>\n",
              "      <td>-0.327642</td>\n",
              "      <td>-0.139097</td>\n",
              "      <td>-0.055353</td>\n",
              "      <td>-0.059752</td>\n",
              "      <td>378.66</td>\n",
              "      <td>0</td>\n",
              "    </tr>\n",
              "    <tr>\n",
              "      <th>3</th>\n",
              "      <td>1.0</td>\n",
              "      <td>-0.966272</td>\n",
              "      <td>-0.185226</td>\n",
              "      <td>1.792993</td>\n",
              "      <td>-0.863291</td>\n",
              "      <td>-0.010309</td>\n",
              "      <td>1.247203</td>\n",
              "      <td>0.237609</td>\n",
              "      <td>0.377436</td>\n",
              "      <td>-1.387024</td>\n",
              "      <td>-0.054952</td>\n",
              "      <td>-0.226487</td>\n",
              "      <td>0.178228</td>\n",
              "      <td>0.507757</td>\n",
              "      <td>-0.287924</td>\n",
              "      <td>-0.631418</td>\n",
              "      <td>-1.059647</td>\n",
              "      <td>-0.684093</td>\n",
              "      <td>1.965775</td>\n",
              "      <td>-1.232622</td>\n",
              "      <td>-0.208038</td>\n",
              "      <td>-0.108300</td>\n",
              "      <td>0.005274</td>\n",
              "      <td>-0.190321</td>\n",
              "      <td>-1.175575</td>\n",
              "      <td>0.647376</td>\n",
              "      <td>-0.221929</td>\n",
              "      <td>0.062723</td>\n",
              "      <td>0.061458</td>\n",
              "      <td>123.50</td>\n",
              "      <td>0</td>\n",
              "    </tr>\n",
              "    <tr>\n",
              "      <th>4</th>\n",
              "      <td>2.0</td>\n",
              "      <td>-1.158233</td>\n",
              "      <td>0.877737</td>\n",
              "      <td>1.548718</td>\n",
              "      <td>0.403034</td>\n",
              "      <td>-0.407193</td>\n",
              "      <td>0.095921</td>\n",
              "      <td>0.592941</td>\n",
              "      <td>-0.270533</td>\n",
              "      <td>0.817739</td>\n",
              "      <td>0.753074</td>\n",
              "      <td>-0.822843</td>\n",
              "      <td>0.538196</td>\n",
              "      <td>1.345852</td>\n",
              "      <td>-1.119670</td>\n",
              "      <td>0.175121</td>\n",
              "      <td>-0.451449</td>\n",
              "      <td>-0.237033</td>\n",
              "      <td>-0.038195</td>\n",
              "      <td>0.803487</td>\n",
              "      <td>0.408542</td>\n",
              "      <td>-0.009431</td>\n",
              "      <td>0.798278</td>\n",
              "      <td>-0.137458</td>\n",
              "      <td>0.141267</td>\n",
              "      <td>-0.206010</td>\n",
              "      <td>0.502292</td>\n",
              "      <td>0.219422</td>\n",
              "      <td>0.215153</td>\n",
              "      <td>69.99</td>\n",
              "      <td>0</td>\n",
              "    </tr>\n",
              "  </tbody>\n",
              "</table>\n",
              "</div>"
            ],
            "text/plain": [
              "   Time        V1        V2        V3  ...       V27       V28  Amount  Class\n",
              "0   0.0 -1.359807 -0.072781  2.536347  ...  0.133558 -0.021053  149.62      0\n",
              "1   0.0  1.191857  0.266151  0.166480  ... -0.008983  0.014724    2.69      0\n",
              "2   1.0 -1.358354 -1.340163  1.773209  ... -0.055353 -0.059752  378.66      0\n",
              "3   1.0 -0.966272 -0.185226  1.792993  ...  0.062723  0.061458  123.50      0\n",
              "4   2.0 -1.158233  0.877737  1.548718  ...  0.219422  0.215153   69.99      0\n",
              "\n",
              "[5 rows x 31 columns]"
            ]
          },
          "metadata": {
            "tags": []
          },
          "execution_count": 4
        }
      ]
    },
    {
      "cell_type": "code",
      "metadata": {
        "id": "moM92WI71Y7J",
        "colab_type": "code",
        "outputId": "e0e155fd-2af7-4ab0-d6a8-d1244af205a9",
        "colab": {
          "base_uri": "https://localhost:8080/",
          "height": 34
        }
      },
      "source": [
        "df.shape # provides # rows and # columns of the dataframe df - 768 rows and 9 columns"
      ],
      "execution_count": 0,
      "outputs": [
        {
          "output_type": "execute_result",
          "data": {
            "text/plain": [
              "(284807, 31)"
            ]
          },
          "metadata": {
            "tags": []
          },
          "execution_count": 5
        }
      ]
    },
    {
      "cell_type": "markdown",
      "metadata": {
        "id": "YxB7h1y7bSNP",
        "colab_type": "text"
      },
      "source": [
        "Let's create numpy arrays, one for the features (X) and one for the label (y)\n",
        "\n"
      ]
    },
    {
      "cell_type": "code",
      "metadata": {
        "id": "qUygFiYQaw3N",
        "colab_type": "code",
        "colab": {}
      },
      "source": [
        "X=df.drop('Class', 1).values #drop 'Outcome' column but you keep the index column\n",
        "y=df['Class'].values"
      ],
      "execution_count": 0,
      "outputs": []
    },
    {
      "cell_type": "markdown",
      "metadata": {
        "id": "10WLT2xwiB67",
        "colab_type": "text"
      },
      "source": [
        "We import the train_test_split function from sklearn to split the arrays or matrices into random train and test subsets>\n",
        "\n",
        "Parameters:\t\n",
        "test_size : in our case 20% (default=0.25)\n",
        "\n",
        "random_state: is basically used for reproducing your problem the same every time it is run. If you do not use a random_state in train_test_split, every time you make the split you might get a different set of train and test data points and will not help you in debugging in case you get an issue. We used random_state=42 but number does not matter\n",
        "\n",
        "stratify : array-like or None (default=None)\n",
        "If the number of values belonging to each class are unbalanced, using stratified sampling is a good thing. You are basically asking the model to take the training and test set such that the class proportion is same as of the whole dataset, which is the right thing to do."
      ]
    },
    {
      "cell_type": "code",
      "metadata": {
        "id": "Hxn2btplf0jS",
        "colab_type": "code",
        "colab": {}
      },
      "source": [
        "random_state = np.random.RandomState(42)"
      ],
      "execution_count": 0,
      "outputs": []
    },
    {
      "cell_type": "code",
      "metadata": {
        "id": "12_ydvVxekDA",
        "colab_type": "code",
        "colab": {}
      },
      "source": [
        "from sklearn.model_selection import train_test_split #method to split training and testing data sets\n",
        "X_train, X_test, y_train, y_test=train_test_split(X, y, test_size=0.2, random_state=random_state, stratify=y)"
      ],
      "execution_count": 0,
      "outputs": []
    },
    {
      "cell_type": "code",
      "metadata": {
        "id": "-luLiVgn3pCF",
        "colab_type": "code",
        "colab": {}
      },
      "source": [
        "#from sklearn.preprocessing import StandardScaler \n",
        "#sc=StandardScaler()\n",
        "#X_train=sc.fit_transform(X_train)\n",
        "#X_test=sc.transform(X_test)"
      ],
      "execution_count": 0,
      "outputs": []
    },
    {
      "cell_type": "markdown",
      "metadata": {
        "id": "Us9gXeWFjfPs",
        "colab_type": "text"
      },
      "source": [
        "Now we are ready to use AD algorithm"
      ]
    },
    {
      "cell_type": "code",
      "metadata": {
        "id": "AcmvlE1RflBF",
        "colab_type": "code",
        "outputId": "d1f26969-586e-493a-9213-48613e9d562b",
        "colab": {
          "base_uri": "https://localhost:8080/",
          "height": 284
        }
      },
      "source": [
        "pip install pyOD"
      ],
      "execution_count": 0,
      "outputs": [
        {
          "output_type": "stream",
          "text": [
            "Requirement already satisfied: pyOD in /usr/local/lib/python3.6/dist-packages (0.7.4)\n",
            "Requirement already satisfied: scikit-learn>=0.19.1 in /usr/local/lib/python3.6/dist-packages (from pyOD) (0.21.3)\n",
            "Requirement already satisfied: six in /usr/local/lib/python3.6/dist-packages (from pyOD) (1.12.0)\n",
            "Requirement already satisfied: numpy>=1.13 in /usr/local/lib/python3.6/dist-packages (from pyOD) (1.16.4)\n",
            "Requirement already satisfied: scipy>=0.19.1 in /usr/local/lib/python3.6/dist-packages (from pyOD) (1.3.1)\n",
            "Requirement already satisfied: matplotlib in /usr/local/lib/python3.6/dist-packages (from pyOD) (3.0.3)\n",
            "Requirement already satisfied: joblib in /usr/local/lib/python3.6/dist-packages (from pyOD) (0.13.2)\n",
            "Requirement already satisfied: numba>=0.35 in /usr/local/lib/python3.6/dist-packages (from pyOD) (0.40.1)\n",
            "Requirement already satisfied: pyparsing!=2.0.4,!=2.1.2,!=2.1.6,>=2.0.1 in /usr/local/lib/python3.6/dist-packages (from matplotlib->pyOD) (2.4.2)\n",
            "Requirement already satisfied: kiwisolver>=1.0.1 in /usr/local/lib/python3.6/dist-packages (from matplotlib->pyOD) (1.1.0)\n",
            "Requirement already satisfied: python-dateutil>=2.1 in /usr/local/lib/python3.6/dist-packages (from matplotlib->pyOD) (2.5.3)\n",
            "Requirement already satisfied: cycler>=0.10 in /usr/local/lib/python3.6/dist-packages (from matplotlib->pyOD) (0.10.0)\n",
            "Requirement already satisfied: llvmlite>=0.25.0dev0 in /usr/local/lib/python3.6/dist-packages (from numba>=0.35->pyOD) (0.29.0)\n",
            "Requirement already satisfied: setuptools in /usr/local/lib/python3.6/dist-packages (from kiwisolver>=1.0.1->matplotlib->pyOD) (41.2.0)\n"
          ],
          "name": "stdout"
        }
      ]
    },
    {
      "cell_type": "code",
      "metadata": {
        "id": "B_unKXEbf8bg",
        "colab_type": "code",
        "colab": {}
      },
      "source": [
        "from pyod.models.lof import LOF   # LOF detector\n",
        "from pyod.models.ocsvm import OCSVM # One Class SVM\n",
        "from pyod.models.iforest import IForest #Isolated Forests\n",
        "from pyod.utils.data import evaluate_print"
      ],
      "execution_count": 0,
      "outputs": []
    },
    {
      "cell_type": "code",
      "metadata": {
        "id": "YekEurMDioue",
        "colab_type": "code",
        "colab": {}
      },
      "source": [
        "Classifiers = {'Local Outlier Factor (LOF)': LOF(n_neighbors=20, algorithm='auto', metric='minkowski', p=2, metric_params=None, contamination=0.002, n_jobs=-1), \n",
        "               'OneClassSVM': OCSVM (kernel='poly', degree=3 , nu=0.1, max_iter=-1, contamination=0.002), \n",
        "               'Isolation Forests': IForest(n_estimators=100, contamination=0.002, n_jobs=-1, random_state=random_state)}"
      ],
      "execution_count": 0,
      "outputs": []
    },
    {
      "cell_type": "code",
      "metadata": {
        "id": "IgUVVkIim6-B",
        "colab_type": "code",
        "outputId": "873af6c7-b216-471a-a9e2-cf4ba59a07ed",
        "colab": {
          "base_uri": "https://localhost:8080/",
          "height": 247
        }
      },
      "source": [
        "for i, (clf_name, clf) in enumerate(Classifiers.items()):\n",
        "        print()\n",
        "        print(i + 1, 'fitting', clf_name)\n",
        "        \n",
        "        # fit the data and tag outliers\n",
        "        clf.fit(X_train) # fit model on training data\n",
        "       \n",
        "        y_train_pred = clf.labels_ # the binary labels of the training data: 0 for inliers and 1 for anomalies\n",
        "        y_train_scores = clf.decision_scores_ # the outlier scores of the training data\n",
        "        \n",
        "        y_test_pred = clf.predict(X_test) # predict if a particular sample is an outlier or not\n",
        "        y_test_scores = clf.decision_function(X_test) # predict raw anomaly score of the transaction\n",
        "        y_test_proba=clf.predict_proba(X_test) # predict the probability of a sample being outlier\n",
        "        \n",
        "        evaluate_print(clf_name, y_test, y_test_scores)"
      ],
      "execution_count": 0,
      "outputs": [
        {
          "output_type": "stream",
          "text": [
            "\n",
            "1 fitting Local Outlier Factor (LOF)\n",
            "Local Outlier Factor (LOF) ROC:0.7673, precision @ rank n:0.051\n",
            "\n",
            "2 fitting OneClassSVM\n",
            "OneClassSVM ROC:0.6295, precision @ rank n:0.0\n",
            "\n",
            "3 fitting Isolation Forests\n"
          ],
          "name": "stdout"
        },
        {
          "output_type": "stream",
          "text": [
            "/usr/local/lib/python3.6/dist-packages/sklearn/ensemble/iforest.py:247: FutureWarning: behaviour=\"old\" is deprecated and will be removed in version 0.22. Please use behaviour=\"new\", which makes the decision_function change to match other anomaly detection algorithm API.\n",
            "  FutureWarning)\n"
          ],
          "name": "stderr"
        },
        {
          "output_type": "stream",
          "text": [
            "Isolation Forests ROC:0.9519, precision @ rank n:0.2551\n"
          ],
          "name": "stdout"
        }
      ]
    }
  ]
}
