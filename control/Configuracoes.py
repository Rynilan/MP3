from os import path, rename, remove


def pegar_configuracoes() -> tuple[path]:
    """ Get the value of the configurations of the window, summary:
            language: str = configuracoes[0]
            theme: str = configuracoes[1]
            font_size: str = configuracoes[2]
            font_family: str = configuracoes[3]
            font_characteristic: str = configuracoes[4]
            fg1: str = configuracoes[5][1]
            fg2: str = configuracoes[5][6]
            bgMas: str = configuracoes[5][0]
            bgCad: str = configuracoes[5][2]
            bgToc: str = configuracoes[5][4]
            bgLis: str = configuracoes[5][3]
            bgOpc: str = configuracoes[5][5]

    ."""

    endereco = path.dirname(path.realpath(__file__)).removesuffix("/control")
    with open(endereco + r"/model/config.txt", "r") as config:
        opcoes: list[str] = config.readlines()
    for indice, opcao in enumerate(opcoes):
        opcoes[indice]: str = opcao[opcao.find(":") + 1:].removesuffix("\n")
    with open(endereco + r"/model/config/temas/" +
              opcoes[1] + ".txt", "r") as tema:
        opcoes.append(tema.readlines())
    for indice, cor in enumerate(opcoes[5]):
        opcoes[5][indice]: list[str] = cor[cor.find(":") + 1:].removesuffix("\n")
    opcoes[5] = tuple(opcoes[5])
    return tuple(opcoes)


def mudar_configuracoes(indice: int, valor: str) -> None:
    """ Update the configuration file."""

    endereco: str = path.dirname(
                                    path.realpath(__file__)
                                ).removesuffix(r"/control") + r"/model"
    with open(endereco + r"/config.txt", "r") as config:
        opcoes: list[str] = config.readlines()
        opcoes[indice]: str = opcoes[indice].replace(
            opcoes[indice][opcoes[indice].find(":") + 1:], valor + "\n"
        )
    with open(endereco + r"/temp_config.txt", "w") as config:
        config.writelines(opcoes)
    remove(endereco + r"/config.txt")
    rename(endereco + r"/temp_config.txt", endereco + r"/config.txt")


def pegar_texto(idioma: str) -> tuple[str]:
    """ Get all the text that 'll be displayed on screen."""

    with open(path.dirname(path.realpath(__file__)).removesuffix("/control") +
              r"/model/config/idiomas/{}.txt".format(idioma), "r",
              encoding='utf-8') as texto:
        frases = texto.readlines()
    for indice, frase in enumerate(frases):
        frases[indice] = frase.removesuffix("\n")
    return tuple(frases)
