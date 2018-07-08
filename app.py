from flask import Flask, render_template, request
app = Flask(__name__)
@app.route("/")
def main():
    return render_template('index.html')
@app.route('/showSignUp')
def showSignUp():
    return render_template('signup.html')

@app.route('/signUp', methods = ['POST', 'GET'])
def signUp():
   if request.method == 'POST':
      result = request.form
      return render_template("show.html",result = result)
if __name__== "__main__":
    app.run()