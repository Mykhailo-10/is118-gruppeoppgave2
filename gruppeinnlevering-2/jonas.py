#Jonas sin del - Gruppeinnlevering 02 IS-118
print("Uke 6: Teamet er i storming-fasen. Prototypen skal leveres om tre uker.\n")
 
#Beslutning 1: Silje og Elias
print("Silje og Elias er uenige om teknologi og design, og konflikten er blitt personlig.")
print("A) Enesamtaler og et strukturert fellesmøte")
print("B) Avstemning i plenum")
valg1 = input("Velg A eller B: ").strip().upper()
 
# Gyldig svar: A eller B. Spør på nytt til brukeren svarer riktig.
while valg1 != "A" and valg1 != "B":
    valg1 = input("Ugyldig valg. Skriv A eller B: ").strip().upper()
 
if valg1 == "A":
    print("Konflikten dempes og tilliten bevares, men det tar to uker.\n")
else:
    print("Dere får en rask avklaring, men Silje føler seg overkjørt og trekker seg unna.\n")
 
#Beslutning 2: Hamdi og Hallgeir
print("Hamdi vil ha en kontrollert løsning, Hallgeir vil ha en åpen og dialogbasert løsning.")
print("A) Arrangere workshop og testpilot")
print("B) Vente og se an situasjonen")
valg2 = input("Velg A eller B: ").strip().upper()
 
while valg2 != "A" and valg2 != "B":
    valg2 = input("Ugyldig valg. Skriv A eller B: ").strip().upper()
 
# Scenarioet avhenger av både valg 1 og valg 2
if valg1 == "A" and valg2 == "A":
    print("Begge konfliktene er håndtert og tilliten holder, men teamet merker tidspresset.\n")
elif valg1 == "B" and valg2 == "B":
    print("Ingen av konfliktene er løst. Tilliten er lav og teamet står fast i stormen.\n")
else:
    print("Dere har fremdrift, men uløst spenning ligger under overflaten.\n")
 
#beslutning 3: innspurt
print("Én uke igjen til prototypen skal presenteres for ledelsen.")
print("A) Fokus på relasjoner og feiring av delmål")
print("B) Streng oppgavestyring og fokus på fristen")
valg3 = input("Velg A eller B: ").strip().upper()
 
while valg3 != "A" and valg3 != "B":
    valg3 = input("Ugyldig valg. Skriv A eller B: ").strip().upper()
 
#Utfall: bestemmes av alle tre valgene
print("\nUTFALL:")
if valg1 == "A" and valg2 == "A" and valg3 == "A":
    print("Teamet når norming-fasen med tillit og felles normer. Prototypen blir litt forsinket.")
elif valg1 == "B" and valg2 == "B" and valg3 == "B":
    print("Teamet er utbrent, flere føler seg overkjørt, og prosjektet står i fare for å stoppe.")
else:
    print("Fristen nås, men samarbeidet er sårbart og konfliktene kan blusse opp igjen.")
 
print("Dine valg:", valg1, valg2, valg3)