from flask import Flask, render_template

# create a flask app.
app = Flask(__name__)

#create home page
@app.route("/")
def home_page():
    return render_template('index.html')

if __name__ == "__main__":
    app.run(debug=True)