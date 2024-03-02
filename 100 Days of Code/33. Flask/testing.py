def hi_decorator(function):
    def wrapper_function():
        print("~this is decorator~")
        function()
    return wrapper_function

@hi_decorator
def say_hello():
    print("hello")

@hi_decorator
def say_bye():
    print("Bye")

def say_greeting():
    print("How are you?")

say_hello()