class SMS:
    def __init__(self, id, alert, timestamp, video): # video may not be needed?
        self.id = id
        self.alert = alert
        self.timestamp = timestamp
        self.video = video

    def create_sms(id, alert):
        return (f"{id} - id, {alert} - alert")