def validate_category_name(name):

    name = name.strip()

    if not name:
        return False, "Category name is required."

    if len(name) < 2:
        return False, "Category name must contain at least 2 characters."

    if len(name) > 30:
        return False, "Category name cannot exceed 30 characters."

    return True, ""