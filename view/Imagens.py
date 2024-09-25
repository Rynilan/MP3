from PIL import (
    Image,
    ImageTk
)

from os import path


class Imagens:
    """ A class just to store the images that 'll be used on the screen."""

    def __init__(self: object) -> None:
        endereco: str = path.dirname(path.realpath(__file__)).removesuffix(
                        "/view") + r'/model/config/icons/{}.png'
        tamanho: tuple[int, int] = (16, 16)
        self.claro = ImageTk.PhotoImage(
            Image.open(endereco.format("claro")).resize(tamanho)
        )
        self.escuro = ImageTk.PhotoImage(
            Image.open(endereco.format("escuro")).resize(tamanho)
        )
        self.pausar_continuar = ImageTk.PhotoImage(
            Image.open(endereco.format("pausar_e_continuar")).resize(tamanho)
        )
        self.parar = ImageTk.PhotoImage(
            Image.open(endereco.format("parar")).resize(tamanho)
        )
        self.proximos_10 = ImageTk.PhotoImage(
            Image.open(endereco.format("proximos_10")).resize(tamanho)
        )
        self.anteriores_10 = ImageTk.PhotoImage(
            Image.open(endereco.format("anteriores_10")).resize(tamanho)
        )
