import pandas as pd
import numpy as np
import random
from datetime import datetime, timedelta
import os

# Seed for reproducibility
random.seed(42)
np.random.seed(42)

n = 1000
today = datetime.today()

def random_date(start, end):
    return start + timedelta(days=random.randint(0, (end - start).days))

plan_types = ['Free', 'Basic', 'Pro', 'Enterprise']
plan_prices = {'Free': 0, 'Basic': 29, 'Pro': 59, 'Enterprise': 129}

data = []
for i in range(1, n + 1):
    signup = random_date(datetime(2020, 1, 1), today - timedelta(days=30))
    last_login = random_date(signup, today)
    plan = np.random.choice(plan_types, p=[0.3, 0.3, 0.3, 0.1])
    usage = np.random.normal(loc=200 if plan != 'Free' else 50, scale=30)
    usage = max(0, usage)
    logins = np.random.poisson(lam=10 if plan != 'Free' else 3)
    tickets = np.random.poisson(lam=1.5 if plan != 'Free' else 0.5)
    churned = np.random.choice([0, 1], p=[0.85, 0.15]) if plan != 'Free' else np.random.choice([0, 1], p=[0.7, 0.3])

    data.append([
        f"CUST{i:04}",
        signup.date(),
        last_login.date(),
        plan,
        round(usage, 1),
        logins,
        tickets,
        plan_prices[plan],
        churned
    ])

columns = [
    "customer_id", "signup_date", "last_login_date",
    "plan_type", "monthly_usage_minutes",
    "num_logins_last_30_days", "num_support_tickets",
    "subscription_price", "churned"
]

df = pd.DataFrame(data, columns=columns)

os.makedirs("data", exist_ok=True)
df.to_csv("data/raw_customers.csv", index=False)
print("data/raw_customers.csv generated successfully.")