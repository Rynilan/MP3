from pathlib import Path


class Musica:
    def __init__(self, endereco: Path | None = ""):
        self.info = False
        self.pos = "00 : 00"
        self.posSegundo = 0
        self.toca = False
        self.endereco = endereco
        self.nome = endereco[endereco.rfind("/") + 1: endereco.rfind(".")]

    def Info(self) -> None:
        import pydub as pd

        endereco = self.endereco
        if endereco.endswith(".mp3"):
            musica, self.tipo = pd.AudioSegment.from_mp3(endereco), "mp3"
        else:
            musica = pd.AudioSegment.from_file(endereco, format=".wav")
            self.tipo = "wave"
        self.duracao = str(len(musica) // 60000)
        self.duracaoSegundo = int(len(musica) / 1000)
        if len(self.duracao) == 1:
            self.duracao = "0" + self.duracao
        if len(str(len(musica) % 60)) == 1:
            self.duracao = self.duracao + " : 0" + str(len(musica) % 60)
        else:
            self.duracao = self.duracao + " : " + str(len(musica) % 60)
        self.info = True

    def Play(self) -> None:

        from os import remove, getcwd
        from pyaudio import PyAudio
        import wave as wv
        from time import time

        if not self.info:
            self.Info()
        musica = self.endereco
        tipo = self.tipo
        if tipo == "mp3":
            musica = self.Temp(musica)
        with wv.open(musica, "rb") as mus:
            audio = PyAudio()
            formato = audio.get_format_from_width(mus.getsampwidth())
            tocador = audio.open(format=formato,
                                 channels=mus.getnchannels(),
                                 rate=mus.getframerate(),
                                 output=True)
            chunk = 1024
            self.data = mus.readframes(chunk)
            self.toca = True
            tempoInicial = time()
            while len(self.data) > 0 and self.toca:
                if self.posSegundo < int(time() - tempoInicial):
                    self.posicao(tempoInicial)
                tocador.write(self.data)
                self.data = mus.readframes(chunk)
            tocador.close()
            self.toca = False
            audio.terminate()
            self.posSegundo, self.pos = 0, "00 : 00"
        if tipo == "mp3":
            remove(getcwd() + "/temp.wav")

    def Temp(self, mp3):

        from pydub import AudioSegment
        from os import getcwd

        mp3 = AudioSegment.from_mp3(mp3)
        mp3.export(getcwd() + "/temp.wav", format="wav")
        return str(getcwd() + "/temp.wav")

    def Stop(self) -> None:
        self.toca = False

    def posicao(self: object, inicio: int) -> None:
        from time import time

        self.posSegundo = int(time() - inicio)
        if len(f"{int((time() - inicio) // 60)}") == 1:
            a = "0" + f"{int((time() - inicio) // 60)}"
        else:
            a = f"{int((time() - inicio) // 60)}"
        if len(f"{int((time() - inicio) % 60)}") == 1:
            b = "0" + f"{int((time() - inicio) % 60)}"
        else:
            b = f"{int((time() - inicio) % 60)}"
        self.pos = a + " : " + b
