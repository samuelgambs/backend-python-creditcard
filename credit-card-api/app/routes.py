from flask import jsonify

@app.route('/api/v1/credit-card', methods=['GET'])
def list_credit_cards():
    # Implement logic to list credit cards
    response_data = [{"exp_date": "02/2026", "holder": "Fulano", "number": "0000000000000001", "cvv": "123"}]
    return jsonify(response_data)


@app.route('/api/v1/credit-card/<key>', methods=['GET'])
def get_credit_card(key):
    # Implement logic to retrieve a specific credit card
    return f"Details of credit card with key {key}"  # Replace with actual response

@app.route('/api/v1/credit-card', methods=['POST'])
def create_credit_card():
    # Implement logic to create a new credit card
    return "Credit card created"  # Replace with actual response
