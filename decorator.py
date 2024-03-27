# Define a decorator to check authorization before executing a function
from datetime import datetime

def decorator(func):
    """
    A wrapper function that checks if you're allowed to do something before actually
    doing it. If you're not allowed, it stops and tells you so.
    """
    def wrapper():
        # Check if you have permission to perform the action
        time = datetime.now().hour

        if 6 <= time < 18:
            # If not authorized, tell the user they can't proceed
            return func()
        # If authorized, go ahead and perform the action
        return "You are not authorized"
    return wrapper



# Decorate functions with the authorization check
# This means "make sure I'm allowed to do this before doing it"
@decorator
def do_A():
    """Does Task A and tells you it's done."""
    return "Do A"

@decorator
def do_B():
    """Does Task B and tells you it's done."""
    return "Do B"

@decorator
def do_C():
    """Does Task C and tells you it's done."""
    return "Do C"

# Main part of the script where we try to do Tasks A, B, and C
if __name__ == "__main__":
    # Try to do Task A and print what happens
    print(do_A())  # Expected: "Do A" if allowed; "You are not authorized" if not
    # Try to do Task B and print what happens
    print(do_B())  # Expected: "Do B" if allowed; "You are not authorized" if not
    # Try to do Task C and print what happens
    print(do_C())  # Expected: "Do C" if allowed; "You are not authorized" if not
