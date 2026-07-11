import re


import re


def validate_name(name):

    name = name.strip()

    if not name:
        return False, "Name is required."

    if len(name) < 3:
        return False, "Name must be at least 3 characters."

    if len(name) > 50:
        return False, "Name cannot exceed 50 characters."

  
    if not re.fullmatch(r"[A-Za-z\s'-]+", name):
        return False, (
            "Name can only contain letters, spaces, "
            "apostrophes (') and hyphens (-)."
        )


    if "  " in name:
        return False, "Name cannot contain multiple consecutive spaces."

    return True, ""


def validate_email(email):

    email = email.strip().lower()

    pattern = r'^[\w\.-]+@[\w\.-]+\.\w+$'

    if not re.match(pattern, email):
        return False, "Invalid email address."

    return True, ""


def validate_password(password):

    if len(password) < 8:
        return False, "Password must be at least 8 characters long."

    if not re.search(r"[A-Z]", password):
        return False, "Password must contain at least one uppercase letter."

    if not re.search(r"[a-z]", password):
        return False, "Password must contain at least one lowercase letter."

    if not re.search(r"\d", password):
        return False, "Password must contain at least one number."

    if not re.search(r"[!@#$%^&*(),.?\":{}|<>]", password):
        return False, "Password must contain at least one special character."

    return True, ""