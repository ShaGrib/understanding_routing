from flask import Flask

app = Flask(__name__)

@app.route('/')
def hello_world():
    return 'Hello World!'

@app.route("/dojo")
def dojo_page():
    return "Dojo!"

@app.route("/say/<name>")
def say_word(name):
    return "Hi " + name.capitalize()

@app.route("/repeat/<int:num>/<string:word>")
def repeat_word_x_times(num, word):
    wordy = word + " "
    return wordy * num

# @app.errorhandler(400)
# def not_found():
#     return "Sorry! No response. Try again."

if __name__ == "__main__":
    app.run(debug=True)