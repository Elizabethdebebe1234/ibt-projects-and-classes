class NewsAgency:
    def __init__(self):
        self.subscribers = []

    def subscribe(self, subscriber):
        self.subscribers.append(subscriber)

    def notify(self, news):
        for subscriber in self.subscribers:
            subscriber.update(news)


class PhoneSubscriber:
    def update(self, news):
        print(f"Phone: {news}")


class EmailSubscriber:
    def update(self, news):
        print(f"Email: {news}")


# Create the subject
agency = NewsAgency()

# Create subscribers
phone = PhoneSubscriber()
email = EmailSubscriber()

# Subscribe them
agency.subscribe(phone)
agency.subscribe(email)

# Send news
agency.notify("Breaking News: Python class is starting!")