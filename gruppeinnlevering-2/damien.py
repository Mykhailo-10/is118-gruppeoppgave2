# === 1. Introduksjon ===
print("Velkommen til Erlings prosjekt!")
print("Erling er midt i et veldig krevenede prosjekt som innvolverer mange ulike mennesker.")
print("Gruppen hans har fått litt vanskeligheter og stemninger er spent.\n")
print("Silje og Elias har havnet i en opphetet konflikt om teknologi og design.")
print("silje kjemper for brukervennlighet, mens Elias skal ivareta IT-sikkerhet og kostnader.\n")

# bruker \n for å lage litt luft mellom print og input.

input("trykk på Enter for å fortsette...\n")

# === input med trykk Enter for å la bruker lese teksten før den går videre.

print("Beslutning 1: Hvordan skal Erling håndtere den første utfordringen?\n")
print("1A: Enesamtaler og strukturert fellesmøte.\n")
print("1B: skjære gjennom med avsteming i plenum.\n")
svar1 = ""

# lager en while loop som tvinger brukeren til å skrive inn 1A eller 1B for å gå bidere. 

while svar1 != "1A" and svar1 != "1B":
    svar1 = input("Skriv inn 1A eller 1B for å velge:")

# === skal lage if og else for å gi brukeren en respons basert på deres valg.

if svar1 == "1A":
    print("Erling velger å ha enesamtaler og et strukturert fellesmøte. Dette hjelper med å få samtalen tilbake til saklig tema.")
else:
    print("Erling tvinger frem avstemning. En rask teknisk avklaring er på plass, men taperen føler seg lit overkjørt..")

input("Trykk på Enter for å fortsette...")

# === Beslutnigspunkt 2:Hamdi og Hallgeir ===
print("\nNeste utfordring Erling møter er uenighet mellom Hamdi og Hallgeir.")
print ("Uenigheten dreiser seg om folkemøter skal styres strengt eller være mer åpene")
print("\nBeslutning 2: Hvordan håndterer Erling uenogheten mellom Hamdi og Hallgeir?\n")
print("2A: Erling velger å arrangere en Workshop og en testpilot")
print("\n2B: Erling velger å avvente situasjonen og håper at de finner en løsning selv.\n")



