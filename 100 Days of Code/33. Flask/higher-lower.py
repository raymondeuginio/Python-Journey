from flask import Flask
import random
angkarahasia = random.randint(1,9)
print(angkarahasia)
app = Flask(__name__)

@app.route("/")
def hellogame():
    return "<b style='font-size: 23px'>Guess a number between 0 and 9</b>" \
            "</br><img src='https://media.giphy.com/media/3o7aCSPqXE5C6T8tBC/giphy.gif' width = 300>"
@app.route("/<int:tebakan>")
def hasiltebakan(tebakan):
    if tebakan == angkarahasia:
        return "<h1 style='color:green'>You found me!</h1>" \
            "<img src='https://media.giphy.com/media/4T7e4DmcrP9du/giphy.gif'>"
    if tebakan < angkarahasia :
        return "<h1 style='color:red'>Too low,try again!</h1>" \
            "<img src='https://media.giphy.com/media/jD4DwBtqPXRXa/giphy.gif'>"
    if tebakan > angkarahasia :
        return "<h1 style='color:purple'>Too high,try again!</h1>" \
            "<img src='https://media.giphy.com/media/3o6ZtaO9BZHcOjmErm/giphy.gif'>"
    
if __name__ == "__main__":
    app.run(debug=True)