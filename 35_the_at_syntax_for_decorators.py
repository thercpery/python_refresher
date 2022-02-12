import functools

user = {
    "username": "RC",
    "access_level": "guest"
}

def make_secure(func):
    @functools.wraps(func) # it keeps the name and documentation of any function that has this function as a decorator.
    def secure_function():
        if user["access_level"] == "admin":
            return func()
        else:
            return f"No admin permissions for {user['username']}."

    return secure_function

@make_secure # this will prevent the function from running as is and instead created and passed it through an operator in one go.
def get_admin_password():
    # Guests must not access this function.
    return "1234"

print(get_admin_password.__name__)
print(get_admin_password())