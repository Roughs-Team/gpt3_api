# gpt3_api
**gpt3_api** – Python модуль для работы с GPT-3 API от Roughs Team

```python
import gpt3_api

token = 'ваш токен от roughs.ru/gpt'

gpt = gpt3_api.Generator(token)
reuslt = gpt.send('Однажды, в студенную зимнюю пору')
print(reuslt.text)
```

Установка
------------
    $ pip3 install git+https://github.com/buvanenko/gpt3_api.git
