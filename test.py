# Define imports and config dictionary
import msal
import requests
from dotenv import load_dotenv 
import os 



load_dotenv()


config = {
  'client_id': os.getenv("CLIENT_ID"),
  'client_secret': os.getenv("CLIENT_SECRET"),
  'authority': 'https://login.microsoftonline.com/'+os.getenv("TENANT_ID"),
  'scope': ['https://graph.microsoft.com/.default']
}

# Define a function that takes parameter 'url' and executes a graph call.
# Optional parameter 'pagination' can be set to False to return only first page of graph results
def make_graph_call(url, pagination=True):
  # Firstly, try to lookup an access token in cache
  token_result = client.acquire_token_silent(config['scope'], account=None)
  print(token_result)
  # Log that token was loaded from the cache
  if token_result:
    print('Access token was loaded from cache.')

  # If token not available in cache, acquire a new one from Azure AD
  if not token_result:
    token_result = client.acquire_token_for_client(scopes=config['scope'])
    print('New access token aquired from AAD')

   # If token available, execute Graph query
  if 'access_token' in token_result:
    headers = {
        'Authorization': 'Bearer ' + token_result['access_token'],
        "Content-Type": "application/json"
        }
    graph_results = []

    while url:
      try:
        graph_result = requests.get(url=url, headers=headers).json()
        # print(graph_result)
        graph_results.extend(graph_result['value'])
        if (pagination == True):
          url = graph_result['@odata.nextLink']
        else:
          url = None
      except:
         break
  else:
    print(token_result.get('error'))
    print(token_result.get('error_description'))
    print(token_result.get('correlation'))

  return graph_results

# Create an MSAL instance providing the client_id, authority and client_credential parameters
client = msal.ConfidentialClientApplication(config['client_id'], authority=config['authority'], client_credential=config['client_secret'])
# print(client)""
# Make an MS Graph call
url = 'https://graph.microsoft.com/v1.0/users/'+os.getenv("USER_ID")+"/mailFolders('inbox')/messages"
resp = make_graph_call(url, pagination=False)
import json
with open("response.json","w") as filew:
  json.dump(resp,filew)
print(resp)



