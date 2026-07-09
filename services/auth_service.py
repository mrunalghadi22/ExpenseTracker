from datetime import datetime
from werkzeug.security import generate_password_hash
from werkzeug.security import check_password_hash

from models.user_model import UserModel
from utils.validators import (
    validate_name,
    validate_email,
    validate_password
)


class AuthService:

    @staticmethod
    def register_user(data):

        full_name = data.get("full_name", "").strip()
        email = data.get("email", "").strip().lower()
        password = data.get("password", "")
        confirm_password = data.get("confirm_password", "")

        # Validate Name
        valid, message = validate_name(full_name)
        if not valid:
            return False, message

        # Validate Email
        valid, message = validate_email(email)
        if not valid:
            return False, message

        # Validate Password
        valid, message = validate_password(password)
        if not valid:
            return False, message

        # Password Match
        if password != confirm_password:
            return False, "Passwords do not match."

        # Email Exists
        if UserModel.email_exists(email):
            return False, "Email already exists."

        user = {
            "full_name": full_name,
            "email": email,
            "password": generate_password_hash(password),
            "is_active": True,
            "created_at": datetime.utcnow(),
            "updated_at": datetime.utcnow()
        }

        UserModel.create_user(user)

        return True, "Registration successful."
    
    @staticmethod
    def login_user(data):
    
      email = data.get("email", "").strip().lower()
    
      password = data.get("password", "")

   
      # Email validation
    
      valid, message = validate_email(email)

    
      if not valid:
       
          return False, message, None

    
      user = UserModel.get_user_by_email(email)

    
      if not user:
       
          return False, "Invalid email or password.", None

    
      if not user.get("is_active", True):
        
          return False, "Account has been deactivated.", None

    
      if not check_password_hash(user["password"], password):
        
          return False, "Invalid email or password.", None

    
      return True, "Login successful.", user