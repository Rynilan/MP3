from tkinter import (
    Label,
    Toplevel,
    Button,
    Frame,
    Tk,
    Scrollbar
)
from control.Configuracoes import (
    pegar_texto,
    pegar_configuracoes
)
from control.secao_sobre import texto_sobre


class Sobre:
    """ Create a toplevel window to show the about text."""

    def __init__(self: object, master: Tk) -> None:
        self.master = master
        self.toplevel: Toplevel = Toplevel()
        self.toplevel.destroy()

    def criar(self: object) -> None:
        self.toplevel.destroy()
        self.css(self.html(self.master))

    def html(self: object, master: Tk) -> tuple:
        """ Method to create and position all the elements of the window."""
        elementos: list = list()
        elementos.append(Toplevel(master))
        master = elementos[-1]
        elementos.append(Button(master, command=self.kill))
        elementos.append(Label(master))
        for elemento in elementos:
            if type(elemento) is Toplevel:
                pass
            elif type(elemento) is Button:
                elemento.pack(side='bottom', fill='x')
            else:
                elemento.pack()
        self.elementos: tuple = elementos
        self.toplevel = elementos[0]
        return elementos

    def css(self: object, elementos: object) -> None:
        configuracoes: tuple[str] = pegar_configuracoes()
        texto: tuple[str] = pegar_texto(configuracoes[0])
        for elemento in elementos:
            tipo = type(elemento)
            if tipo is Button:
                elemento.config(bg=configuracoes[5][0],
                                fg=configuracoes[5][1],
                                text=texto[8])
            elif tipo is Label:
                elemento.config(bg=configuracoes[5][0],
                                fg=configuracoes[5][1],
                                text=texto_sobre(configuracoes[0]))

            else:
                elemento.config(bg=configuracoes[5][0])
                elemento.title(texto[14])

    def kill(self: object) -> None:
        self.elementos[0].destroy()
