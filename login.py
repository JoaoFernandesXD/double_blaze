import requests
from bs4 import BeautifulSoup
import pandas as pd


def login():
    headers = {
        'User-Agent': 'Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:109.0) Gecko/20100101 Firefox/109.0',
        'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,*/*;q=0.8',
        'Accept-Language': 'pt-BR,pt;q=0.8,en-US;q=0.5,en;q=0.3',
        'Referer': 'https://www.historicosblaze.com/users/sign_in?locale=br',
        'Origin': 'https://www.historicosblaze.com',
    }

    session = requests.Session()

    URL = 'https://www.historicosblaze.com/users/sign_in'
    page_doubles = 'https://www.historicosblaze.com/br/blaze/doubles'

    req = session.get(URL, headers=headers)
    soup = BeautifulSoup(req.text, 'html.parser')
    card = soup.find("meta", {"name":"csrf-token"})
    token = card['content']


    dados_login = {
        'authenticity_token': token,
        'user[email]': 'Seu email',
        'user[password]': 'Sua senha',
        'user[remember_me]': '0',
        'button': '',
    }


    response = session.post(URL, headers=headers, data=dados_login)

    if response.status_code == 200:
        print("Login com sucesso")
    else:
        print("Falha no login")


    lista_cores = []

    for i in range(1, 6):
        params = {'page':i}
        #print('Pegando informações', i)
        response1 = session.get(page_doubles, params=params, headers=headers)
        soup = BeautifulSoup(response1.text, 'html.parser')
        cards = soup.find_all("div", {"class":"double-single double-single-exporter border"})
        for corpo in cards:
            cor = corpo.find("span", {"class":"color-table"})
            if cor:
                cor = cor.getText()

            number = corpo.find("span", {"class":"number-table"})
            if number:
                number = number.getText()

            hora = corpo.find("span", {"class":"minute-table"})
            if hora:
                hora = hora.getText()
            
            data = corpo.find("span", {"class":"date-table"})
            if data:
                data = data.getText()

            seed_servidor = corpo.find("span", {"class":"seed-table"})
            if seed_servidor:
                seed_servidor = seed_servidor.getText()
            lista_cores.append({
                'cor': cor,
                'numero': number,
                'hora': hora,
                'data': data,
                'seed_servidor': seed_servidor
            })


    df = pd.DataFrame(lista_cores)
    df.to_csv('historico.csv', sep=';', index=False)
