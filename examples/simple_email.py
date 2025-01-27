import os

import resend

if not os.environ["RESEND_API_KEY"]:
    raise EnvironmentError("RESEND_API_KEY is missing")


resend.api_key = os.environ["RESEND_API_KEY"]

params = {
    "from": "r@email.io",
    "to": ["to@gmail.com"],
    "subject": "hi",
    "html": "<strong>hello, world!</strong>",
    "reply_to": "to@gmail.com",
    "bcc": "to@gmail.com",
    "cc": ["to@gmail.com"],
    "tags": [
        {"name": "tag1", "value": "tagvalue1"},
        {"name": "tag2", "value": "tagvalue2"},
    ],
}

email = resend.Emails.send(params)
print(email)

email_resp = resend.Emails.get(email_id=email["id"])
print(email_resp)
