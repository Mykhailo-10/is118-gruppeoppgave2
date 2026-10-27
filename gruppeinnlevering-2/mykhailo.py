# Første del: forteller starten på historien.
print("""Prosjektet er kommunens nye digitale portal for innbyggerne.
Det har gått seks uker siden teamet startet.
Du er Erling, prosjektleder.
Teamet er nå i storming-fasen.
Den første prototypen skal være klar om tre uker.
Resten av teamet følger med.

Silje er UX-designer og vil ha god brukervennlighet og godt design.
Elias er IT-rådgiver og tenker på IT-sikkerhet og budsjett.
Uenigheten deres har gått fra en sakskonflikt til en personkonflikt.
Begge søker støtte hos sine nærmeste i teamet.

Hva gjør du?
A: Du snakker med Silje og Elias hver for seg, og holder så et strukturert fellesmøte.
B: Du skjærer gjennom med en avstemning i plenum.""")  

# Listene inneholder svarene vi godtar for A og B.
a_valg = ["a", "aa", "aaa"]
b_valg = ["b", "bb", "bbb"]

# Andre del: valget. Vi henter svaret fra spilleren, og programmet viser ulikt resultat avhengig av valget.
valg = input("Hva velger du, A eller B? Skriv A eller B: ").lower() # .lower() gjør bokstavene små, så "A" og "a" regnes som det samme.

antall_a = 0

if valg in a_valg:         
    print("Samtalene kommer tilbake til saken, og tilliten i teamet blir bedre. Men det tar tid, og dere har dårlig tid.")
    antall_a += 1
elif valg in b_valg:
    print("Du får en rask avgjørelse. Men den som tapte, føler seg overkjørt, og samholdet blir svakere.")
else:      # else tar imot alt annet enn A og B.
    print("Det valget finnes ikke. Du gjør ingenting, og konflikten blir værende.")

print(f"Dine poengene: {antall_a}")

