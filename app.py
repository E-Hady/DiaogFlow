from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route('/webhook', methods=['POST'])
def webhook():
    request_data = request.get_json()

    # Extract the necessary information from the request JSON
    intent = request_data['queryResult']['intent']['displayName']
    parameters = request_data['queryResult']['parameters']

    # Perform your business logic based on the intent and parameters
    if intent == 'vomitting':
    response = f"Get Sum rest."

    else:
        response = "Sorry, I didn't understand that."

    # Create the webhook response
    webhook_response = {
        "fulfillmentMessages": [
            {
                "text": {
                    "text": [response]
                }
            }
        ]
    }

    return jsonify(webhook_response)

if __name__ == '__main__':
    app.run(debug=True)
