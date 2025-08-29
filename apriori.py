import pandas as pd
from mlxtend.frequent_patterns import apriori, association_rules
import matplotlib.pyplot as plt

# Step 1: Load and Preprocess the Data
data = pd.read_csv('customer_data.csv')  # Adjust path as needed

# Check if 'Items_Purchased' exists in the dataset
if 'Items_Purchased' not in data.columns:
    raise ValueError("Column 'Items_Purchased' not found in the dataset. Please include this column for Apriori analysis.")

# Handle missing values and preprocess the 'Items_Purchased' column
data['Items_Purchased'] = data['Items_Purchased'].fillna('')

# Convert 'Items_Purchased' into one-hot encoded transaction format
transactions = data['Items_Purchased'].str.get_dummies(sep=', ')

# Step 2: Apply Apriori Algorithm
min_support = 0.001  # Example minimum support
print("Sample Transactions DataFrame:")
print(transactions.head())  # Debug check: Ensure transactions are formatted correctly

# Apply apriori to get frequent itemsets
frequent_itemsets = apriori(transactions, min_support=min_support, use_colnames=True)
print("\nFrequent Itemsets:")
print(frequent_itemsets)

# Step 3: Generate Association Rules
if not frequent_itemsets.empty:
    rules = association_rules(frequent_itemsets, metric="confidence", min_threshold=0.5, support_only=False, num_itemsets=frequent_itemsets.shape[0])  

    print("\nAssociation Rules:")
    print(rules[['antecedents', 'consequents', 'support', 'confidence', 'lift']])

    # Optional: Filter high lift rules
    high_lift_rules = rules[rules['lift'] > 1.5]  # For example, only showing high lift rules
    print("\nHigh Lift Rules:")
    print(high_lift_rules[['antecedents', 'consequents', 'lift']])

    # Step 4: Generate Recommendations based on User Input
    user_input = input("\nEnter item(s) you are buying (separate multiple items with commas): ").strip()  # Get user input

    # Split user input by commas and remove extra spaces
    user_items = [item.strip() for item in user_input.split(',')]

    print(f"\nRecommendations based on {', '.join(user_items)}:")

    recommended = False

    # Check each rule to see if any of the user's items are in the antecedents
    for index, row in rules.iterrows():
        antecedents = list(row['antecedents'])
        consequents = list(row['consequents'])

        # Check if any of the user's items are in the antecedents
        if any(item in antecedents for item in user_items):
            recommended_items = ', '.join(consequents)
            print(f"If you are buying {', '.join(user_items)}, consider buying: {recommended_items} "
                  f"(Confidence: {row['confidence']:.2f}, Lift: {row['lift']:.2f})")
            recommended = True

    if not recommended:
        print(f"Sorry, no recommendations found for {', '.join(user_items)}. Try another item.")

else:
    print("No frequent itemsets found. Try lowering the min_support parameter.")

# Visualization of the frequent itemsets (optional)
frequent_itemsets['support'].plot(kind='bar', figsize=(10,6))
plt.title("Frequent Itemsets Support")
plt.xlabel("Itemsets")
plt.ylabel("Support")
plt.show()
