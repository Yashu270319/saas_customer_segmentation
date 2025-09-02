import streamlit as st
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

st.set_page_config(
    page_title="SaaS Customer Segmentation Dashboard",
    layout="wide",
    page_icon="📊"
)

st.title("📊 SaaS Customer Segmentation Dashboard")
st.markdown("This dashboard displays customer segmentation results using KMeans clustering.")

# Load clustered data
@st.cache_data
def load_data():
    return pd.read_csv("data/clustered_customers.csv")

df = load_data()

# Sidebar Filters
st.sidebar.header("🔍 Filter Customers")
selected_plan = st.sidebar.multiselect(
    "Select Plan Type(s):",
    options=df['plan_type'].unique(),
    default=df['plan_type'].unique()
)

selected_cluster = st.sidebar.multiselect(
    "Select Cluster(s):",
    options=sorted(df['cluster'].unique()),
    default=sorted(df['cluster'].unique())
)

filtered_df = df[
    (df['plan_type'].isin(selected_plan)) &
    (df['cluster'].isin(selected_cluster))
]

# KPI Cards
col1, col2, col3 = st.columns(3)
col1.metric("Total Customers", len(filtered_df))
col2.metric("Churned Customers", filtered_df['churned'].sum())
col3.metric("Avg. Engagement Score", f"{filtered_df['engagement_score'].mean():.2f}")

# Cluster Distribution Chart
st.subheader("📈 Cluster Distribution")
cluster_counts = filtered_df['cluster'].value_counts().sort_index()
fig1, ax1 = plt.subplots()
sns.barplot(x=cluster_counts.index, y=cluster_counts.values, palette="Set2", ax=ax1)
ax1.set_xlabel("Cluster ID")
ax1.set_ylabel("Number of Customers")
st.pyplot(fig1)

# PCA Cluster Scatter Plot
st.subheader("🧬 PCA Cluster Visualization")
st.image("data/cluster_plot.png", caption="2D Cluster View (PCA)", use_column_width=True)

# Show full table
st.subheader("📋 Customer Data Table")
st.dataframe(filtered_df.reset_index(drop=True), use_container_width=True)