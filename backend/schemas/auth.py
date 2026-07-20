from pydantic import BaseModel, ConfigDict, EmailStr, Field


class UserRegisterRequest(BaseModel):
    """
    Request schema for user registration.
    """

    name: str = Field(
        ...,
        min_length=3,
        max_length=100,
        description="Full name of the user",
    )

    email: EmailStr

    password: str = Field(
        ...,
        min_length=8,
        max_length=128,
        description="User password",
    )


class UserLoginRequest(BaseModel):
    """
    Request schema for user login.
    """

    email: EmailStr

    password: str = Field(
        ...,
        min_length=8,
        max_length=128,
    )


class UserResponse(BaseModel):
    """
    User information returned after authentication.
    """

    id: int
    name: str
    email: EmailStr
    role: str

    model_config = ConfigDict(
        from_attributes=True
    )


class TokenResponse(BaseModel):
    """
    JWT authentication response.
    """

    access_token: str
    token_type: str
    user: UserResponse