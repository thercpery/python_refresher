import functools

user = {
    "username": "RC",
    "access_level": "guest"
}

def make_secure(func):
    @functools.wraps(func) # it keeps the name and documentation of any function that has this function as a decorator.
    def secure_function(*args, **kwargs):
        if user["access_level"] == "admin":
            return func(*args, **kwargs)
        else:
            return f"No admin permissions for {user['username']}."

    return secure_function

@make_secure # this will prevent the function from running as is and instead created and passed it through an operator in one go.
def get_password(panel):
    # Guests must not access this function.
    if panel == "admin":
        return "1234"
    elif panel == "billing":
        return "super_secure_password"

print(get_password("billing"))