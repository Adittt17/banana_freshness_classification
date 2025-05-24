# **🍌 Banana Freshness Classification Using CNN**
This project is a **banana Freshness classification system** developed using a **Convolutional Neural Network (CNN)**. It classifies banana images into two categories:

**Ripe**

**Unripe**

🟢 **Try the live demo:**
🔗 https://bananafreshnessclassification.streamlit.app/

## **🧠 About the Project**
The freshness of bananas greatly affects their quality, flavor, and market value. This project aims to assist consumers and sellers by providing an AI-powered tool to automatically classify bananas based on ripeness using image analysis.
The model was trained on a dataset containing images of ripe and unripe bananas captured under various lighting and background conditions. It utilizes convolutional layers to learn visual features and make predictions.

## **🛠️ Technologies Used**

**Python**

**TensorFlow / Keras**

**Streamlit** (for the web app)

**OpenCV** (for image preprocessing)

**Google Colab / Jupyter Notebook**

## **📂 Dataset**
We used a subset of the **Fruits Fresh and Rotten for Classification** dataset from Kaggle, focusing only on the banana class for ripeness detection.

**📦 Dataset Source:**
🔗 https://www.kaggle.com/datasets/sriramr/fruits-fresh-and-rotten-for-classification
The dataset contains labeled images of fresh and rotten bananas, which we mapped to:

**Ripe** → freshbanana

**Unripe** → rottenbanana

## **🚀 Features**

Upload a banana image

Predict if the banana is Ripe or Unripe

View prediction confidence score

Intuitive web interface for easy use

## **🧪 How to Train the Model**
To train the model on your own:

- Download the dataset from the Kaggle link above.

- Extract and organize the banana images into two folders: ripe/ and unripe/.

- Open the .ipynb file in this repository using Google Colab or Jupyter Notebook.

- Run the notebook to:

  - Preprocess the images

  - Define and train a CNN

  - Evaluate and save the model (.h5 file)

## **👨‍💻 Team**
This project was developed by students of the **Computer Engineering Department, Universitas Sriwijaya,** as part of a **final project for the Computer Vision course.**
