import requests

class LLMConnector:
    def __init__(self, api_key):
        self.api_key = api_key
        self.base_url = 'https://gemini.googleapis.com/v1/'

    def query(self, prompt):
        headers = {'Authorization': f'Bearer {self.api_key}'}
        data = {'prompt': prompt}
        response = requests.post(f'{self.base_url}query', headers=headers, json=data)

        if response.status_code == 200:
            return response.json()
        else:
            raise Exception('Error querying Google Gemini: ' + response.text)
