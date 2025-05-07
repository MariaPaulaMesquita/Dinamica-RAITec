import requests
from bs4 import BeautifulSoup

pagina = requests.get('https://www.gov.br/ans/pt-br/acesso-a-informacao/participacao-da-sociedade/atualizacao-do-rol-de-procedimentos')
dados_pagina = BeautifulSoup(pagina.text, 'html.parser')

# Encontrar todos os links da página com classe 'internal-link'
links = dados_pagina.find_all('a', class_= "internal-link")

# Procurar o link que termina com .pdf
for link in links: # Aqui, eu especifico que procuro um link em links, na variável que foi criada.
  href = link.get('href') # "href", que significa referência de hipertexto, é um atributo da tag "a" (<a>), âncora,
# em que, nessa linha de código, eu puxo, pela âncora (<a) uma referência (href), que é o link do pdf.
  if href and href.endswith('.pdf'): #se href existe (não é nulo) e termina com '.pdf', executa:
        pdf_url = href #armazena o link do pdf na variável "pdf_url"
        break #quebra o laço, pois eu quero apenas o primeiro link pdf.

# Fazer o download do PDF
resposta = requests.get(pdf_url) #cria outra variável "resposta" para a biblioteca requests fazer uma 
# requisição HTTP (GET) para o link do PDF armazenado na variável pdf_url. A resposta do servidor será
# armazenada na variável resposta.
with open('anexo1.pdf', 'wb') as f: #Essa linha abre um arquivo no modo de escrita binária ('wb') e o 
# prepara para receber os dados do PDF. 'anexo1.pdf' é o nome do arquivo onde o PDF será salvo. Se o 
# arquivo não existir, ele será criado. 'wb' significa "write binary" (escrever em modo binário). 
# Isso é necessário porque estamos lidando com um arquivo binário (PDF) e não com texto.
# with é usado para garantir que o arquivo seja automaticamente fechado depois de terminado o processo 
# (evitando problemas como o arquivo ficar aberto).
    f.write(resposta.content) #Essa linha escreve o conteúdo do PDF no arquivo que foi aberto.
# A função write() grava os dados binários do PDF no arquivo 'anexo1.pdf'
# resposta.content contém os bytes (dados binários) do PDF, ou seja, o conteúdo real do arquivo PDF que foi baixado.
# A função write() coloca esses bytes dentro do arquivo 'anexo1.pdf'. 
# Ou seja, f.write(resposta.content) escreve o conteúdo do PDF no arquivo do computador.
print('PDF baixado com sucesso!')