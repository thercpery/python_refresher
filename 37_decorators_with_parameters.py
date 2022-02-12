import functools

user = {
    "username": "RC",
    "access_level": "guest"
}

def make_secure(access_level): # this is a factory that is used to make a decorator
    def decorator(func):
        @functools.wraps(func) # it keeps the name and documentation of any function that has this function as a decorator.
        def secure_function(*args, **kwargs):
            if user["access_level"] == access_level:
                return func(*args, **kwargs)
            else:
                return f"No {access_level} permissions for {user['username']}."

        return secure_function

    return decorator

@make_secure("admin")
def get_admin_password():
    # Make this only accessible to admins.
    return "admin: 1234"

@make_secure("user")
def get_dashboard_password():
    # Make this only accessible to users.
    return "user: user_password"

print(get_admin_password())
print(get_dashboard_password())

user = {"username": "anna", "access_level": "admin"}
print(get_admin_password())
print(get_dashboard_password())