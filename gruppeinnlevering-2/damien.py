# === 1. Introduksjon ===
print("Velkommen til Erlings prosjekt!")
print("Erling er midt i et veldig krevenede prosjekt som innvolverer mange ulike mennesker.")
print("Gruppen hans har fått litt vanskeligheter og stemninger er spent.\n")

# bruker \n for å lage litt luft mellom print og input som komme runder.
input("trykk på Enter for å fortsette...\n")

# === input med trykk Enter for å la bruker lese teksten før den går videre.

print("Beslutning 1: Hvordan skal Erling håndtere den første utfordringen?\n")
print("1A: Enesamtaler og strukturert fellesmøte.\n")
print("1B: skjære gjennom med avsteming i plenum.\n")
svar1 = ""

# lager en while loop som tvinger brukeren til å skrive inn 1A eller 1B for å gå bidere. 

while svar1 != "1A" and svar1 != "1B":
    svar1 = input("Skriv inn 1A eller 1B for å velge:")


