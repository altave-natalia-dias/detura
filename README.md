# detura
Verificador de Classes de Anotação em Imagens
O script fornecido realiza as seguintes tarefas:

    Lê um arquivo JSON que contém informações sobre imagens e suas anotações.
    Define uma lista de classes de anotação desejadas, incluindo "hardhat", "uniform", "boots", "gloves", "hearing protection", "safety glasses" e "lifejacket".
    Percorre todas as imagens presentes no arquivo JSON.
    Para cada imagem, verifica se o arquivo de imagem correspondente existe.
    Abre a imagem usando a biblioteca PIL.
    Obtém as classes de anotação presentes na imagem a partir do JSON.
    Verifica se todas as classes de anotação desejadas estão presentes nas classes obtidas.
    Exibe mensagens indicando se a imagem está corretamente anotada ou se possui classes de anotação incorretas.
    Mantém um contador para acompanhar o progresso da verificação das imagens.
    No final da verificação, exibe uma mensagem informando o número total de imagens com erros e lista os nomes das imagens com erros, se houver, ou uma mensagem indicando que todas as imagens foram conferidas com sucesso.
