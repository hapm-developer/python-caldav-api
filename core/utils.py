import json

from google_auth_oauthlib.flow import InstalledAppFlow


class MyAppFlow(InstalledAppFlow):

    @classmethod
    def from_client_secrets_json(cls, json_auth, scopes, **kwargs):
        client_config = json.load(json_auth)

        return cls.from_client_config(client_config, scopes=scopes, **kwargs)
