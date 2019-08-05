from flask import Flask, render_template
import os

app = Flask(__name__)


@app.route('/')
def index():
    env_var = 'exceptionally nice app'#os.getenv('ENV_VAR')

    return render_template('index.html', env_var=env_var)

@app.route('/write/<filename>')
def write(filename):
    f= open("./static/{}test.txt".format(filename),"w+")

    return "{} was created".format(filename)

if __name__ == '__main__':
    app.run(port=8080)
