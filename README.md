# Double Blaze

o Script acessa o site historicosblaze.com usando a biblioteca Python requests. A biblioteca requests permite enviar solicitações HTTP e interagir com páginas da web, o que é essencial para este código, pois ele precisa acessar e coletar dados do site para realizar sua análise. Usando requests, seu código é capaz de se conectar ao site, recuperar as informações necessárias e armazená-las em um formato que pode ser usado para análise adicional. Em seguida, ele faz o login com uma conta, acessa a página do jogo Double e coleta os últimos 1800 registros do jogo usando o BeautifulSoup e armazena tudo em um arquivo csv. Após isso, ele roda a função de probabilidade e tenta calcular a frequência relativa e calcular a probabilidade das próximas cores cair na sequência, analisando os últimos 1800 jogos.


## Recursos utilizados

- [Requests](https://pypi.org/project/requests/) A biblioteca requests permite enviar solicitações HTTP e interagir com páginas da web.
- [Pandas](https://pandas.pydata.org/) para manipulação de dados
- [BeautifulSoup](https://pypi.org/project/beautifulsoup4/) BeautifulSoup é uma biblioteca Python para extrair dados de páginas web, navegar e modificar arvores de HTML/XML. Utilizado em conjunto com requests para coletar dados de uma pagina web.


## Como usar

- Clone este repositório
- Adicione suas credenciais como seu Email e Senha do site
- Execute o script com python probabilidade.py

## Observações

- Certifique-se de ter as bibliotecas necessárias instaladas antes de executar o script.
- É altamente recomendado testar o script em um ambiente de desenvolvimento antes de usá-lo em produção.


## Atenção 
- AVISO: Este script de análise de jogos é apenas para fins educacionais. Não me responsabilizo por quaisquer perdas financeiras decorrentes do uso deste código. Use-o por sua conta e risco.


  ![Blaze](https://th.bing.com/th/id/OIP.sIsGbwPHzrMo97UR0Eq0uAHaES?pid=ImgDet&rs=1)
