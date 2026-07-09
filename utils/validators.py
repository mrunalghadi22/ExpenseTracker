import re


def validate_name(name):

    name = name.strip()

    if len(name) < 3:
        return False, "Name must be at least 3 characters."

    if len(name) > 50:
        return False, "Name cannot exceed 50 characters."

    return True, ""


def validate_email(email):

    email = email.strip().lower()

    pattern = r'^[\w\.-]+@[\w\.-]+\.\w+$'

    if not re.match(pattern, email):
        return False, "Invalid email address."

    return True, ""


def validate_password(password):

    if len(password) < 8:
        return False, "Password must be at least 8 characters."

    if not re.search(r"[A-Z]", password):
        return False, "Password needs one uppercase letter."

    if not re.search(r"[a-z]", password):
        return False, "Password needs one lowercase letter."

    if not re.search(r"\d", password):
        return False, "Password needs one number."

    if not re.search(r"[!@#$%^&*(),.?\":{}|<>]", password):
        return False, "Password needs one special character."

    return True, ""