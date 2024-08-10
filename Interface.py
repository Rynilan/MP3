from Cadastro import (ListarCad,
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
                     BooleanVar)

from Musica import Musica

from threading import Thread


class Janela:
    """ The window of the music player."""
    framework = Thread()
    ant = [int(), Musica()]
    MusCad = ListarCad()

    def __init__(self, master=None):
        font = ("Exmouth", "30", "bold")
        bg = "#32CD32"
        fg = "#8B4513"

        master["bg"] = bg
        master.title("MP3")
        master.geometry("1366x768")
        master.bind("<Escape>", lambda a: self.Kill(master))

        self.titulo = Label(master,
                            text="Músicas Piratas 3",
                            font=font,
                            fg=fg,
                            bg=bg)
        self.titulo.pack(side="top",
                         fill="x")

        self.sair = Button(master,
                           text="Sair",
                           font=font,
                           fg=fg,
                           bg=bg,
                           activebackground=fg,
                           activeforeground=bg,
                           command=lambda: self.Kill(master))
        self.sair.pack(side="bottom",
                       fill="x")

        self.Cadastro = Frame(master,
                              bg="#FFFACD",
                              borderwidth="5",
                              relief="raised")
        self.Cadastro.place(x=25,
                            y=60,
                            width=700,
                            height=300)

        self.Lista = Frame(master,
                           bg="#40E0D0",
                           borderwidth="5",
                           relief="raised")
        self.Lista.place(x=750,
                         y=60,
                         width=516,
                         height=540)

        self.Opcoes = Frame(master,
                            bg="#B22222",
                            borderwidth="5",
                            relief="raised")
        self.Opcoes.place(x=25,
                          y=385,
                          width=200,
                          height=215)

        self.Tocador = Frame(master,
                             bg="#F0C300",
                             borderwidth="5",
                             relief="raised")
        self.Tocador.place(x=250,
                           y=385,
                           width=475,
                           height=215)

        texto = "Para cadastrar uma música\nindique o seu diretório."
        self.IntroCad = Label(self.Cadastro,
                              text=texto,
                              font=font,
                              fg=fg,
                              bg="#FFFACD")
        self.IntroCad.pack()

        self.CampoCad = Entry(self.Cadastro,
                              fg=fg,
                              bg="#FFFACD",
                              insertbackground=fg,
                              font=("Hack", "12"),
                              width="30")
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
                               fg=fg,
                               bg="#FFFACD",
                               activeforeground="#FFFACD",
                               command=self.Cadastrar,
                               activebackground=fg,
                               font=font,
                               text="Cadstrar",
                               borderwidth="3",
                               relief="raised")
        self.BotaoCad.pack(pady="10")

        self.TituloLista = Label(self.Lista,
                                 text="Músicas Cadastradas:",
                                 font=font,
                                 fg=fg,
                                 bg="#40E0D0")
        self.TituloLista.pack()

        self.BotaoPlay = Button(self.Lista,
                                text="Play",
                                command=lambda: self.Tocar("botao"),
                                font=font,
                                fg=fg,
                                bg="#40E0D0",
                                activebackground=fg,
                                activeforeground="#7FFFD4",
                                relief="raised",
                                borderwidth="3")
        self.BotaoPlay.place(x=50,
                             y=50)

        self.BotaoExc = Button(self.Lista,
                               text="Excluir",
                               command=self.Excluir,
                               font=font,
                               fg=fg,
                               bg="#40E0D0",
                               activebackground=fg,
                               activeforeground="#7FFFD4",
                               relief="raised",
                               borderwidth="3")
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

        self.IntroToc = Label(self.Tocador,
                              bg="#F0C300",
                              font=font,
                              text="Escolha uma música\n -- : -- / -- : --",
                              fg="#FFFFFF")
        self.IntroToc.pack(pady="5")

        self.BarraToc = Label(self.Tocador,
                              bg="#F0C300",
                              font=font,
                              text="[]"*15,
                              fg="#FFFFFF")
        self.BarraToc.pack(pady="5")

        self.BotaoParar = Button(self.Tocador,
                                 bg="#F0C300",
                                 font=("Hack", "16"),
                                 text="Parar",
                                 fg="#FFFFFF",
                                 command=self.Parar,
                                 activebackground="#FFFFFF",
                                 activeforeground="#F0C300")
        self.BotaoParar.pack()

        font = ("Exmouth", "20", "bold")
        # OBS: para obter o valor das BooleanVar 's é necessário
        # usar o método .get()
        self.ciclo = BooleanVar()
        self.OpLoop = Checkbutton(self.Opcoes,
                                  text="Cíclico?",
                                  bg="#B22222",
                                  fg="#000000",
                                  onvalue=True,
                                  offvalue=False,
                                  variable=self.ciclo,
                                  font=font,
                                  highlightthickness=0,
                                  state="disabled")

        self.aleatorio = BooleanVar()
        self.OpAlea = Checkbutton(self.Opcoes,
                                  text="Aleatório?",
                                  bg="#B22222",
                                  fg="#000000",
                                  onvalue=True,
                                  offvalue=False,
                                  variable=self.aleatorio,
                                  font=font,
                                  highlightthickness=0,
                                  state="disabled")

        self.continuo = BooleanVar()
        self.Contin = Checkbutton(self.Opcoes,
                                  text="Continuo?",
                                  bg="#B22222",
                                  fg="#000000",
                                  onvalue=True,
                                  offvalue=False,
                                  variable=self.continuo,
                                  font=font,
                                  command=self.FuncaoOpcoes,
                                  highlightthickness=0)

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
                ant = self.ant
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
        if self.continuo.get() is True and not ant.toca.is_set():
            self.Tocar("continuo")
        else:
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
