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

```


