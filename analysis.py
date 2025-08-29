import pandas as pd
from mlxtend.frequent_patterns import apriori, association_rules

def analyze_market_basket(input_items, 
                           data_path='customer_data.csv', 
                           min_support=0.001, 
                           min_confidence=0.5):
    # Load data
    df = pd.read_csv(data_path)
    
    # Preprocess transactions
    df['Items_Purchased'] = df['Items_Purchased'].fillna('')
    
    # Convert Items_Purchased to one-hot encoded format
    transactions = df['Items_Purchased'].str.get_dummies(sep=', ')
    
    # Apply Apriori algorithm
    frequent_itemsets = apriori(transactions, min_support=min_support, use_colnames=True)
    rules = association_rules(frequent_itemsets, metric="confidence", min_threshold=min_confidence,num_itemsets=frequent_itemsets.shape[0])
    
    # Find recommendations
    recommendations = []
    for _, row in rules.iterrows():
        antecedents = list(row['antecedents'])
        consequents = list(row['consequents'])
        
        # Check if any input items are in antecedents
        if any(str(item) in input_items for item in antecedents):
            recommendations.append({
                'items': [str(item) for item in consequents] if consequents else ['No specific items'],
                'confidence': row['confidence'],
                'lift': row['lift']
            })
    
    return recommendations
