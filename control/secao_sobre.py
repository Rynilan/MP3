from os import path


def texto_sobre(idioma: str) -> str:
    ''' Returns a formatted string containing all the text of the about file.
    '''

    endereco: str = path.dirname(
        path.realpath(__file__)
    ).removesuffix("/control") + r'/model/config/idiomas/sobre_{}.txt'.format(
            idioma
        )
    with open(endereco) as sobre:
        linhas: list[str] = sobre.readlines()
        texto: str = ""
    for linha in linhas:
        texto += linha
    return texto
