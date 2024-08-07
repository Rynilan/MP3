from pathlib import Path
from pygame import mixer, init


class Musica:
    init()
    mixer.init()

    def __init__(self: object, endereco: Path | None = ""):
        self.pos = "00 : 00"
        self.posSegundo = 0

        self.duracao = "-- : --"
        self.duracaoSegundo = 0

        self.toca = False
        self.info = False

        self.endereco = endereco
        self.nome = endereco[endereco.rfind("/") + 1: endereco.rfind(".")]

    def Info(self: object) -> None:
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

        if not self.info:
            self.Info()
        if mixer.music.get_busy():
            self.Stop()
        mixer.music.load(self.endereco)
        mixer.music.play()
        self.toca = True

    def Stop(self: object) -> None:
        mixer.music.stop()
        mixer.music.unload()
        self.toca = False

    def terminou(self):
        if mixer.music.get_busy():
            return False
        return True

    def posicao(self: object) -> None:
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
