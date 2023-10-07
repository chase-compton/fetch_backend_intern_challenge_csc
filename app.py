from flask import Flask
from endpoints import api  # Importing the 'api' Blueprint from endpoints module

app = Flask(__name__)  # Creating a Flask application instance
app.register_blueprint(api)  # Registering the 'api' Blueprint with the application

if __name__ == '__main__':
    # Running the Flask application on port 8000
    app.run(port=8000)
