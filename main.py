# encoding: utf-8

from Xlib.display import Display
from Xlib import X
from Xlib.protocol.event import KeyPress

# Imports para reprodução de audio
import pyaudio, array, math

# Botão Esquerdo: 1
# Botão Direito: 3
botoes_ref = [1, 3]
botoes = ["Botão Esquerdo", "Botão Direito"]

# Tecla A: 38
# Tecla S: 39
# Tecla D: 40
# Tecla F: 41
# Tecla G: 42
# Tecla W: 25
# Tecla Espaço: 65
teclas_ref = [38, 39, 40, 41, 42, 25, 65]
teclas = ["A", "S", "D", "F", "G", "W", "Espaço"]

# Cima: 111
# Baixo: 116
# Esquerda: 113
# Direita: 114
setas_ref = [111, 116, 113, 114]
setas = ["Cima", "Baixo", "Esquerda", "Direita"]

# Captura de teclado e mouse
display = Display(':0')
root = display.screen().root

root.grab_pointer(True, X.ButtonPressMask, X.GrabModeAsync, X.GrabModeAsync, 0, 
                    0, X.CurrentTime)
root.grab_keyboard(True, X.GrabModeAsync, X.GrabModeAsync, X.CurrentTime)


# Reprodução de som
p = pyaudio.PyAudio()
stream = p.open(rate=44100, channels=1, format=pyaudio.paFloat32, output=True)

while True:
    event = display.next_event()
    # Para evitar o erro de mudança de source (e.g. maKey maKey pra teclado)
    try:    
        e = event.detail
    except:
        continue

    # Caso precise verificar numeros de tecla, descomentar a linha abaixo
    #print e

    # Botões
    if e in botoes_ref:
        print botoes[botoes_ref.index(e)] + " clicado."
    # Teclas
    elif e in teclas_ref:
        if isinstance(event, KeyPress):
            print "Tecla " + teclas[teclas_ref.index(e)] + " pressionada."
            stream.write(array.array('f',
            ((teclas_ref.index(e) * 2) * math.sin(i / float(10.)) for i in range(44100))).tostring())
    # Setas
    elif e in setas_ref:
        if isinstance(event, KeyPress):
            print "Seta para " + setas[setas_ref.index(e)] + " pressionada."
    else:
        break
        stream.close()
        p.terminate()
        #continue
