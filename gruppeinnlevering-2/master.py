# Teller for hvor mange ganger spilleren velger A.
antall_a = 0
# Teller for hvor mange ganger spilleren skriver noe annet.
antall_ugyldig = 0
# Første del: forteller starten på historien.
print()
print("-----")
print("START")
print()
print("""Prosjektet er kommunens nye digitale portal for innbyggerne.
Det har gått seks uker. Du er Erling, prosjektleder, og teamet er i storming-fasen.
Prototypen skal være klar om tre uker.

Silje (UX-designer) vil ha god brukervennlighet. Elias (IT-rådgiver) tenker på IT-sikkerhet og budsjett.
Uenigheten deres har gått fra en sakskonflikt til en personkonflikt.""")

# Listene inneholder svarene vi godtar for A og B.
a_valg = ["a", "aa", "aaa"]
b_valg = ["b", "bb", "bbb"]

# Valg 1: Erling håndterer konflikten mellom Silje og Elias.
print()
print("-----")
print("BESLUTNING 1 AV 3")
print()
print("""Hva gjør du?
A: Du snakker med Silje og Elias hver for seg, og holder så et strukturert fellesmøte.
B: Du skjærer gjennom med en avstemning i plenum.""")

print()
valg = input("Hva velger du, A eller B? Skriv A eller B: ").lower() # .lower() gjør bokstavene små, så "A" og "a" regnes som det samme.
print()
print("KONSEKVENS:")
if valg in a_valg:
    print("Samtalene kommer tilbake til saken. Konflikten roer seg, og tilliten i teamet er bevart. Men to uker har gått.")
    antall_a += 1    # Hvis spilleren velger A, legger vi til 1 på telleren. Tallet bestemmer hvilken slutt spilleren får.
elif valg in b_valg:
    print("Du får en rask avgjørelse. Men den som tapte, føler seg overkjørt, tilliten er lav, og Silje trekker seg mer unna det faglige samarbeidet.")
else:      # else tar imot alt annet enn A og B.
    print("Det valget finnes ikke. Du gjør ingenting, og konflikten blir værende.")
    antall_ugyldig += 1 # Hvis spilleren skriver noe annet, legger vi til 1 på telleren. Tallet bestemmer hvilken slutt spilleren får.

# Valg 2: Erling håndterer uenigheten mellom Hamdi og Hallgeir.
print()
print("-----")
print("BESLUTNING 2 AV 3")
print()
print("""Samtidig vokser en ny uenighet frem. Hamdi vil ha en kontrollert løsning for folkemøter.
Hallgeir vil ha et mer åpent system med plass til spontane innspill.

Hva gjør du?
A: Du arrangerer en workshop og en testpilot med brukerne.
B: Du venter og ser an situasjonen.""")

print()
valg = input("Hva velger du, A eller B? Skriv A eller B: ").lower()
print()
print("KONSEKVENS:")
if valg in a_valg:
    print("Du arrangerer workshop og testpilot. Brukerne blir hørt, men det krever merarbeid.")
    antall_a += 1    # Hvis spilleren velger A, legger vi til 1 på telleren. Tallet bestemmer hvilken slutt spilleren får.
elif valg in b_valg:
    print("Du venter og ser an situasjonen. Teamet sparer tid nå, men Hallgeir kan føle seg oversett.")
else:      # else tar imot alt annet enn A og B.
    print("Det valget finnes ikke. Du gjør ingenting, og konflikten blir værende.")
    antall_ugyldig += 1 # Hvis spilleren skriver noe annet, legger vi til 1 på telleren. Tallet bestemmer hvilken slutt spilleren får.

# Her velger vi scenario etter hvor mange ganger spilleren har valgt A: 2 = 2.1, 1 = 2.2, 0 = 2.3.
if antall_a == 2:
    print("Begge konfliktene roer seg, og tilliten er bevart. Men tiden som gikk til samtaler og workshop gjør at teamet merker presset før fristen.")
elif antall_a == 1:
    print("Du kommer videre, og stemningen er delvis god. Men uløst spenning ligger fortsatt under overflaten.")
else:      # else tar imot 0.
    print("Tilliten er lav, ingen av årsakene er tatt tak i, og teamet står fast i storming-fasen.")

# Valg 3: Erling velger hvordan han leder teamet i innspurten.
print()
print("-----")
print("BESLUTNING 3 AV 3")
print()
print("""Det gjenstår bare en uke til prototypen skal presenteres for ledelsen.
Du må velge hvordan du leder teamet i innspurten.

Hva gjør du?
A: Du legger vekt på relasjoner og feirer delmål.
B: Du styrer oppgavene strengt og setter fokus på fristen.""")

print()
valg = input("Hva velger du, A eller B? Skriv A eller B: ").lower()
print()
print("KONSEKVENS:")
if valg in a_valg:
    print("Teamet får støtte og beholder motivasjonen, men mindre tid går til produksjon.")
    antall_a += 1    # Hvis spilleren velger A, legger vi til 1 på telleren. Tallet bestemmer hvilken slutt spilleren får.
elif valg in b_valg:
    print("Du får rask fremdrift mot fristen, men det skaper utbrenthet, og samholdet svekkes.")
else:      # else tar imot alt annet enn A og B.
    print("Det valget finnes ikke. Du gjør ingenting, og innspurten går uten tydelig ledelse.")
    antall_ugyldig += 1 # Hvis spilleren skriver noe annet, legger vi til 1 på telleren. Tallet bestemmer hvilken slutt spilleren får.

# Slutten: antall A fra de tre valgene bestemmer hvilken avslutning spilleren får.
print()
print("-----")
print("SLUTT")
print()
if antall_ugyldig >= 2:
    print("""Du har ikke tatt tydelige valg underveis. Teamet mister retningen, og ledelsen mister tilliten til deg.
Du blir fritatt fra rollen som prosjektleder på grunn av manglende handling.""")
elif antall_a == 0:
    print("""Teamet blir stående fast i storming-fasen.
Utbrenthet og svakt samhold gjør at noen føler seg oversett og overkjørt, og nye uenigheter kan stoppe hele prosjektet.""")
elif antall_a == 3:
    print("""Teamet kommer ut av storming-fasen og går videre til norming.
Samholdet og tilliten bærer dere gjennom, men prosjektet blir forsinket fordi tiden var knapp.""")
else:     # else tar imot resten: 1 eller 2 A og færre enn to ugyldige svar, altså delvis håndtering.
    print("Konflikten løses delvis, men samarbeidet er sårbart. Stemningen i teamet er dårlig, og spenningene kan komme tilbake.")