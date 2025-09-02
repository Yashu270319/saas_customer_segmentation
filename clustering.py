import pandas as pd
from sklearn.cluster import KMeans
from sklearn.preprocessing import StandardScaler, OneHotEncoder
from sklearn.compose import ColumnTransformer
from sklearn.pipeline import Pipeline
import os

def cluster_customers(input_path="data/processed_customers.csv", output_path="data/clustered_customers.csv", n_clusters=4):
    """
    Clusters customers using KMeans.

    Parameters:
        input_path (str): Path to processed data CSV
        output_path (str): Where to save clustered data
        n_clusters (int): Number of clusters for KMeans

    Returns:
        pd.DataFrame: Clustered customer data
    """
    if not os.path.exists(input_path):
        raise FileNotFoundError(f"Input file not found: {input_path}")

    df = pd.read_csv(input_path)

    # Features for clustering
    drop_cols = ['customer_id', 'churned']
    cluster_df = df.drop(columns=drop_cols)

    # Categorical encoding + scaling
    numeric_features = cluster_df.select_dtypes(include=['int64', 'float64']).columns.tolist()
    categorical_features = ['plan_type']

    preprocessor = ColumnTransformer([
        ('num', StandardScaler(), numeric_features),
        ('cat', OneHotEncoder(), categorical_features)
    ])

    pipeline = Pipeline([
        ('preprocess', preprocessor),
        ('kmeans', KMeans(n_clusters=n_clusters, random_state=42))
    ])

    pipeline.fit(cluster_df)

    # Predict clusters
    cluster_labels = pipeline.named_steps['kmeans'].labels_
    df['cluster'] = cluster_labels

    # Save result
    os.makedirs(os.path.dirname(output_path), exist_ok=True)
    df.to_csv(output_path, index=False)
    print(f"Clustered data saved to: {output_path}")
    return df