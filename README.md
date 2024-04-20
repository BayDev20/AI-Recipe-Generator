# AI Recipe Generator Web Application

This web application allows users to enter ingredients they have on hand and receive recipe suggestions using OpenAI's GPT-3.5 model. It provides creative recipes based on the ingredients provided.

## Features

- User can input ingredients to see recipe suggestions.
- Utilizes OpenAI's GPT API to generate recipes.
- Secure handling of the API key using environment variables.

## Prerequisites

Before you begin, ensure you have met the following requirements:
- Python 3.6 or above is installed.
- Flask and requests libraries are installed.
- You have an OpenAI API key.

## Installation

To set up your local development environment, follow these steps:

1. **Clone the repository**:
   ```bash
    git clone https://yourrepository.git
    cd yourrepository
   ```
2. **Create and activate a virtual environment**:
   ```bash
   python -m venv venv           # Create virtual environment
   source venv/bin/activate      # Activate on Linux/macOS
   venv\Scripts\activate         # Activate on Windows
   ```
3. **Install dependencies**:
   ```bash
   pip install flask requests
   ```

# Configuration
**Set up the required environment variable for your API key**:
```bash
  set OPENAI_API_KEY=your_openai_api_key_here
```
Replace your_openai_api_key_here with your actual OpenAI API key. Make sure this is done in the environment where the application will run.

# Running the Application
**To run the application, execute**:
```bash
  export FLASK_APP=app.py    # Ensure this is set in your environment
  flask run                 # Start the Flask application
```
   
