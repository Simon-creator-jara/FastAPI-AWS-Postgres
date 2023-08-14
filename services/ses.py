from decouple import config
import boto3

class SESService:
    def __init__(self):
        self.key=config("AWS_ACCESS_KEY")
        self.secret=config("AWS_SECRET")
        self.ses = boto3.client(
            "ses",aws_access_key_id=self.key, aws_secret_access_key=self.secret
        )
    
    def send_mail(self,subject,to_adresses,text_data):
        body={"Text":{"Data":text_data, "Charset":"UTF-8"}}

        self.ses.send_email(Source="simonjaramillovelez@hotmail.com",
                            Destination={"ToAddresses":to_adresses,
                                         "CcAddresses":[],
                                         "BccAddresses":[]},
                            Message={"Subject":{"Data":subject, "Charset":"UTF-8"}, "Body":body},

                            )
