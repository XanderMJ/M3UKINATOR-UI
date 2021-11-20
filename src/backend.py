import tekore as spotify
import os

scope = spotify.scope.every

class Client:

    def __init__(self, token) -> None:
        self.token = token
        
    