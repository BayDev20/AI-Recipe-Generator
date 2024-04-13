from flask import Flask, request, render_template, session
import requests
import os

app = Flask(__name__)

# Load configuration from environment variables
api_key = os.getenv('OPENAI_API_KEY')
secret_key = os.getenv('FLASK_SECRET_KEY')

# Check if necessary configurations are loaded
if not api_key:
    raise ValueError("OPENAI_API_KEY is not set in the environment variables.")
if not secret_key:
    raise ValueError("FLASK_SECRET_KEY is not set in the environment variables.")

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
            {"role": "user", "content": f"I have the following ingredients: {ingredients}. Please give me a recipe."}
        ]
    }
    try:
        response = requests.post(url, json=data, headers=headers)
        response.raise_for_status()  # Raises an HTTPError for bad responses
        response_data = response.json()
        print("API Response:", response_data)
        return response_data
    except requests.exceptions.RequestException as e:
        print(f"Failed to fetch recipe suggestions: {e}")
        return None

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST' and 'ingredients' in request.form:
        ingredients = request.form['ingredients']
        session['last_ingredients'] = ingredients  # Store the last ingredients

        result = get_recipe_suggestions(ingredients)
        if result and 'choices' in result and result['choices']:
            recipes = result['choices'][0]['message']['content'].replace("\n", "<br>")
        else:
            recipes = "No recipes found."
        return render_template('index.html', recipes=recipes)
    return render_template('index.html')

if __name__ == "__main__":
    app.run(debug=True)