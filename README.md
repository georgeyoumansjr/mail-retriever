# mail-retriever

## Running the Application

- Setting Up:
Create a virtual Environment and install the libraries in the "requirements.txt" value
```
pip install -r requirements.txt
```

- Create the credentials needed from azure:
Use the url to register the application, add secrets, add permissions, and grant admin access for those permission.
https://portal.azure.com/
if any issue refer to this blog: https://medium.com/nerd-for-tech/query-ms-graph-api-in-python-e8e04490b04e

- Setup the ENVIRONMENT VARIABLES in ".env" file:
add the values from the followed creds

```
CLIENT_ID=YOUR APPLICATION/CLIENT ID #application id at time of application creation
TENANT_ID=YOUR TENANT ID #tenant id at time of application creation
CLIENT_SECRET=YOUR SECRET #client Secret (value is viewable only at the time of creation)
USER_ID=YOUR USER ID #Whole mail you want to extract
```

- Run the application:
```
python manage.py runserver
```

- The route to view the Email listing of Junk, Sent + Inbox mails:
```
http://localhost:8000/outlook/
```

- The JSON format for the response sample is:
 For failed Junk

```
[
  {
    "@odata.etag": "W/\"FwAAABYAAAB18OR3DJpKSK/FhLFozcWrAAAGK33o\"",
    "id": "AAMkADI4NDliYzc3LWIwZmQtNDFmYy05MjY2LTEwZTk0NDc2YjMzNwBGAAAAAABStYkUTXXpSY1UyE4pVKHaBwB18OR3DJpKSK-FhLFozcWrAAAAAAEVAAB18OR3DJpKSK-FhLFozcWrAAAGLjmtAAA=",
    "createdDateTime": "2023-05-30T11:40:00Z",
    "lastModifiedDateTime": "2023-05-31T05:19:10Z",
    "changeKey": "FwAAABYAAAB18OR3DJpKSK/FhLFozcWrAAAGK33o",
    "categories": [],
    "receivedDateTime": "2023-05-30T11:40:00Z",
    "sentDateTime": "2023-05-30T11:39:53Z",
    "hasAttachments": false,
    "internetMessageId": "<20230530113953.956D4100E59@relay.mailchannels.net>",
    "subject": "Undeliverable: 🍚Get Your KSH 50 Off on Grade 1 Rice - Buy Now 🌾",
    "bodyPreview": "This is the mail system at host relay.mailchannels.net.\r\n\r\nI'm sorry to have to inform you that your message could not\r\nbe delivered to one or more recipients. It's attached below.\r\n\r\nFor further assistance, please send mail to postmaster.\r\n\r\nIf you do so",
    "importance": "normal",
    "parentFolderId": "AAMkADI4NDliYzc3LWIwZmQtNDFmYy05MjY2LTEwZTk0NDc2YjMzNwAuAAAAAABStYkUTXXpSY1UyE4pVKHaAQB18OR3DJpKSK-FhLFozcWrAAAAAAEVAAA=",
    "conversationId": "AAQkADI4NDliYzc3LWIwZmQtNDFmYy05MjY2LTEwZTk0NDc2YjMzNwAQAIXRqvFHgJhEu0L3PMgpa_Q=",
    "conversationIndex": "AQHZkut3hdGq8UeAmES7Qvc8yClr5A==",
    "isDeliveryReceiptRequested": null,
    "isReadReceiptRequested": false,
    "isRead": false,
    "isDraft": false,
    "webLink": "https://outlook.office365.com/owa/?ItemID=AAMkADI4NDliYzc3LWIwZmQtNDFmYy05MjY2LTEwZTk0NDc2YjMzNwBGAAAAAABStYkUTXXpSY1UyE4pVKHaBwB18OR3DJpKSK%2FFhLFozcWrAAAAAAEVAAB18OR3DJpKSK%2FFhLFozcWrAAAGLjmtAAA%3D&exvsurl=1&viewmodel=ReadMessageItem",
    "inferenceClassification": "focused",
    "body": {
      "contentType": "text",
      "content": "This is the mail system at host relay.mailchannels.net.\r\n\r\nI'm sorry to have to inform you that your message could not\r\nbe delivered to one or more recipients. It's attached below.\r\n\r\nFor further assistance, please send mail to postmaster.\r\n\r\nIf you do so, please include this problem report. You can\r\ndelete your own text from the attached returned message.\r\n\r\n                   The mail system\r\n\r\n<victorinejepchumba@yoo.com>: host\r\n    eu-smtp-inbound-2.mimecast.com[91.220.42.241] said: 550 Invalid Recipient -\r\n    https://community.mimecast.com/docs/DOC-1369#550\r\n    [FbbFUcEeNJeFtMZ8JSf8TQ.uk91] (in reply to RCPT TO command)\r\n"
    },
    "sender": {
      "emailAddress": {
        "name": "Mail Delivery System",
        "address": "MAILER-DAEMON@mailchannels.net"
      }
    },
    "from": {
      "emailAddress": {
        "name": "Mail Delivery System",
        "address": "MAILER-DAEMON@mailchannels.net"
      }
    },
    "toRecipients": [
      {
        "emailAddress": {
          "name": "victorinejepchumba@yoo.com",
          "address": "victorinejepchumba@yoo.com"
        }
      }
    ],
    "ccRecipients": [],
    "bccRecipients": [],
    "replyTo": [],
    "flag": {
      "flagStatus": "notFlagged"
    }
  }
]
```


