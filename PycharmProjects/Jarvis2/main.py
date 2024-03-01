import os
import openai
import requests
from pprint import print
openai_apí_key = os.environ.get ("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")
bing_search_apí_key = os.environ ['BING_SEARCH_V7_SUBSCRIPTION_KEY']
bing_search_endpoint - os.environ['BING_SEARCH_V7_ENDPOINT) + "/bing/v7.0/search*
def search(query):
# Query terms) to search for
query = "Microsoft Cognitive Services*
# Construct a request
mkt = 'en-US'
params = ( 'g': Luery,
'mkt': mkt J
headers = ( 'Ocp-Apim-Subscription-Key': bing_search_api_key
# Call the API
try:
response = requests.get (bing_search_endpoint, headers headers, params-params)
response. raise_for_status ()
print ("InHeaders: \n" )
print (response.headers)
print ("InJSON Response: \n")
pprint (response.ison ( ))
except Exception as ex:
raise ex
• Prompt the user for a question
question = input ("What is your question? ")
36
• Send a query to the Bing search engine and retrieve the result
results = search(question);
• Check if there are any results if results:
# Use OpenAI's GPT-3 API to answer the question
openai.api_key = openai_api_key
response = openai. Completion.create(
engine="text-davinci-002"
prompt=f" (question)in(results [0] ('url']in" max_tokens=1024, n=1.
stop=None, temperature=0.5,
