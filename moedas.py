import requests
import json
cotacoes = requests.get('https://economia.awesomeapi.com.br/last/USD-BRL,EUR-BRL,BTC-BRL')
cotacoes = cotacoes.json()
cotacao_dolar = cotacoes['USDBRL']['bid']
cotacao_euro = cotacoes['EURBRL']['bid']
cotacao_bit = cotacoes['BTCBRL']['bid']

print(f'A cotação do dolar atualmente é {cotacao_dolar}')
print(f'A cotação do euro atualmente é {cotacao_euro}')
print(f'A cotação do bitcoin atualmente é {cotacao_bit}')