# Code is running an A/B test to compare two marketing campaigns: 
# one shown to a control group and one to a test group. 
# We’re trying to see if the new test campaign gets more people to buy something

import pandas as pd


control_df = pd.read_csv('control_group.csv')
test_df = pd.read_csv('test_group.csv')

# print(control_df.head())
# print(test_df.head())

#Split into separate columns, so it looks like a normal table.
control_df = control_df.iloc[:, 0].str.split(";", expand=True)
test_df = test_df.iloc[:, 0].str.split(";", expand=True)

# print(control_df.head())
# print(test_df.head())

# Add column names
columns = [
    "Campaign Name", "Date", "Spend", "Impressions", "Reach", "Website Clicks",
    "Searches", "View Content", "Add to Cart", "Purchase"
]
control_df.columns = columns
test_df.columns = columns

# print(control_df.head())
# print(test_df.head())

# Convert numbers from strings to real numbers
cols_to_numeric = [
    "Spend", "Impressions", "Reach", "Website Clicks",
    "Searches", "View Content", "Add to Cart", "Purchase"
]

# If something can’t be turned into a number (like the word "N/A"), it becomes a missing value
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

# This function does the math to measure how well the ad is working at each step:
# CTR (Click Through Rate): How many people clicked after seeing the ad?
# Search Rate: How many people searched after clicking?
# View Content Rate: How many people viewed something after searching?
# Add to Cart Rate: How many added to cart after viewing?
# Purchase Rate: How many bought something after adding to cart?
# Overall Conversion Rate: How many people bought something out of all who saw the ad?

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

# Finally: Do the A/B Test!

from statsmodels.stats.proportion import proportions_ztest, proportion_confint

# Total conversions and impressions
control_purchases = control_clean["Purchase"].sum()
control_impressions = control_clean["Impressions"].sum()

test_purchases = test_clean["Purchase"].sum()
test_impressions = test_clean["Impressions"].sum()

# Run a Z-test (fancy math to compare the groups)
counts = [test_purchases, control_purchases]  # num of successes
nobs = [test_impressions, control_impressions]  # num of observations (trials)

# This tests if the test group got significantly more purchases than the control group.
# p_value tells us how likely the result was just random luck

z_stat, p_value = proportions_ztest(count=counts, nobs=nobs, alternative='larger')

print("Z-statistic:", z_stat)
print("P-value:", p_value)

# Optional interpretation
if p_value < 0.05:
    print("Result: Statistically significant — Test campaign performs better.")
else:
    print("Result: Not statistically significant — No strong evidence that Test is better.")

# output

# Z-statistic: 33.77499922226043 --- very large => huge diff btw the 2 groups 
# P-value: 2.29665316998631e-250 --- chances of seeing this result just by random luck are practically zero
# Result: Statistically significant — Test campaign performs better.

# -----------------
# -----------------

# Variations We Can Use

# 1. Change the alternative hypothesis

# # Test if the test group is BETTER (this is what you used)
# alternative='larger'

# # Test if the two groups are just DIFFERENT (not necessarily better or worse)
# alternative='two-sided'

# # Test if the test group is WORSE
# alternative='smaller'

# 2. Flip the order of groups
# counts = [control_purchases, test_purchases]
# nobs = [control_impressions, test_impressions]

# Then we'd need to adjust the alternative direction — for example:

# alternative='smaller'

# if we’re still testing whether the test group is better than control (now second in the list)

# 3. Use different metrics

# could compare click-through rate, add-to-cart rate, or any other step of the funnel. 
# Just plug those into counts and nobs:

# counts = [test_clicks, control_clicks]
# nobs = [test_impressions, control_impressions]

# Or, if you want to compare overall conversion rate:

# counts = [test_purchases, control_purchases]
# nobs = [test_reach, control_reach]  # Or impressions, depending on your logic

# 4. Use confidence intervals
# confint = proportion_confint(count=counts, nobs=nobs, alpha=0.05)

# Confidence intervals — call separately for each group
# confint_test = proportion_confint(count=test_purchases, nobs=test_impressions, alpha=0.05)
# confint_control = proportion_confint(count=control_purchases, nobs=control_impressions, alpha=0.05)

# print("95% Confidence Interval:", confint)
# print("95% Confidence Interval for Test group:", confint_test)
# print("95% Confidence Interval for Control group:", confint_control)