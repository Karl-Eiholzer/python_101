def say_hello(greet_name):
    'Says hellow to person'
    if greet_name.upper() == "NISHA":
        message1 = "Hello Sundara!!"
    else:
        message1 = str("Hello  ") + greet_name
    return message1

def check_if_string(greet_name):
    'Return false if the input is not characters'
    whitelist_set = set('abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ')
    'if any(c not in whitelist_set for c in greet_name):  '
    if greet_name.isalpha():
        result = "TRUE"
    else:
        result = "FALSE"
    return result