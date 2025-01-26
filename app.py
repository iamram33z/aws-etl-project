# Import Necessary Libraries
from flask import Flask, render_template, request, redirect, url_for

# Create an instance of the Flask class
app = Flask(__name__)

# Define the route for the home page
@app.route('/')
def home():
    return render_template('index.html')

# Define the route for saving data
@app.route('/save_data', methods=['GET'])
def save_data():
    # Correcting the syntax for request.args.get
    regno = request.args.get('regno')
    name = request.args.get('name')
    standard = request.args.get('standard')
    math = request.args.get('math')
    science = request.args.get('science')
    computer = request.args.get('computer')

    # Debugging: Print the collected data to the console
    print(regno, name, standard, math, science, computer)

    return redirect(url_for('home'))

# Run the app
if __name__ == '__main__':
    app.run(debug=True)
