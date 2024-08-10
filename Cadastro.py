from pathlib import Path


def Cadastro(endereco: Path) -> None:
    """ Stores the path on the memory if the path leads to a .mp3 file."""
    from os import path

    # Verifica se o endereço dado é do tipo .mp3 ou .wav.
    if ValideEndereco(endereco):
        with open(path.dirname(path.realpath(__file__)) + "/cadastradas.txt",
                  "a") as cad:
            cad.writelines(endereco + "\n")
    else:
        print("ERRO: endereço inválido.")


def ListarCad() -> list[Path]:
    """ List all the paths that are in the memory.

        Note: if a path stored has changed and it's not valid anymore
        it'll be removed from the memory."""
    from os import path

    cadastradas = list()
    with open(path.dirname(path.realpath(__file__)) + "/cadastradas.txt",
              "r") as cad:
        musCad = cad.readlines()
    cad = 0
    if len(musCad) > 0:
        for x in musCad:
            if ValideEndereco(x.removesuffix("\n")):
                cadastradas.append(x.removesuffix("\n"))
            else:
                RemoverCad(cad)
            cad += 1
        return cadastradas
    else:
        return list()


def ValideEndereco(endereco: Path) -> bool:
    """ Confirm if the path leads to a .mp3 file."""
    from os import path

    # Verifica se o endereco informado existe.
    if endereco.endswith(".mp3"):
        if path.exists(endereco):
            existe = True
        else:
            existe = False
    else:
        existe = False
    return existe


def RemoverCad(indice: int) -> list[Path]:
    """ Remove a path from the memory."""
    from os import path, rename, remove

    # Pega as músicas do cadastro.
    with open(path.dirname(path.realpath(__file__)) + r"/cadastradas.txt",
              "r") as cad:
        cad = cad.readlines()
    # Remove a música de índice selecionado.
    cad.pop(indice)
    # Cria um árquivo (temp.txt) que será o novo arquivo de cadastro.
    with open(path.dirname(path.realpath(__file__)) + r"/temp.txt",
              "w") as temp:
        temp.writelines(cad)
    # Renomeia temp.txt para cadastradas.txt, deleta a antiga cadastradas.txt
    remove(path.dirname(path.realpath(__file__)) + r"/cadastradas.txt")
    rename(path.dirname(path.realpath(__file__)) + r"/temp.txt",
           path.dirname(path.realpath(__file__)) + r"/cadastradas.txt")
    return ListarCad()
