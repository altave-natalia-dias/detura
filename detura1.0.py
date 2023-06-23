import json
from PIL import Image
import os

# Caminho para o arquivo JSON com todas as informações
caminho_json = "/home/Área de Trabalho/json/instances_default.json"

# Classes de anotação desejadas
classes_desejadas = ["hardhat", "uniform", "boots", "gloves", "hearing protection", "safety glasses", "lifejacket"]

# Caminho para os frames a serem validados
caminho_imagem = "/home/Área de Trabalho/frames"


# Função para verificar se as classes de anotação estão corretas
def verificar_classes_imagens(caminho_json, caminho_imagem):
    # Abre o arquivo JSON e carrega os dados
    with open(caminho_json, "r") as arquivo:
        dados_json = json.load(arquivo)

    total_imagens = len(dados_json["imagens"])
    imagens_conferidas = 0
    imagens_com_erro = []

    # Percorre todas as imagens no arquivo JSON
    for imagem in dados_json["imagens"]:
        # Obtém o caminho e o nome da imagem
        nome_imagem = imagem["nome"]

        # Verifica se o arquivo de imagem existe
        if nome_imagem:
            arquivo_imagem = os.path.join(caminho_imagem, nome_imagem)
            if os.path.exists(arquivo_imagem):
                # Abre a imagem usando a biblioteca PIL
                img = Image.open(arquivo_imagem)

                # Obtém as classes de anotação presentes na imagem
                classes_presentes = set(imagem["classes"])

                # Verifica se as classes de anotação estão corretas
                if set(classes_desejadas).issubset(classes_presentes):
                    print(f"A imagem {nome_imagem} está corretamente anotada.")
                else:
                    print(f"A imagem {nome_imagem} possui classes de anotação incorretas.")
                    imagens_com_erro.append(nome_imagem)
            else:
                print(f"A imagem {nome_imagem} não foi encontrada.")
                imagens_com_erro.append(nome_imagem)
        else:
            print("Nome da imagem não fornecido.")
            imagens_com_erro.append("Imagem sem nome")

        # Atualiza o contador
        imagens_conferidas += 1
        print(f"Imagens conferidas: {imagens_conferidas}/{total_imagens}")

    # Exibe a mensagem de conclusão
    print("Verificação concluída.")
    if imagens_com_erro:
        print(f"Número de imagens com erros: {len(imagens_com_erro)}")
        print("Imagens com erros:")
        for erro in imagens_com_erro:
            print(erro)
    else:
        print("Todas as imagens foram conferidas com sucesso.")


# Chama a função para verificar as classes de anotação
verificar_classes_imagens(caminho_json, caminho_imagem)

