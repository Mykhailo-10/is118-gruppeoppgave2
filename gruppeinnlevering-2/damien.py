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
    print("Men det krever ekstra tid i en allerede presset tidsfrist..")
else:
    print("Erling tvinger frem avstemning. En rask teknisk avklaring er på plass, men taperen føler seg lit overkjørt..")

input("Trykk på Enter for å fortsette...")

# === Beslutnigspunkt 2:Hamdi og Hallgeir ===
print("\nBeslutning 2: Neste utfordring Erling møter er uenighet mellom Hamdi og Hallgeir.")
print ("Uenigheten dreiser seg om folkemøter skal styres strengt eller være mer åpene")
print("\nHvordan håndterer Erling uenigheten mellom Hamdi og Hallgeir?\n")
print("2A: Erling velger å arrangere en Workshop og en testpilot")
print("\n2B: Erling velger å avvente situasjonen og håper at de finner en løsning selv.\n")

svar2= ""

# === lager en while loop som tvinger brukeren til å skrive inn 2A eller 2B for å gå videre.

while svar2 != "2A" and svar2 != "2B":
    svar2 = input("Skriv inn 2A eller 2B for å velge: ")

# === lager en ny IF Else som git brukeren en repsons på deres nye valg. 

if svar2 == "2A":
    print("Erling sikrer at brukerne blir hørt og vil bygge tillit til systemet, men det krever mer arbeid og tid...")
else:
    print("Erling unngår ekstra tidsbruk på ekstra møter i en periode med stram tidsfrist, men kan øke risiko for flere uenigheter...")

input("Trykk på Enter for å fortsette...")

# === Beslutning 3: Det gjenstår bare en uke til første prototypen skal presenteres for ledelsen.

print("\nBeslutning 3: Det gjenstår bare en uke til første prototypen skal presenteres for ledelsen.")
print("Erling må velge overordnet ledelsesstrategi for den siste innspurten\n")
print("3A: Erling kan velge relasjonsfokus og feiring av delmål, men dette krever tid og tar bort fra tid de kan bruke på å fremstille prototypen.\n")
print("3B: Erling kan velge streng oppgavestyring og fristfokus, men dette kan føre til stress og utbrenthet.")

svar3 = ""
 # === lager enda en while loop for å tvinge riktig input fra brukeren.

while svar3 != "3A" and svar3 != "3B":
    svar3 = input("Skriv inn 3A eller 3B for å velge: ")

# === legger til IF og ELSE for å gi brukeren repons basert på valget de tok.

if svar3 == "3A":
    print("Erling velger relasjonsfokus og feiring av delmål. Dette skaper et godt arbeidsmiljø, men kan føre til at prototypen ikke blir ferdig i tide...")
else:
    print("Erling velger streng oppgavestyring og fristfokus. Dette sikrer at prototypen blir ferdig i tide, men kan føre til stress og utbrenthet blant teammedlemmene...")

# === skal ha en input for å la brukeren komme seg videre til sluttresultatet av valgene de tok.

input("Trykk på Enter for å se sluttresulatet av valgene dine...")

score = 0 

# === her er det If statments som sjekker hvilke valg brukeren tok og gir poeng for de beste valgene.

if svar1 == "1A":
    score += 1
if svar2 == "2A":
    score += 1
if svar3 == "3A":
    score += 1  

print("\nSpillets slutt")

# === her er det if, elif og else statments som er brukt for å gi brukeren en feed back på valgene deres. De sjekker om du har enten 3 "riktigte" eller om du har ingen så gir feedback basert på det. 

if score == 3:
    print("Gratulerer! Du har gjort de beste valgene og lykkes med å lede prosjektet til suksess.")
    print("Teamet finner felles normer og samarbeidet blir bra!.")
elif score == 0:
    print("Du har gjort noen dårlige valg, men det er ikke for sent å lære av dem.")
    print("Tilliten i teamer er svekket, og samarbeidet har låst seg helt")
else:
    print("Du har gjort noen gode og noen dårlige valg. Prøv igjen for å oppnå bedre resultat.")
    print("Teamet har blitt påvirket av de dårlige valgene, og samarbeidet er merkelig og krevende.")

print("\nTakk for at du spilte!")
