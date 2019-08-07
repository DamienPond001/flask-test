from flask import Flask, render_template
import os
import rpy2.robjects as robjects

app = Flask(__name__)


@app.route('/')
def index():
    r = robjects.r
    r.source("test.R")
    r_response = r.test()
    env_var = r_response[0]#os.getenv('ENV_VAR')

    return render_template('index.html', env_var=env_var)

@app.route('/write/<filename>')
def write(filename):
    f= open("./static/{}test.txt".format(filename),"w+")

    return "{} was created".format(filename)

if __name__ == '__main__':
    app.run(port=80)
