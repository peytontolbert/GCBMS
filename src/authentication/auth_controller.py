from encryption_service import EncryptionService
from rbac_manager import RBACManager
from models import User
from fastapi.responses import JSONResponse  # Updated import
from src.database import db  # Added import for db
import jwt
from datetime import datetime, timedelta
import os

class AuthController:
    @staticmethod
    def process_google_login(user_info: dict) -> JSONResponse:
        email = user_info.get('email')
        name = user_info.get('name')
        # Check if user exists
        user = User.query.filter_by(email=email).first()
        if not user:
            # Register new user
            user = User(
                username=name,
                email=email,
                password_hash=EncryptionService.hash_password('default_password')  # Handle appropriately
            )
            # Assign default role
            RBACManager.assign_role(user.id, 'Viewer')
            # Save user to the database
            db.session.add(user)
            db.session.commit()
        # Generate tokens
        tokens = AuthController.generate_tokens(user)
        return JSONResponse(content=tokens)  # Replaced jsonify with JSONResponse

    @staticmethod
    def generate_tokens(user: User) -> dict:
        payload = {
            "sub": user.id,
            "exp": datetime.utcnow() + timedelta(hours=1)
        }
        access_token = jwt.encode(payload, os.getenv("JWT_SECRET"), algorithm="HS256")
        refresh_payload = {
            "sub": user.id,
            "exp": datetime.utcnow() + timedelta(days=7)
        }
        refresh_token = jwt.encode(refresh_payload, os.getenv("JWT_SECRET"), algorithm="HS256")
        return {
            "access_token": access_token,
            "refresh_token": refresh_token,
            "expires_at": payload["exp"].isoformat()
        }

    # ... existing methods ...