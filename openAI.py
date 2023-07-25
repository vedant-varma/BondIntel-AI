# Replace with your actual key, ideally fetched securely
openai.api_key = "ENTER YOUR OPENAI KEY HERE"


def bond_predict(bond):
    """Predict insights on a given bond."""
    messages = [
        {"role": "system",
         "content": "You are an assistant that provides insights on bonds."},
        {"role": "user",
         "content": f"Please provide insights on this bond: {bond}"},
    ]
    response = openai.ChatCompletion.create(
        model="gpt-3.5-turbo", messages=messages
    )
    return response.choices[0].message['content']


def chat(bond, text):
    """Chat with the AI model about a given bond."""
    messages = [
        {"role": "system",
         "content": "You are an assistant that provides insights on bonds."},
        {"role": "user",
         "content": f"For the bond {bond}, {text}"},
    ]
    response = openai.ChatCompletion.create(
        model="gpt-3.5-turbo", messages=messages
    )
    return response.choices[0].message['content']
