from flask import Flask, render_template, request
from analysis import analyze_market_basket

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def index():
    recommendations = []
    input_items = []
    
    if request.method == 'POST':
        input_items = [item.strip() for item in request.form.get('items', '').split(',')]
        recommendations = analyze_market_basket(input_items)
        print(recommendations)
    
    return render_template('index.html', 
                           recommendations=recommendations, 
                           input_items=input_items)

if __name__ == '__main__':
    app.run(debug=True)
