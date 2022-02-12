# Decorators allow us to easily modify functions to secure it without having to replace any functions by its secure counterparts.

user = {
    "username": "RC",
    "access_level": "guest"
}

def get_admin_password():
    # TODO: Guests must not access this function.
    return "1234"

# Using a function
# def secure_get_admin():
#     if user["access_level"] == "admin":
#         return "1234"

# Use a decorator
def make_secure(func):
    def secure_function():
        if user["access_level"] == "admin":
            return func()
        else:
            return f"No admin permissions for {user['username']}."

    return secure_function

# Traditional way
# if user["access_level"] == "admin":
#     print(get_admin_password()) # this is protected

# print(secure_get_admin()) # returns None because access_level is "guest"

get_admin_password = make_secure(get_admin_password)

print(get_admin_password()) # this is not