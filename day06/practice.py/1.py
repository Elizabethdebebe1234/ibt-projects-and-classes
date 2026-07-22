class Report:
    def build(self):
        print("----- Addis Bank Report -----")
        print("Report generated successfully.")

class report_saver:
    def save(self):
        print("Report saved successfully.")
    
class Email_Sender:
    def send(self):
        print("Email sent successfully.")


report = Report()
report.build()

saver = report_saver()
saver.save()

sender = Email_Sender()
sender.send()

    