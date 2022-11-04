import requests


class UserClient:
    @staticmethod
    def get_user(api_key):
        headers = {
            "Authorization": api_key
        }
        print('send request1!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!')
        response = requests.request(method="GET", url="http://user-serv:5001/api/user", headers=headers)
        if response.status_code == 401:
            return False
        user = response.json()
        return user
