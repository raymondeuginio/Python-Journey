from flask import Flask

app = Flask(__name__)

def make_bold(function):
    def wrappedup():
        return f'<b>{function()}</b>'
    return wrappedup

def make_underline(function):
    def wrappedup():
        return f'<u>{function()}</u>'
    return wrappedup

def make_emphasis(function):
    def wrappedup():
        return f'<emp>{function()}</emp>'
    return wrappedup


@app.route("/")
@make_bold
@make_underline
@make_emphasis
def hello_world():
    return "<p>Hello, World!</p>"

@app.route("/username/<name>")
def greet(name):
    return f"Hello {name}! "

if __name__ == "__main__":
    app.run(debug=True)