from services.auth.jwt_service import (
    create_access_token,
    verify_access_token,
)

token = create_access_token(
    {
        "sub": "admin@gmail.com",
        "user_id": 1,
        "role": "admin",
    }
)

print("Token:")
print(token)

print("\nDecoded Payload:")
print(verify_access_token(token))