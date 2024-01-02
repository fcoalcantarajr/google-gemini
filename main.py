import pandas as pd

from inserir import *
from gerar_timestamp import *
from gemini import *
from inserir_input import *
from salvar_arquivos import *

def gerar_mensagens(inicial=None):  
    if inicial is None:
        mensagens = [{
            "role": "model",
            "content": "Hello, you are an assistant model."
        }]
    else:
        df = pd.read_csv(inicial, encoding='utf-8-sig')
        mensagens = df.to_json(orient='records',force_ascii=False)
    return mensagens

def main():
    """
    Main function that handles the user interaction.

    Returns: None
    """
    mensagens = gerar_mensagens()
    lista_mensagens = list(mensagens)
    print(mensagens)
    arquivo_txt = iniciar_arquivo_txt()
    arquivo_csv = iniciar_arquivo_csv()
    while True:
        texto = get_multiline_input()
        print("Prompt inserido com sucesso!")
        if texto != 'sair':
            inserir_prompt(lista_mensagens, texto)
            retorno = gemini(mensagens)
            inserir_retorno(lista_mensagens, retorno)
            print(retorno)
            escrever_arquivo(arquivo_txt, texto, retorno)
            salvar_dict(mensagens, arquivo_csv)
        else:
            print('Saindo...')
            break

if __name__ == '__main__':
    main()
