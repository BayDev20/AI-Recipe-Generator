from flask import Flask, request, render_template, session
import requests
import os  # Only os is needed for env variables

app = Flask(__name__)

# Load configuration from environment variables
api_key = os.getenv('OPENAI_API_KEY')
secret_key = os.getenv('FLASK_SECRET_KEY')

app.config['SECRET_KEY'] = secret_key  # Use the secret key from env variables

def get_recipe_suggestions(ingredients):
    url = "https://api.openai.com/v1/chat/completions"
    headers = {
        "Authorization": f"Bearer {api_key}",
        "Content-Type": "application/json",
    }
    data = {
        "model": "gpt-3.5-turbo",
        "messages": [
            {"role": "user", "content": f"I have the following ingredients: {ingredients}. Please give me a complete recipe including all of the steps that make use of those ingredients. I am only cooking for two people. I want measurements, temperatures and all the nutritional macros. Talk to me like you are a fun chef named chef puccino and I just asked you for a recipe. Use a lot of emojis including next to the ingredients"}
        ]
    }
    response = requests.post(url, json=data, headers=headers)
    response_data = response.json()  # Get the JSON response data

    print("API Response:", response_data)  # Print the response data to the terminal

    return response_data

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST' and 'ingredients' in request.form:
        ingredients = request.form['ingredients']
        session['last_ingredients'] = ingredients  # Store the last ingredients

        result = get_recipe_suggestions(ingredients)
        if 'choices' in result and result['choices']:
            recipes = result['choices'][0]['message']['content'].replace("\n", "<br>")
        else:
            recipes = "No recipes found."
        return render_template('index.html', recipes=recipes)
    return render_template('index.html')

if __name__ == "__main__":
    app.run(debug=True)