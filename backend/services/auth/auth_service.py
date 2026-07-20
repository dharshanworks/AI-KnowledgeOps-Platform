from sqlalchemy.orm import Session

from models.user import User
from services.auth.password_service import (
    hash_password,
    verify_password,
)
from services.auth.jwt_service import (
    create_access_token,
)


class AuthService:
    """
    Authentication service.
    Handles user registration and login.
    """

    @staticmethod
    def register_user(
        db: Session,
        name: str,
        email: str,
        password: str,
    ) -> User:
        """
        Register a new user.
        """

        existing_user = (
            db.query(User)
            .filter(User.email == email)
            .first()
        )

        if existing_user:
            raise ValueError(
                "User already exists with this email."
            )

        user = User(
            name=name,
            email=email,
            password_hash=hash_password(password),
            role="user",
            is_active=True,
        )

        db.add(user)
        db.commit()
        db.refresh(user)

        return user

    @staticmethod
    def authenticate_user(
        db: Session,
        email: str,
        password: str,
    ) -> User | None:
        """
        Authenticate a user using email and password.
        """

        user = (
            db.query(User)
            .filter(User.email == email)
            .first()
        )

        if not user:
            return None

        if not verify_password(
            password,
            user.password_hash,
        ):
            return None

        if not user.is_active:
            return None

        return user

    @staticmethod
    def login_user(
        db: Session,
        email: str,
        password: str,
    ) -> dict:
        """
        Authenticate user and generate JWT token.
        """

        user = AuthService.authenticate_user(
            db,
            email,
            password,
        )

        if user is None:
            raise ValueError(
                "Invalid email or password."
            )

        access_token = create_access_token(
            {
                "sub": user.email,
                "user_id": user.id,
                "role": user.role,
            }
        )

        return {
            "access_token": access_token,
            "token_type": "bearer",
            "user": {
                "id": user.id,
                "name": user.name,
                "email": user.email,
                "role": user.role,
            },
        }