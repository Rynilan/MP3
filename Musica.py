from pathlib import Path
from threading import Event
from pygame import mixer, init


class Musica:
    """ Transform a path into a music object

        endereco: Path | None = None
    """
    init()
    mixer.init()

    def __init__(self: object, endereco: Path | None = ""):
        self.pos = "00 : 00"
        self.posSegundo = 0

        self.duracao = "-- : --"
        self.duracaoSegundo = 0

        self.toca = Event()
        self.info = False

        self.endereco = endereco
        self.nome = endereco[endereco.rfind("/") + 1: endereco.rfind(".")]

    def Info(self: object) -> None:
        """ Add the information of the music when it is more
            convenient"""
        endereco = self.endereco
        musica = mixer.Sound(endereco)
        duracaoSegundo = int(musica.get_length())
        duracao = str()
        if len(str(duracaoSegundo // 60)) == 1:
            duracao = "0" + str(duracaoSegundo // 60)
        else:
            duracao = str(duracaoSegundo // 60)
        if len(str(duracaoSegundo % 60)) == 1:
            duracao = duracao + " : 0" + str(duracaoSegundo % 60)
        else:
            duracao = duracao + " : " + str(duracaoSegundo % 60)
        self.duracao = duracao
        self.duracaoSegundo = duracaoSegundo
        self.info = True

    def Play(self: object) -> None:
        """ Load and play the music on the stream."""
        if not self.info:
            self.Info()
        if mixer.music.get_busy():
            self.Stop()
        mixer.music.load(self.endereco)
        mixer.music.play()

    def Stop(self: object) -> None:
        """ Stop and unload the music from the stream."""
        mixer.music.stop()
        mixer.music.unload()
        self.toca.set()

    def terminou(self: object) -> None:
        """ Test if the stream is busy during the stream play,
            and when it end set the event of 'toca'."""
        if not mixer.music.get_busy():
            self.toca.set()

    def posicao(self: object) -> None:
        """ Get the position of the music in seconds (it doesn't
            return it, just calculate and store it on 'pos' and
            'posSegundo'"""
        if mixer.music.get_busy():
            posicaoSegundo = int(mixer.music.get_pos() // 1000)
            posicao = str()
            if len(str(posicaoSegundo // 60)) == 1:
                posicao = "0" + str(posicaoSegundo // 60)
            else:
                posicao = str(posicaoSegundo // 60)
            if len(str(posicaoSegundo % 60)) == 1:
                posicao = posicao + " : 0" + str(posicaoSegundo % 60)
            else:
                posicao = posicao + " : " + str(posicaoSegundo % 60)
            self.pos = posicao
            self.posSegundo = posicaoSegundo
