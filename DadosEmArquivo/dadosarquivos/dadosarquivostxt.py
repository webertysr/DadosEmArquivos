#Weberty Souza Rodrigues
#Cadastro de Cliente usando arquivo de texto .txt, com Tratamento de Erros e Exceções, uso de data automatica no cadastro, E Requisicao de endereco atraes de site de CEO.
from datetime import datetime
import requests


diretorio = '/Users/webetysouza/Documents/'  #variavel global para definir o diretorio onde sera gravado o arquivo.

#Requisição de Endereço através de requests de site de CEP usando json
def endereco_cep(cep,numero):
    response = requests.get('https://viacep.com.br/ws/{}/json/'.format(cep))
    endereco = response.json()

    #Filtrando Apenas Informações relevantes do json
    return endereco['cep'], endereco['logradouro'], numero, endereco['bairro'], endereco['localidade'], endereco['uf']

#Criando a Classe Arquivo.

class Arquivo:
    def __init__(self):
        pass


    def criar_arquivo(diretorioEnome):              #Criar novo arquivo
        arquivo = open(diretorioEnome, 'w')
        arquivo.close()

    def escrever_arquivo(texto,diretorioEnome):      #Inserindo Novo Cliente
        arquivo = open(diretorioEnome, 'a')
        arquivo.write(texto)
        arquivo.close()


    def ler_arquivo(diretorio):                 #Lendo um Arquivo
        arquivo = open(diretorio, 'r')
        texto = arquivo.read()
        print(texto)
        input('\nAperte ENTER Para Sair')

#Tratando Erros e Lidando com Exceções.
class Error(Exception):
    pass
class Tratamento_Error(Error):
    def __init__(self,message):
        self.message = message

if __name__ == '__main__':
  #Loop de Repeticao do Menu.
     menu = 0
     while menu != 4:

        while True: #Tratando um erro de entrada
            try:
                print('---MENU---\n')
                print(' 1-Criar Novo Arquivo\n 2-Cadastrar Cliente\n 3-Ler Arquivo\n 4-Sair\n')
                menu = int(input('Informe uma Opção: '))
                if menu < 1 or menu > 4:
                    raise Tratamento_Error('A Opção NÃO Pode Ser Diferente de: 1, 2, 3 ou 4.')
                break
            except ValueError:
                print('Valor Inválido. Deve-se Digitar Apenas Números.')
            except Tratamento_Error as ex:
                print(ex)
        if menu == 1:
            nome_arquivo = input('Informe o Nome do Arquivo: ') + '.txt'
            diretorioEnome = '{}{}'.format(diretorio,nome_arquivo)
            Arquivo.criar_arquivo(diretorioEnome) #CHama a Funcao criar arquivo.
            print('O Arquivo: ' + nome_arquivo + ' Foi Criado!')
            input('\nAperte ENTER Para Sair')
        elif menu == 2:
            print('\nSe o Arquivo Não existir, Ele será Criado!\n')
            nome_arquivo = input('Informe o Nome do Arquivo: ') + '.txt'
            diretorioEnome = '{}{}'.format(diretorio, nome_arquivo)
            nome_cliente = input('\nInforme o Nome do Cliente: ').upper() #Transforma Todo o Nome em Letra Maiuscula.
#Parte                          #rua = input('Informe o Endereço: \nRua: ')
#comentada                      #numero = input('\nInforme o Numero: ')
#se necessario                  #bairro = input('\nBairro: ')
#entrar com                     #cidade = input('\nInforme a Cidade: ')
#endereco manual descomente     #endereco_cliente = 'Rua: ' + rua + ' Num: ' + numero + ' Bairro: ' + bairro + ' Cidade: ' + cidade
            contador = 0
            while True:  # Tratando um erro de entrada para o CEP. So aceitara 8 numeros sem espacos e sem letras ou caracteres.
                try:
                    cep = input('Informe o CEP: ')
                    contador = len(cep)
                    if contador != 8:
                        raise Tratamento_Error('Valor Inválido. Deve-se Digitar Apenas 8 Números, sem espaços e sem traço.')
                    else:
                        for x in range(8):
                            a = cep[x]
                            if a < chr(48) or a > chr(57):
                                raise Tratamento_Error('Valor Inválido. Deve-se Digitar Apenas 8 Números, sem espaços e sem traço.')
                        break
                except Tratamento_Error as ex:
                    print(ex)
            numero = input('Informe o numero da sua residencia: ')
            endereco_porcep = endereco_cep(cep, numero)
            telefone_cliente = input('Informe o Telefone do Cliente: ')
            data = datetime.now()  #Comando para pegar a Data e Hora atual
            data_cadastro = data.strftime('%d/%m/%Y')
            cadastro = '\nNome do Cliente: ' + nome_cliente + ' Endereço do Cliente: ' + '{}'.format(endereco_porcep) + ' Telefone do Cliente: ' + telefone_cliente + ' Data do Cadastro: ' + data_cadastro
            Arquivo.escrever_arquivo(cadastro,diretorioEnome) #CHama a Funcao de cadastro de novo Cliente.
            input('Aperte ENTER Para Sair:')

        elif menu == 3: #Tratamento de Erro de Nome de Arquivo ou Arquivo Inexistente
            while True:
                try:
                    nome_arquivo = input('Informe o Nome do Arquivo: ') + '.txt'
                    diretorioEnome = '{}{}'.format(diretorio,nome_arquivo)
                    Arquivo.ler_arquivo(diretorioEnome)  # Funcao para ler o Arquivo
                    break
                except FileNotFoundError:
                    print('Arquivo Inválido ou Não Encontrado: ')
                except Tratamento_Error as ex:
                    print(ex)



