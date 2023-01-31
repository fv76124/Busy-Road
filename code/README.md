# Busy-Road

Wij hebben gebruik gemaakt van 3 algoritmes: 
    Random Algoritme
    Breadth First Algoritme
    Depth First Algoritme

Alle algoritmes zijn te vinden in het solve.py bestand

BELANGRIJK!
Als je de game grootte wilt veranderen naar een andere grootte (6x6 grid naar 9x9 grid) neem dan de volgende stappen:
1. In main.py moet de loadfile veranderd worden naar de gewenste bestandnaam bijv. "Rushhour6x6_1.csv"
2. In Board.py moeten 2 functies aangepast worden:
    - Bij de functie create_board moet de range verandert worden. Als je game 6x6_1 runt dan moet de range voor de
    2 for-loops ook range(6) zijn. Dus als je game 9x9_4 wil runnen moet de range '(9)' worden voor allebei.
    - Bij de functie is_won moet de code verandert worden afhankelijk van welke grootte grid je runt. Als je 6x6 runt
    dan moet de eerste stukje code aanblijven (zie comments bij de code). Als je wil veranderen dan moet je de andere code 
    in een comment plaatsen door te selecteren en CTRL / te gebruiken.

Als je het algoritme wil aanpassen neem de volgende stappen:
1. In main.py staat er een variabel genaamd solver. Achter solver staat welke algoritme je kan runnen. Haal de comment weg
van het algortime dat je wilt runnen en comment het algoritme dat je uit wilt zetten door te selecteren en CTRL / te gebruiken.