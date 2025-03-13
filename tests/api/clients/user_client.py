import requests

class UserClient:
    def __init__(self, base_url="https://demoqa.com"):
        self.base_url = base_url

    def generate_token(self, data):
        token = f"{self.base_url}/Account/v1/GenerateToken"
        return requests.post(token,json=data)

    def login(self, data):
        url = f"{self.base_url}/Account/v1/Login"
        return requests.post(url,json=data)

    # def create_user(self, data):
    #     url = f"{self.base_url}/Account/v1/User"
    #     return requests.post(url, json=data)
    # # first_name,last_name,user_name,password + kaptcha
    # def delete_user(self, user_id):
    #     url = f"{self.base_url}/Account/v1/User/{user_id}"
    #     return requests.delete(url)