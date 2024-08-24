# Project: Analyzing Farmburg's A/B Test
# Author: Isaac
# Date: 2024-08-24

import pandas as pd
from scipy.stats import chi2_contingency, binom_test

# Project Scope:
# The goal of this project is to analyze the results of an A/B test conducted by Farmburg
# to determine the optimal price point for a new microtransaction feature in their farming simulation game.

# Project Goals:
# 1. Analyze the purchase data from three different price points using a Chi-Square test.
# 2. Determine the number of purchases needed to justify the feature development cost.
# 3. Perform binomial tests to evaluate if the observed purchase rates at each price point meet the required threshold.

# Project Narrative:
# Brian is a Product Manager at FarmBurg, a popular farming simulation social network game.
# In the game, players can plow, plant, and harvest different crops. Brian has been running an A/B test with three different price points
# for a new microtransaction feature. The price points tested were $0.99, $1.99, and $4.99, corresponding to Groups A, B, and C.
# Brian needs to analyze the test results to determine which price point would generate enough revenue to justify the cost of developing the feature.
# The key question is: At which price point should FarmBurg charge for the upgrade package to maximize revenue while meeting the minimum threshold?

# Step 1: Load and inspect the data
abdata = pd.read_csv('/mnt/data/clicks.csv')
print(abdata.head())

# Step 2: Create a contingency table for group and is_purchase
Xtab = pd.crosstab(abdata['group'], abdata['is_purchase'])
print(Xtab)

# Explanation of Step 2:
# The contingency table shows the number of users in each group (A, B, C) who made a purchase ('Yes') or did not make a purchase ('No').
# From the table, we can observe that Group A (the $0.99 price point) has the highest number of purchases (316),
# followed by Group B ($1.99) with 183 purchases, and Group C ($4.99) with 83 purchases.
# This initial observation suggests that the lower price point may have attracted more purchases, but further analysis is needed
# to determine the significance and overall revenue implications.

# Step 3: Perform Chi-Square test to see if there is a significant difference in purchase rates
chi2, pval, dof, expected = chi2_contingency(Xtab)
print(f"Chi-Square Test p-value: {pval}")

# Explanation of Step 3:
# The Chi-Square test is used to determine whether there is a statistically significant difference in purchase rates between the groups.
# The p-value obtained from the test is extremely low (2.4126213546684264e-35), which is much lower than the common significance threshold of 0.05.
# This indicates that there is a significant difference in the purchase rates across the three groups. 
# However, this test alone doesn't tell us which price point is the best for maximizing revenue, so further analysis is required.

# Step 4: Calculate the number of visitors and the revenue target
num_visits = len(abdata)
print(f"Number of visitors: {num_visits}")

# Step 5: Calculate the number of sales needed for each price point
num_sales_needed_099 = 1000 / 0.99
num_sales_needed_199 = 1000 / 1.99
num_sales_needed_499 = 1000 / 4.99

# Step 6: Calculate the proportion of visits needed to meet the revenue target
p_sales_needed_099 = num_sales_needed_099 / num_visits
p_sales_needed_199 = num_sales_needed_199 / num_visits
p_sales_needed_499 = num_sales_needed_499 / num_visits

print(f"Proportion needed for $0.99: {p_sales_needed_099}")
print(f"Proportion needed for $1.99: {p_sales_needed_199}")
print(f"Proportion needed for $4.99: {p_sales_needed_499}")

# Step 7: Calculate sample sizes and number of purchases for each group
samp_size_099 = sum(abdata['group'] == 'A')
sales_099 = sum((abdata['group'] == 'A') & (abdata['is_purchase'] == 'Yes'))

samp_size_199 = sum(abdata['group'] == 'B')
sales_199 = sum((abdata['group'] == 'B') & (abdata['is_purchase'] == 'Yes'))

samp_size_499 = sum(abdata['group'] == 'C')
sales_499 = sum((abdata['group'] == 'C') & (abdata['is_purchase'] == 'Yes'))

print(f"Sample size for $0.99: {samp_size_099}, Purchases: {sales_099}")
print(f"Sample size for $1.99: {samp_size_199}, Purchases: {sales_199}")
print(f"Sample size for $4.99: {samp_size_499}, Purchases: {sales_499}")

# Step 8: Perform binomial tests for each group
pvalueA = binom_test(x=sales_099, n=samp_size_099, p=p_sales_needed_099, alternative='greater')
pvalueB = binom_test(x=sales_199, n=samp_size_199, p=p_sales_needed_199, alternative='greater')
pvalueC = binom_test(x=sales_499, n=samp_size_499, p=p_sales_needed_499, alternative='greater')

print(f"Binomial Test p-value for $0.99: {pvalueA}")
print(f"Binomial Test p-value for $1.99: {pvalueB}")
print(f"Binomial Test p-value for $4.99: {pvalueC}")

# Conclusion:
# Based on the binomial test results:
# - The $0.99 price point (Group A) did not have a significantly higher purchase rate than required.
# - The $1.99 price point (Group B) also did not meet the required threshold.
# - The $4.99 price point (Group C) had a purchase rate significantly higher than the target.
# Therefore, Brian should charge $4.99 for the upgrade to maximize revenue, as the purchase rate at this price point was significantly higher than the target needed to reach $1000 in revenue per week.
