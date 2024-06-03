"""
This file has some test for the criticall functionallity such as authentification.
Authors: Andrés Vanegas, Sergio Sanabria
"""



# valid email and password should create a Login instance
def test_valid_email_and_password(self):
    email = "test@example.com"
    password = "strongpassword123"
    login_instance = Login(email=email, password=password)
    assert login_instance.email == email
    assert login_instance.password.get_secret_value() == password


# valid username, email, and password should create a SignUp instance successfully
def test_valid_signup(self):
    user_info = SignUp(username="testuser", email="testuser@example.com", password="strongpassword")
    assert user_info.username == "testuser"
    assert user_info.email == "testuser@example.com"
    assert user_info.password.get_secret_value() == "strongpassword"

