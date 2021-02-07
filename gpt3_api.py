# Модуль для работы с GPT-3 API от Roughs Team

import requests
from time import sleep

class Result:
    """Результат генерации"""
    def __init__(self, result):
        self.context = result['context']
        self.text = result['text']
        self.time = result['time']
        self.time_spent = result['time_spent']

class Generator:
    """Генератор текстов"""
    
    def __init__(self, token, api_url='https://roughs.ru/gpt'):
        self.token = token
        self.api_url = api_url

    def send(self, context):
        """Отправить текст на генерацию"""
        params = {'context': context, 'token': self.token}
        response = requests.get(self.api_url+'/send', params=params).json()
        generate_id = response['generate_id']
        
        i = 0
        while True:
            i = i + 1
            params = {'generate_id': generate_id, 'token': self.token}
            response = requests.get(self.api_url+'/status', params=params).json()
            try:
                text = response["text"]
                print('='*18)
                print(f'ruGPT-3:\n{text}')
                break
            except KeyError:
                print('='*18)
                print(f'    Проверка №{i}')
                print(f'Статус: {response["status"]}')
                print(f'Место в очереди: {response["position"]}')
                sleep(1)
        
        return Result(response)