import bcrypt

"""
    Helper function to hash password 

    using the bcrypt algorithm,
    might add a gensalt value from .env later to add more rounds

"""


def hash_password(password: str) -> str:
    encoded_pwd = password.encode("utf-8")

    hashed = bcrypt.hashpw(encoded_pwd, bcrypt.gensalt())

    return hashed.decode("utf-8")


def verify_password(password: str, hashed_password: str) -> bool:
    return bcrypt.checkpw(
        password.encode("utf-8"),
        hashed_password.encode("utf-8"),
    )
