from flask import Flask, render_template
import os

app = Flask(__name__)


@app.route('/')
def index():
    env_var = os.getenv('env_var')
    return render_template('index.html', env_var=env_var)

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=80)