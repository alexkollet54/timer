import requests

params = {
    'access_key': '83d24cb044016e841aaaa95999e07651',
    'query': 'New York'
}

api_result = requests.get('https://api.weatherstack.com/current', params)

api_response = api_result.json()

print('Current temperature in %s is %d℃' % (api_response['location']['name'], api_response['current']['temperature']))