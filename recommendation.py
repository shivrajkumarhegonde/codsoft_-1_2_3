from flask import Flask, render_template
from app.routes import routes

app = Flask(__name__)
app.register_blueprint(routes)

@app.route('/')
def home():
    return render_template('index.html', recommendations=None)

if __name__ == '__main__':
    app.run(debug=True)
