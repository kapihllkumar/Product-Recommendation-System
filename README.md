# 🛒 Product Recommendation System

A **Product Recommendation System** built using **Market Basket Analysis (Apriori Algorithm)** to generate personalized product suggestions based on transactional data.  
The project provides a **Flask web application** for interactive recommendations and a **data analysis pipeline** for exploring frequent itemsets and association rules.

---

## ✨ Features
- **Flask Web App**: Enter purchased items and receive product recommendations instantly.  
- **Apriori Algorithm**: Identify frequent itemsets from historical transaction data.  
- **Association Rules**: Generate rules with support, confidence, and lift metrics.  
- **Visualization**: Plot frequent itemsets for better insights.  
- **Customizable Parameters**: Easily adjust `min_support` and `min_confidence` thresholds.  
- **CSV-Based Input**: Works with your own purchase history datasets.  

---

## ⚙️ Installation & Setup

##
### Prerequisites
- Python 3.8+  
- Virtual environment (recommended)

### Steps
```bash
# Clone the repository
git clone https://github.com/kapihllkumarproduct-recommendation-system.git
cd product-recommendation-system

# Create a virtual environment
python -m venv venv
source venv/bin/activate   # On Windows: venv\Scripts\activate

# Install dependencies
pip install -r requirements.txt
```
## Run Flask Web App
```bash
#run the application
python app.py
