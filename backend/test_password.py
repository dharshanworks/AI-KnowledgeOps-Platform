from services.auth.password_service import (
    hash_password,
    verify_password,
)

password = "Admin@123"

hashed = hash_password(password)

print("Original :", password)
print("Hashed   :", hashed)

print(
    verify_password(
        password,
        hashed,
    )
)