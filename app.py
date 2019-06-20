from flask import Flask, render_template

# template_folder points to current directory. Flask will look for '/static/'
app = Flask(__name__, template_folder='.')
# The rest of your file here

@app.route('/')
def index():
  """ Serving static files """
  try:
    return render_template('index.html')
  except:
    return str(e)
if __name__ == '__main__':
  app.run(host='0.0.0.0', debug=True, port=5000)
