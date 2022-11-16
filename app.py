from flask import Flask, render_template, request

# Create a flask app
app = Flask(
  __name__,
  template_folder='templates',
  static_folder='static'
)

@app.route('/')
def index():
  return render_template('index.html')

@app.route('/hello')
def hello():
  return render_template('hello.html', name=request.args.get('name'))

@app.route('/about')
def about():
  return render_template('about.html')

@app.errorhandler(404)
def handle_404(e):
    return render_template('404_error.html')


if __name__ == '__main__':
  # Run the Flask app
  app.run(host='0.0.0.0', debug=True, port=8080)