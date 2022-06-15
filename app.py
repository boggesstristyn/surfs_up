from flask import Flask

#create a new Flask instance called app:
app = Flask(__name__)

# Create Flask Routes
@app.route('/')
def hello_world():
    return 'Hello world'
