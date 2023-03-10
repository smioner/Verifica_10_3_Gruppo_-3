def Verifica_10_3_Gruppo_1(nome, cognome):
    """Restituisce una stringa di saluto con nome e cognome"""
    return f"Ciao {nome} {cognome}, piacere di conoscerti!"
  
  nome_utente = input("Inserisci il tuo nome: ")
cognome_utente = input("Inserisci il tuo cognome: ")
saluto = Verifica_10_3_Gruppo_1(cognome_utente,nome_utente)
print(saluto)

Verifica_10_3_Gruppo_1()
