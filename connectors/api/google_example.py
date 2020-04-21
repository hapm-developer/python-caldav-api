import json

from connectors.base import CalendarConnector
from core.utils import MyAppFlow


class GoogleConnector(CalendarConnector):
    # service_url =
    scopes = ['https://www.googleapis.com/auth/calendar']

    def __init__(self, username, password):
        """

        :param username: It's the client id from google api
        :param password: It's the client secrect from google api
        """
        super().__init__(username, password)
        self.set_scopes()
        self.auth()

    def set_scopes(self):
        self.scopes = [
            "https://www.googleapis.com/auth/calendar",
            "https://www.googleapis.com/auth/calendar.events"
        ]

    def get_json_auth(self):
        return {
            "web": {
                "client_id": self.username,
                "project_id": "caldavtest-274911",
                "auth_uri": "https://accounts.google.com/o/oauth2/auth",
                "token_uri": "https://oauth2.googleapis.com/token",
                "auth_provider_x509_cert_url": "https://www.googleapis.com/oauth2/v1/certs",
                "client_secret": self.password,
                "redirect_uris": ["https://www.zulip.com",
                                  "http://127.0.0.1:8000"],
                "javascript_origins": ["https://www.zulip.com",
                                       "http://127.0.0.1:8000"]}
        }

    def auth(self):
        flow = MyAppFlow.from_client_secrets_json(
            json.dumps(self.get_json_auth()),
            scopes=self.scopes
        )
        credentials = flow.run_console()
        print(credentials)






username = "804612776867-1avo44oqoftjh3vbm9svkiquq83g8cua.apps.googleusercontent.com"
password = "GLKu9mRBoVob4ih_nUEt9nwf"
connetion = GoogleConnector(username, password)
