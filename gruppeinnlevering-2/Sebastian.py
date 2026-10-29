import time
 
 
def pause(seconds=1):
    time.sleep(seconds)
 
 
def ask(prompt):
    return input(prompt + " (A/B): ").strip().lower()
 
 
def main():
    points = 0
 
    print("=" * 50)
    print("          Prosjekt Trøbbel")
    print("=" * 50)
    print("Etter 6 uker inn i prosjektet befinner teamet seg i storming-fasen. Første prototypen må leveres om tre uker, og Erling må ta tre avgjørende beslutninger underveis. Gjennom stiavhengighet (path dependency) vil de tidlige valgene få langsiktig konsekvenser for handlingsrommet og samarbeidsklimaet i de etterfølgende scenariene")
    print("Hjelp Erling med sine beslutninger.\n")
    name = input("Hva heter du?").strip()
    if name == "":
        name = "Erling"
    print(f"\nLykke til, {name}...\n")
    pause()
 
    print("--- Beslutning 1: Håndtering av konflikten mellom Silje og Elias ---")
    print("Silje og Elias har kommet i en sakskonflikt om teknologi og design, og det har utviklet seg fra å være saklig til å bli en mer personorientert konflikt. Situasjonen forsterkes siden de begge har en dobbel lojalitet hvor Silje har sitt fagforankrede fokus på brukervennlighet, og Elias vil ivareta kommunens rammer for IT-sikkerhet og kostnader. Erling har tre valgmuligheter han kan ta.")
    print("A) Enesamtaler og strukturert fellesmøte")
    print("B) Skjær gjennom med avstemning i plenum")
    choice = ask("Hva velger du?")
 
    if choice == "a":
        print("Konflikten deeskaleres, og tilliten bevares, men to uker har gått\n")
        points += 3
    elif choice == "b":
        print("Tilliten er lav, og Silje trekker seg mer unna det faglige samarbeidet\n")
        points += 1
    else:
        print("Du tok ikke noe valg og konflikten gikk ikke over av seg selv\n")
        points += 0
    pause()
 
    print("--- Beslutning 2: Spenningen mellom Hamdi og Hallgeir ---")
    print("Samtidig så vokser det frem en uenighet mellom Hamdi og Hallgeir om folkemøter skal styres strengt eller være mer åpen. Dette handler om håndtering av interessenter med ulike forventninger og psykologiske kontrakter")
    print("A) Arrangere en workshop og en testpilot")
    print("B) Avvente situasjonen")
    choice = ask("Hva velger du?")
 
    if choice == "a":
        print("Konfliktene deeskaleres og tilliten blir holdt, men tidsbruken gjør at teamet merker kjøret før fristen\n")
        points += 3
    elif choice == "b":
        print("Fremdrift oppnås og klimaet er delvis opprettholdt, men uløst spenning ligger under overflaten enda\n")
        points += 1
    else:
        print("Tilliten er lav, ingen årsaker er bearbeidet, og teamet er fastlåst i storming-fasen\n")
        points += 0
    pause()
 
    print("--- Beslutning 3: Siste Innspurt ---")
    print("Det gjenstår bare en uke til den første prototypen skal presenteres for ledelsen. Erling må velge overordnet ledelsestrategi for den siste innspurten")
    print("A) Relasjonsfokus og feiring av delmål")
    print("B) Streng oppgavestyring og fristfokus")
    choice = ask("Hva velger du?")
 
    if choice == "a":
        points += 3
    elif choice == "b":
        points += 1
    else:
        print("Uten en beslutning er teamet i sluttfasen uten en plan\n")
        points += 0
    pause()
 
    print("=" * 50)
    print(f"Din poengsum er: {points} / 9")
    print("=" * 50)
    pause()
 
    if points >= 8:
        print("Resultat: Prosjektet er gikk bra")
        print(f"Gratulerer, {name}. Teamet går over i norming med felles normer, tillit og samhold. Prototypen blir likevel noe forsinket.")
    elif points >= 5:
        print("Resultat: Fullført prosjekt med noen uenigheter")
        print(f"Sårbart samarbeid og dårlig stemning. Lignende spenninger kan blusse opp igjen senere.")
    else:
        print("Resultat: Teamet er splittet med uenigheter og dårlige opplevelser")
        print(f"Utbrenthet, og noen føler seg oversett og overkjørt. Høy risiko for at nye uenigheter stopper prosjektet.")
 
    print("\nTakk for innsatsen!")
 
 
if __name__ == "__main__":
    while True:
        main()
        again = input("\nVil du prøve igjen? (yes/no): ").strip().lower()
        if again == "yes" or again == "y":
            print("\n" * 2)
        else:
            print("Adjø!")
            break
        