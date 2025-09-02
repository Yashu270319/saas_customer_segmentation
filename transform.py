import pandas as pd
from datetime import datetime

def transform_data(df: pd.DataFrame) -> pd.DataFrame:
    """
    Transforms raw customer data for analysis.

    Steps:
    - Converts date columns to datetime
    - Calculates new features (days_since_signup, days_since_last_login)
    - Handles invalid or missing data
    - Creates a composite engagement_score

    Parameters:
        df (pd.DataFrame): Raw customer data

    Returns:
        pd.DataFrame: Transformed data
    """
    # Convert date columns
    df['signup_date'] = pd.to_datetime(df['signup_date'], errors='coerce')
    df['last_login_date'] = pd.to_datetime(df['last_login_date'], errors='coerce')

    # Drop rows with invalid dates
    df.dropna(subset=['signup_date', 'last_login_date'], inplace=True)

    # Feature engineering
    today = pd.to_datetime(datetime.today())
    df['days_since_signup'] = (today - df['signup_date']).dt.days
    df['days_since_last_login'] = (today - df['last_login_date']).dt.days

    # Composite engagement score (basic formula)
    df['engagement_score'] = (
        df['monthly_usage_minutes'] * 0.5 +
        df['num_logins_last_30_days'] * 3 -
        df['num_support_tickets'] * 5
    )

    # Handle negative or nonsense scores
    df['engagement_score'] = df['engagement_score'].apply(lambda x: max(x, 0))

    # Optional: drop unnecessary raw date columns
    df.drop(['signup_date', 'last_login_date'], axis=1, inplace=True)

    print("Data transformed and features engineered.")
    return df