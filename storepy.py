from flask import Flask, render_template

app = Flask(__name__)

@app.route("/")
def index():
  products = [
    {"name": "Product 1", "price": 9.99},
    {"name": "Product 2", "price": 19.99},
    {"name": "Product 3", "price": 29.99}
  ]
  return render_template("index.html", products=products)

if __name__ == "__main__":
  app.run(debug=True)
