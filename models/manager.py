from .user_interface import UserInterface


class Menager(UserInterface):
    
    def __init__(self, username, email):
        super().__init__(username, email)

    def work(self):
        return f'Paying bills...'
