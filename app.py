from flask import Flask, render_template

app = Flask(__name__, template_folder='.')
# The rest of your file here

@app.route('/')
def index():
  """ Serving static files """
  return render_template('index.html')

if __name__ == '__main__':
  app.run(host='0.0.0.0', debug=True, port=5000)
