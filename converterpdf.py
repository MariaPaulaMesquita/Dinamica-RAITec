import pandas as pd # -> criar e manipular as tabelas extraídas do PDF e para salvar os dados em um arquivo CSV.
import pdfplumber # -> leitura do PDF e extrair as tabelas.

tabelas_extraidas = [] #Aqui, criamos uma lista vazia chamada tabelas_extraidas, 
# que será usada para armazenar as tabelas extraídas de cada página do PDF. Ao
# longo do código, vamos adicionar as tabelas extraídas a essa lista.

with pdfplumber.open("anexo1.pdf") as pdf: #Usa o método open da biblioteca pdfplumber para abrir o
# arquivo PDF chamado anexo1.pdf. A instrução with é usada para garantir que o arquivo seja fechado
# automaticamente após o uso. O objeto retornado por pdfplumber.open() é armazenado na variável pdf, que nos
# permite acessar o conteúdo do PDF, como as páginas e as tabelas.

 for page in pdf.pages: # O .pages é um atributo do objeto retornado ao abrir um PDF. Ele representa todas as
# páginas do arquivo PDF como uma lista de objetos. Aqui, o código percorre todas as páginas do PDF, uma por uma. 
# Para cada página, a variável page irá conter o conteúdo da página atual.

  tabelas = page.extract_tables() #Para cada página, o método extract_tables() do pdfplumber tenta identificar e 
# extrair todas as tabelas presentes. O método retorna uma lista de tabelas, onde cada tabela é representada por 
# uma lista de listas (linhas e colunas). A variável tabelas armazenará todas as tabelas extraídas da página.

  for tabela in tabelas: # O código agora percorre cada tabela dentro da lista tabelas. Mesmo que uma página 
# tenha várias tabelas, esse loop permite que você processe cada uma delas separadamente.
            if tabela: #Aqui, o código verifica se a tabela não está vazia.
                df = pd.DataFrame(tabela[1:], columns=tabela[0])  # pd.DataFrame(): Cria um DataFrame do pandas
# a partir da tabela extraída. O DataFrame é uma estrutura de dados bidimensional (tabela) que facilita a
# manipulação e análise de dados. tabela[1:]: seleciona todas as linhas a partir da segunda linha (ou seja, 
# exclui a primeira linha) da lista de listas. columns=tabela[0] significa que a primeira linha da tabela 
# (ou seja, tabela[0]) será usada como o nome das colunas no DataFrame (cabeçalho). df-> abreviação de DataFrame.
                tabelas_extraidas.append(df) #Aqui, o DataFrame criado df é adicionado (append) à lista tabelas_extraidas.
# Isso garante que todas as tabelas extraídas ao longo das páginas do PDF sejam armazenadas para posterior processamento.

if tabelas_extraidas: #se existir algum dado em tabelas_extraidas. executa:
    resultado = pd.concat(tabelas_extraidas, ignore_index=True) #Usa o pd.concat() para juntar todas as tabelas (DataFrames)
# extraídas em uma única tabela. A opção ignore_index=True garante que o índice das linhas seja reorganizado 
# (recomece do zero), sem se preocupar com os índices originais das tabelas.
    resultado.to_csv("tabelas_extraidas.csv", index=False) #Finalmente, o DataFrame resultante (resultado) é salvo como um 
# arquivo CSV chamado tabelas_extraidas.csv. A opção index=False evita que o índice das linhas seja salvo no arquivo CSV,
# pois como, nesse caso, não é importante que o índice seja preservado, o arquivo CSV ficará mais simples e limpo.