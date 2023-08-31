def announce(f):
    """Decorator to print a function's docstring."""
    def wrapper():
        print("About to run the function....")
        f()
        print("Done with the function.")
    return wrapper
    
@announce
def hello():
    print("Hello, world")

hello()