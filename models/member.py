from .user_interface import UserInterface


class Member(UserInterface):
    
    def __init__(self, username, email):
        super().__init__(username, email)

    @staticmethod
    def members():
        return ['username1', 'username2', 'times']
    
    def work(self):
        return f'Coding...'
