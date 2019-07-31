from flask import Flask, render_template
import os

app = Flask(__name__)


@app.route('/')
def index():
    env_var = 'test'#os.getenv('ENV_VAR')
    return render_template('index.html', env_var=env_var)

if __name__ == '__main__':
    app.run(port=8080)
