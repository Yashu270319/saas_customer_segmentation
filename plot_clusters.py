import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.preprocessing import StandardScaler, OneHotEncoder
from sklearn.decomposition import PCA
from sklearn.compose import ColumnTransformer

def plot_customer_clusters(input_path="data/clustered_customers.csv", save_path="data/cluster_plot.png"):
    """
    Visualizes customer clusters in 2D using PCA.

    Parameters:
        input_path (str): Path to clustered data
        save_path (str): Path to save the plot image
    """
    df = pd.read_csv(input_path)

    # Prepare features for PCA
    cluster_df = df.drop(columns=["customer_id", "churned", "cluster"])
    numeric_features = cluster_df.select_dtypes(include=['int64', 'float64']).columns.tolist()
    categorical_features = ['plan_type']

    transformer = ColumnTransformer([
        ('num', StandardScaler(), numeric_features),
        ('cat', OneHotEncoder(), categorical_features)
    ])

    features_scaled = transformer.fit_transform(cluster_df)

    # Reduce to 2D using PCA
    pca = PCA(n_components=2, random_state=42)
    components = pca.fit_transform(features_scaled)

    # Build plot DataFrame
    plot_df = pd.DataFrame({
        "PCA1": components[:, 0],
        "PCA2": components[:, 1],
        "cluster": df["cluster"].astype(str)
    })

    # Plot
    plt.figure(figsize=(10, 6))
    sns.scatterplot(data=plot_df, x="PCA1", y="PCA2", hue="cluster", palette="Set2", s=60, edgecolor="black")
    plt.title("Customer Clusters (2D PCA View)")
    plt.xlabel("Principal Component 1")
    plt.ylabel("Principal Component 2")
    plt.legend(title="Cluster", loc="best")
    plt.tight_layout()
    plt.savefig(save_path)
    plt.show()
    print(f"Cluster plot saved to {save_path}")