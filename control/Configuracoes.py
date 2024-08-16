from os import path, rename, remove


def pegar_configuracoes() -> tuple[path]:
    """ Get the value of the configurations of the window."""

    with open(path.dirname(path.realpath(__file__)) +
              r"/config.txt", "r") as config:
        opcoes: list[str] = config.readlines()
    for opcao, indice in enumerate(opcoes):
        opcoes[indice]: str = opcao[opcao.find(":") + 1:]
    return tuple(opcoes)


def mudar_configuracoes(indice: int, valor: str) -> None:
    """ Update the configuration file."""

    endereco: str = path.dirname(path.realpath(__file__))
    with open(endereco + r"/config.txt", "r") as config:
        opcoes: list[str] = config.readlines()
        opcoes[indice]: str = valor
    with open(endereco + r"/temp_config.txt", "w") as config:
        config.writelines(opcoes)
    remove(endereco + r"/config.txt")
    rename(endereco + r"/temp_config.txt", endereco + r"/config.txt")


def pegar_texto(idioma: str) -> tuple[str]:
    """ Get all the text that 'll be displayed on screen."""

    with open(path.dirname(path.realpath(__file__)) +
              r"/{}".format(idioma), "r") as texto:
        return tuple(texto.readlines)
