"""
    Eric Pasto i Matteo Vilchez.
    19/03/2024
    ASIXc 1B  M03 UF2 A1
    ParaulesBoges Pt.1
    És l’encarregada d’obtenir les dades. En aquesta versió les demanarà per teclat.
    Tot i que és probable, que en posteriors versions, demani les dades per fitxer.
"""
import crazy_words

def frase():
    try:
        frase = input("Introduce el texto que quieres desordenar: ")
        frase_ordenada = frase.split()
        return frase_ordenada, frase
    except:
        print("Error - Lo que has introducido es incorrecto")