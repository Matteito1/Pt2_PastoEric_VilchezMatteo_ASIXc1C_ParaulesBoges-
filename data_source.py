"""
    Eric Pasto i Matteo Vilchez.
    19/03/2024
    ASIXc 1B  M03 UF2 A1
    ParaulesBoges Pt.1
    És l’encarregada d’obtenir les dades. En aquesta versió les demanarà per teclat.
    Tot i que és probable, que en posteriors versions, demani les dades per fitxer.
"""
import crazy_words

def getDataFromKeyboard():
    crazy_words.Texto_Ordenado, crazy_words.introduirfrase = crazy_words.introduirfrase()
    crazy_words.palabras = crazy_words.separar()
    crazy_words.frase_Desordenado = crazy_words.juntar()
    crazy_words.resultado()

def getDataFromChatGPT():
    pass

def getDataFromServer():
    pass
