import pandas as pd


control_df = pd.read_csv('control_group.csv')
test_df = pd.read_csv('test_group.csv')

# print(control_df.head())
# print(test_df.head())

control_df = control_df.iloc[:, 0].str.split(";", expand=True)
test_df = test_df.iloc[:, 0].str.split(";", expand=True)

# print(control_df.head())
# print(test_df.head())

columns = [
    "Campaign Name", "Date", "Spend", "Impressions", "Reach", "Website Clicks",
    "Searches", "View Content", "Add to Cart", "Purchase"
]
control_df.columns = columns
test_df.columns = columns

# print(control_df.head())
# print(test_df.head())

cols_to_numeric = [
    "Spend", "Impressions", "Reach", "Website Clicks",
    "Searches", "View Content", "Add to Cart", "Purchase"
]

for col in cols_to_numeric:
    control_df[col] = pd.to_numeric(control_df[col], errors="coerce")
    test_df[col] = pd.to_numeric(test_df[col], errors="coerce")

# Drop rows with any missing values for clean funnel analysis
control_clean = control_df.dropna().copy()
test_clean = test_df.dropna().copy()

# Define function to calculate funnel metrics
def compute_metrics(df):
    df["CTR"] = df["Website Clicks"] / df["Impressions"]
    df["Search Rate"] = df["Searches"] / df["Website Clicks"]
    df["View Content Rate"] = df["View Content"] / df["Searches"]
    df["Add to Cart Rate"] = df["Add to Cart"] / df["View Content"]
    df["Purchase Rate"] = df["Purchase"] / df["Add to Cart"]
    df["Overall Conversion Rate"] = df["Purchase"] / df["Impressions"]
    return df

# Compute metrics
control_metrics = compute_metrics(control_clean)
test_metrics = compute_metrics(test_clean)

# Average metrics for comparison
control_avg = control_metrics[[
    "CTR", "Search Rate", "View Content Rate", "Add to Cart Rate",
    "Purchase Rate", "Overall Conversion Rate"
]].mean()

test_avg = test_metrics[[
    "CTR", "Search Rate", "View Content Rate", "Add to Cart Rate",
    "Purchase Rate", "Overall Conversion Rate"
]].mean()

# print(control_avg)
# print(test_avg)

from statsmodels.stats.proportion import proportions_ztest

# Total conversions and impressions
control_purchases = control_clean["Purchase"].sum()
control_impressions = control_clean["Impressions"].sum()

test_purchases = test_clean["Purchase"].sum()
test_impressions = test_clean["Impressions"].sum()

# Z-test
counts = [test_purchases, control_purchases]  # successes
nobs = [test_impressions, control_impressions]  # trials

z_stat, p_value = proportions_ztest(count=counts, nobs=nobs, alternative='larger')

print("Z-statistic:", z_stat)
print("P-value:", p_value)

# Optional interpretation
if p_value < 0.05:
    print("Result: Statistically significant — Test campaign performs better.")
else:
    print("Result: Not statistically significant — No strong evidence that Test is better.")