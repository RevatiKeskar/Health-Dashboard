import streamlit as st
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

st.set_page_config(page_title="Health Cluster Dashboard", layout  = "wide")
st.title("Health and Lifestyle clustering Dashboard")


@st.cache_data
def load_data():
    df = pd.read_csv("data/health_clustered.csv")
    return df
data = load_data()
st.subheader("Data Preview")
st.dataframe(data.head())

#Sidebar for cluster selection
st.sidebar.header("Filter options")
clusters = sorted(data['Cluster'].unique())
selected_cluster = st.sidebar.selectbox("Select Cluster", clusters)


#Filetered data
cluster_data = data[data['Cluster'] == selected_cluster]

#Show Cluster Size
st.sidebar.markdown(f"**Cluster Size :** {cluster_data.shape[0]} individuals ")


#Show summary stats
st.subheader(f"Summary statistics for cluster {selected_cluster}")
st.write(cluster_data.describe())

#Numerical columns to include
radar_cols = ['Age','Height_cm','Weight_kg','BMI','Stress_Level','Sleep_Hours','Diet_Quality','Chronic_Disease','Smoker','Alcohol_Consumption']

#Normalize values
cluster_avg = data.groupby('Cluster')[radar_cols].mean()

# Normalize values (0 to 1)
cluster_avg_norm = (cluster_avg - cluster_avg.min()) / (cluster_avg.max() - cluster_avg.min())

# Radar chart setup
labels = radar_cols
num_vars = len(labels)

angles = np.linspace(0, 2 * np.pi, num_vars, endpoint=False).tolist()
angles += angles[:1]  # close circle

fig, ax = plt.subplots(figsize=(7, 7), subplot_kw=dict(polar=True))

for i, row in cluster_avg_norm.iterrows():
    values = row.tolist()
    values += values[:1]
    ax.plot(angles, values, label=f'Cluster {i}')
    ax.fill(angles, values, alpha=0.1)

ax.set_theta_offset(np.pi / 2)
ax.set_theta_direction(-1)
ax.set_thetagrids(np.degrees(angles[:-1]), labels)

plt.title("Cluster Profiles (Radar Chart)", size=15)
plt.legend(loc='upper right', bbox_to_anchor=(1.3, 1.1))

st.pyplot(fig)

import seaborn as sns

st.subheader("Compare a Feature Across Clusters")

feature = st.selectbox("Choose a feature to compare", radar_cols)

fig2, ax2 = plt.subplots(figsize=(8, 5))
sns.barplot(x='Cluster', y=feature, data=data, ci=None, palette="Set2", ax=ax2)
ax2.set_title(f"{feature} by Cluster")
st.pyplot(fig2)


