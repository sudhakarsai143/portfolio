from flask import *
import os
# Create an instance of the Flask class
app = Flask(__name__)

# Define a route for the homepage
@app.route('/')
def home():
    # Render the index.html template located in the 'templates' folder
    return render_template('index.html')

# Run the app
if __name__ == '__main__':
    port = int(os.environ.get('PORT', 5000)) 
    app.run(host='0.0.0.0', port=port,debug=True)
