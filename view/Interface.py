from control.Cadastro import (ListarCad,
                              Cadastro,
                              ValideEndereco,
                              RemoverCad)

from tkinter import (Frame,
                     Label,
                     Button,
                     Entry,
                     Listbox,
                     Scrollbar,
                     Checkbutton,
                     BooleanVar,
                     Tk)

from control.Musica import Musica

from codecs import decode

from control.Configuracoes import (pegar_texto,
                                   pegar_configuracoes,
                                   mudar_configuracoes)

from threading import Thread


class Janela:
    """ The window of the music player."""
    framework = Thread()
    ant = [int(), Musica()]
    MusCad = ListarCad()

    def __init__(self: object, master: Tk) -> None:
        self.html(master)
        self.css()

    def css(self: object) -> None:
        """ Give the style for the widgets."""

        from tkinter import Frame, Button, Entry, Label, Checkbutton
        configuracoes: tuple[str] = pegar_configuracoes()
        textos: tuple[str] = pegar_texto(configuracoes[0])
        font: tuple[str] = (configuracoes[3],
                            configuracoes[2],
                            configuracoes[4])

#        fg1: str = configuracoes[5][1]
#        fg2: str = configuracoes[5][6]
#        bgMas: str = configuracoes[5][0]
#        bgCad: str = configuracoes[5][2]
#        bgToc: str = configuracoes[5][4]
#        bgLis: str = configuracoes[5][3]
#        bgOpc: str = configuracoes[5][5]

        elementos: dict = vars(self)

        for atributo, valor in elementos.items():
            if type(valor) not in (BooleanVar, list, Thread):
                match valor.master:
                    case self.Cadastro:
                        fg: str = configuracoes[5][1]
                        bg: str = configuracoes[5][2]
                    case self.Tocador:
                        fg: str = configuracoes[5][6]
                        bg: str = configuracoes[5][4]
                    case self.Lista:
                        fg: str = configuracoes[5][1]
                        bg: str = configuracoes[5][3]
                    case self.Opcoes:
                        fg: str = configuracoes[5][6]
                        bg: str = configuracoes[5][5]
                    case _:
                        fg: str = configuracoes[5][1]
                        bg: str = configuracoes[5][0]
                if type(valor) in (Label, Checkbutton, Entry, Button):
                    valor.configure(bg=bg, fg=fg, font=font)
                if type(valor) is Entry:
                    valor.configure(insertbackground=fg,
                                    width=30,
                                    font=("Hack", "12"))
                elif type(valor) is Frame:
                    valor.configure(bg=bg,
                                    bd="5",
                                    relief="raised")
                elif type(valor) is Button:
                    valor.configure(activebackground=fg,
                                    activeforeground=bg,
                                    bd="3",
                                    relief="raised")
                elif type(valor) is Checkbutton:
                    valor: Checkbutton
                    valor.configure(highlightthickness=0,
                                    fg="#000000",
                                    font=(configuracoes[3],
                                          "18", configuracoes[4]),
                                    onvalue=True,
                                    offvalue=False,
                                    justify="left")
                elif type(valor) is Tk:
                    valor.configure(bg=bg)
                else:
                    pass
        self.Cadastro["bg"] = configuracoes[5][2]
        self.Opcoes["bg"] = configuracoes[5][5]
        self.Lista["bg"] = configuracoes[5][3]
        self.Tocador["bg"] = configuracoes[5][4]
        self.titulo.configure(text=textos[10])
        self.IntroCad.configure(text=textos[0].replace("\\n", "\n"))
        self.BotaoCad.configure(text=textos[1])
        self.Contin.configure(text=textos[2])
        self.OpLoop.configure(text=textos[3])
        self.OpAlea.configure(text=textos[4])
        self.BotaoParar.configure(text=textos[5], font=("Hack", "12"))
        self.TituloLista.configure(text=textos[6])
        self.BotaoPlay.configure(text=textos[7])
        self.BotaoExc.configure(text=textos[8])
        self.sair.configure(text=textos[9])
        self.IntroToc.configure(text=textos[11].replace("\\n", "\n"))
        self.BarraToc.configure(text=textos[12])

    def html(self: object, master: Tk) -> None:
        """ Create and place the widgets on the window."""

        master.title("MP3")
        master.geometry("1366x768")
        master.bind("<Escape>", lambda a: self.Kill(master))
        self.master = master

        self.titulo = Label(master)
        self.titulo.pack(side="top",
                         fill="x")

        self.sair = Button(master,
                           command=lambda: self.Kill(master))
        self.sair.pack(side="bottom",
                       fill="x")

        self.Cadastro = Frame(master)
        self.Cadastro.place(x=25,
                            y=60,
                            width=700,
                            height=300)

        self.Lista = Frame(master)
        self.Lista.place(x=750,
                         y=60,
                         width=516,
                         height=540)

        self.Opcoes = Frame(master)
        self.Opcoes.place(x=25,
                          y=385,
                          width=200,
                          height=215)

        self.Tocador = Frame(master)
        self.Tocador.place(x=250,
                           y=385,
                           width=475,
                           height=215)

        self.IntroCad = Label(self.Cadastro)
        self.IntroCad.pack()

        self.CampoCad = Entry(self.Cadastro)
        self.CampoCad.bind("<Return>",
                           lambda a: self.Cadastrar())
        self.CampoCad.bind("<KP_Enter>",
                           lambda a: self.Cadastrar())
        self.CampoCad.pack(pady="9",
                           ipady="5",
                           fill="x",
                           padx="10",
                           ipadx="5")

        self.BotaoCad = Button(self.Cadastro,
                               command=self.Cadastrar)
        self.BotaoCad.pack(pady="10")

        self.TituloLista = Label(self.Lista)
        self.TituloLista.pack()

        self.BotaoPlay = Button(self.Lista,
                                command=lambda: self.Tocar("botao"))
        self.BotaoPlay.place(x=50,
                             y=50)

        self.BotaoExc = Button(self.Lista,
                               command=self.Excluir)
        self.BotaoExc.pack(anchor="se",
                           padx="50")

        self.barrax = Scrollbar(self.Lista,
                                orient="horizontal",
                                bg="#40E0D0")
        self.barrax.pack(side="bottom",
                         fill="x")
        self.barray = Scrollbar(self.Lista,
                                orient="vertical",
                                bg="#40E0D0")
        self.barray.pack(side="left",
                         fill="y")

        self.CriaLista()

        self.IntroToc = Label(self.Tocador)
        self.IntroToc.pack(pady="5")

        self.BarraToc = Label(self.Tocador)
        self.BarraToc.pack(pady="5")

        self.BotaoParar = Button(self.Tocador,
                                 command=self.Parar)
        self.BotaoParar.pack()

        # OBS: para obter o valor das BooleanVar 's é necessário
        # usar o método .get()
        self.ciclo = BooleanVar()
        self.OpLoop = Checkbutton(self.Opcoes,
                                  variable=self.ciclo,
                                  state="disabled")

        self.aleatorio = BooleanVar()
        self.OpAlea = Checkbutton(self.Opcoes,
                                  variable=self.aleatorio,
                                  state="disabled")

        self.continuo = BooleanVar()
        self.Contin = Checkbutton(self.Opcoes,
                                  variable=self.continuo,
                                  command=self.FuncaoOpcoes)

        self.Contin.pack(expand=True,
                         anchor="w",
                         padx="10")
        self.OpLoop.pack(expand=True,
                         anchor="w",
                         padx="10")
        self.OpAlea.pack(expand=True,
                         anchor="w",
                         padx="10")

    def Kill(self: object, master: Frame) -> None:
        """ Close the program."""
        if self.framework.is_alive():
            self.Parar()
        master.destroy()
        exit(0)

    def CriaLista(self: object) -> None:
        """ Method to create the list box."""
        lista = Listbox(self.Lista,
                        font=("Exmouth", "30", "bold"),
                        fg="#8B4513",
                        bg="#40E0D0",
                        borderwidth="4",
                        relief="sunken",
                        height="10",
                        width="16",
                        yscrollcommand=self.barray.set,
                        xscrollcommand=self.barrax.set,
                        selectmode="single",
                        selectbackground="#00FA9A")
        lista.bind("<Return>", lambda a: self.Tocar("botao"))
        lista.bind("<KP_Enter>", lambda a: self.Tocar("botao"))
        self.barrax["command"] = lista.xview
        self.barray["command"] = lista.yview
        y = int()
        for x in self.MusCad:
            lista.insert(y, x[x.rfind("/") + 1: x.rfind(".")])
            y += 1
        lista.pack(fill="x")
        self.ListaCad = lista

    def Cadastrar(self: object) -> None:
        """ Adds the path of a music on the data storage and
            update the checklist."""
        endereco = self.CampoCad.get()
        if ValideEndereco(endereco):
            Cadastro(endereco)
            self.MusCad = ListarCad()
            self.ListaCad.destroy()
            self.CriaLista()

    def Excluir(self: object) -> None:
        """ Remove a music of the stored data and reload the
            list box."""
        indice = self.ListaCad.curselection()[0]
        if self.ant[0] == indice:
            self.Parar()
        self.sair.focus()
        self.MusCad = RemoverCad(indice)
        self.ListaCad.destroy()
        self.CriaLista()

    def Tocar(self: object, invocador: str) -> None:
        """ Play the music.

            Important: if there's already a music playing it'll
            stop it."""
        framework = self.framework
        if framework.is_alive() and invocador != "continuo":
            self.Parar()
        escolhida = self.Escolha(invocador)
        escolhida = [escolhida, Musica(self.MusCad[escolhida])]
        escolhida[1].Play()
        framework = Thread(target=self.telaTocadora)
        while not escolhida[1].info:
            pass
        self.framework = framework
        self.ant = escolhida
        framework.start()

    def Escolha(self: object, invocador: str) -> int:
        """ Get the music to be played."""
        from random import random

        if invocador == "continuo":
            muslen = len(self.MusCad)
            if self.aleatorio.get():
                ant = self.ant[0]
                escolhida = ant
                while escolhida == ant:
                    escolhida = int(random() * muslen)
            else:
                if self.ant[0] < muslen - 1:
                    escolhida = self.ant[0] + 1
                elif self.ciclo.get():
                    escolhida = 0
        else:
            escolhida = self.ListaCad.curselection()[0]
        return escolhida

    def Parar(self: object) -> None:
        """ Stop the music from playing and wait the thread, framework
            stop."""
        if self.framework.is_alive():
            self.continuo.set(False)
            self.ant[1].Stop()

    def telaTocadora(self):
        """ Method to update the frame who show the music name,
            position, duration and the progress bar.
            Note: It's placed on a thread."""
        ant = self.ant[1]
        introtoc = self.IntroToc
        barratoc = self.BarraToc
        while not ant.toca.is_set():
            ant.posicao()
            introtoc["text"] = ant.nome + "\n" + ant.pos + " / " + ant.duracao
            if ant.posSegundo % (ant.duracaoSegundo // 15) == 0:
                inter = int(15 * ant.posSegundo / ant.duracaoSegundo)
                barratoc["text"] = "[]" * inter + "--" * (15 - inter)
            ant.terminou()
        if self.continuo.get() is True:
            self.Tocar("continuo")
        else:
            if self.OpLoop.cget("state") == "normal":
                self.continuo.set(True)
            introtoc["text"] = "Escolha uma música\n -- : -- / -- : --"
            barratoc["text"] = "[]" * 15

    def FuncaoOpcoes(self):
        """ Method to activate the others two checkboxes
            activated when the first checkbox is activated."""
        if self.continuo.get():
            self.OpAlea["state"] = "normal"
            self.OpLoop["state"] = "normal"
        else:
            self.OpAlea["state"] = "disable"
            self.OpLoop["state"] = "disable"
