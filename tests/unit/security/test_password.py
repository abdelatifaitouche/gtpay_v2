import pytest
from src.features.auth.security.password import hash_password, verify_password


class TestHashPassword:
    def test_returns_string(self):
        result = hash_password("my_super_secret_password")
        assert isinstance(result, str)

    def test_hash_diff_plain(self):
        plain: str = "my_super_secret_password"

        hashed: str = hash_password(plain)

        assert plain != hashed

    def test_hash_produce_diff(self):
        plain: str = "my_super_secret_password"
        hash_a: str = hash_password(plain)
        hash_b: str = hash_password(plain)

        assert hash_a != hash_b


class TestVerifyPassword:
    def test_verify_same(self):
        plain: str = "my_super_secret_password"

        hashed: str = hash_password(plain)

        assert isinstance(hashed, str)
        assert hashed != plain

        assert verify_password(plain, hashed) is True

    def test_wrong_password(self):
        plain: str = "my_super_secret_password"

        hashed: str = hash_password(plain)

        assert verify_password("my_not_secure_password", hashed) is False

    def test_empty_wrong_password(self):
        hashed: str = hash_password("my_super_secret_password")

        assert verify_password("", hashed) is False
