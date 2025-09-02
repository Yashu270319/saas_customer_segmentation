from etl.extract import extract_data
from etl.transform import transform_data
from etl.load import load_data
from ml.clustering import cluster_customers
from visualize.plot_clusters import plot_customer_clusters

def main():
    print("\nStarting SaaS Customer Segmentation Pipeline...\n")

    # 1. Extract
    print("Extracting raw data...")
    df_raw = extract_data()

    # 2. Transform
    print("Transforming data...")
    df_transformed = transform_data(df_raw)

    # 3. Load
    print("Saving processed data...")
    load_data(df_transformed)

    # 4. ML Clustering
    print("Running KMeans clustering...")
    df_clustered = cluster_customers()

    # 5. Visualization
    print("Generating cluster plot...")
    plot_customer_clusters()

    print("\nPipeline completed successfully!")

if __name__ == "__main__":
    main()