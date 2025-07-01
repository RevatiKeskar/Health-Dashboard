# 🧠 Health & Lifestyle Cluster Dashboard

A machine learning dashboard that segments individuals into health-based clusters using unsupervised learning. Built with **K-Means Clustering**, enriched with **EDA**, feature engineering, and visualized using **Streamlit**.

## 🚀 Features

- 📊 **Clustering** of individuals based on health & lifestyle habits
- 📉 Detailed **EDA** with outlier removal & feature engineering
- 🧠 **Radar Charts** to compare cluster profiles
- 📈 Interactive **Bar Plots** to analyze features by cluster
- 🧵 Clean UI built with Streamlit (auto-deployed from GitHub)
- 📂 Dataset from Kaggle: [Health & Lifestyle](https://www.kaggle.com/datasets/sahilislam007/health-and-lifestyle-dataset)

---

## 🧪 Tech Stack

- **Python** (Pandas, NumPy, Scikit-learn, Matplotlib, Seaborn)
- **Machine Learning**: K-Means Clustering
- **Visualization**: Streamlit
- **Deployment**: Streamlit Cloud
- **Data**: Health & Lifestyle data (7.5K+ entries)

---

## 📊 Cluster Insights

| Cluster Name                | Traits                                                |
|----------------------------|--------------------------------------------------------|
| Elderly Health-Conscious   | Good sleep, low stress, healthy habits                |
| Unhealthy Lifestyle Group  | Low diet quality, smokers, poor exercise              |
| Obese but Low-Stress       | High BMI but sleep well and low stress                |
| Young Fit Smokers          | Younger, active, but smokers with alcohol consumption |

> You can view these insights dynamically on the dashboard.

---

## 🧠 How Clustering Works

Unsupervised learning (K-Means) groups similar people based on:

- **Age, BMI, Sleep, Stress, Smoking, Alcohol, Chronic Disease**
- Missing values filled using group-wise medians
- Label encoding + normalization before clustering

---

## 🔍 Run Locally

```bash
git clone https://github.com/yourusername/health-cluster-dashboard.git
cd health-cluster-dashboard
pip install -r requirements.txt
streamlit run app.py```


## 🌐 Live Demo

👉 [View Live Dashboard](https://health-cluster-dashboard.streamlit.app/)

---

## 📬 Contact

Made with ❤️ by [Revati Keskar]  
📧 keskarrevati@gmail.com 
📱 [LinkedIn](https://www.linkedin.com/in/revatikeskar/) | [GitHub](https://github.com/RevatiKeskar)
