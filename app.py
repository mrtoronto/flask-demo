from flask import Flask, render_template

app = Flask(__name__)

kg_test_var = None

@app.route('/')
def home():
    """
    This is a test docstring to demo whether the KG can read docstrings
    """
    return render_template('index.html', title='Flask Demo')

if __name__ == '__main__':
    app.run(debug=True) 
