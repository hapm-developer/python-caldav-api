class CalendarConnector:

    service_url = ""
    username = ""
    password = ""

    def __init__(self, username, password):
        self.username = username
        self.password = password

    def auth(self):
        raise NotImplementedError("Auth method not implemented")

    def get_calendars(self):
        raise NotImplementedError("get_calendar not implemented")

    def get_calendar_by_name(self, name):
        raise NotImplementedError

    def create_calendar_event(self, name, date):
        raise NotImplementedError