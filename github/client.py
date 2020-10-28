import requests
import json


class GitHubClient:
    
    API_BASE_URL = 'https://api.github.com'

    def __str__(self) -> str:
        return f'GitHubClient()'
    
    @classmethod
    def get_repo_by_user(cls, user) -> json:
        response = requests.get(
            f'{cls.API_BASE_URL}/users/{user}/repos'
        )
        if response.status_code == 200:
            return {"status_code": 200, "body": response.json()}
        else:
            return {"status_code": response.status_code, "body": "Error while getting repos"}
