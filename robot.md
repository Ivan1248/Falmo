1) Mapiranje prostora i određivanje položaja
	- Model prostora služi određivanju položaja robota i pamćenju informacija o stanju okoline.
	- postupak rekonstrukcije: monokularni SLAM
		- treba se moći izvršavati dovoljno brzo na mobitelu
		- valjalo bi da je gušći radi korisničkog sučelja
		- algoritam:
			- CNN-SLAM:
				(+) gusta rekonstrukcija, robustan, semantička segmentacija
				(-) spor
			- PL-SLAM:
				(+) brz
				(-) rijetka rekonstrukcija
			- ORB-SLAM:
				(+) brz
¸				(-) rijetka rekonstrukcija
			- LSD-SLAM:
				(+) polugusta rekonstrukcija (rubovi)
				(-) sporiji od ORB-SLAM-a
		- još se može iskorištavati: 
			- poznata udaljenost koju robot prijeđe u jednici vremena kao referentna mjera udaljenosti
			- akcelerometar, žiroskop		
	- načini snimanja (ne moraju se međusobno isključivati):
			1. korisnik snimi sve kamerom (jednostavnije za početak)
			2. robot snimi sve
	- prilagođavanje rekonstrukcije na temelju najnovijih snimki robota
	- mogući problemi:
		- početno istraživanje i izgradnja modela dvorišta, promjenjivost oblika biljaka
2) Raspoznavanje
	- prepoznavanje objekata koji smetaju, visoke trave i uključivanje informacija o travi u model prostora
		- konvolucijska mreža - semantička segmentacija
		- razredi: 
			- visoka trava (treba kositi)
			- niska trava, tlo bez trave (moguće kretanje preko takve površine)
			- čovjek ili neka druga životinja koja je jako blizu 
				=> zaustaviti košenje ako je jako blizu i nastaviti kada se udalji ili pratiti i lajati u slučaju mačke
			- ostalo (grm, rupa, zid, stablo, kamen,  ...) 
				=> treba izbjegavati
	- uključivanje semantičkih informacija u rekonstrukciju prostora
	- dodatno/alternativno za bolje prepoznavanje trave:
		- prepoznavanje dubine - određivanje udaljenosti (i pomoću toga visine) biljaka
			- označavanje podataka - snimanje trave uz i bez svjetla - dobivanje dubinske mape
			- kamera s i bez izvora svjetlosti uz kameru (izvor svjetlosti možda obojana svjetleća dioda)
	- prepoznavanje vlažnosti
	- mogući problemi:
		- sjene
		- ekspozicija
3) Korisničko sučelje (program za npr. Android)
	- prikaz rekonstrukcije (s plohama i teksturama)
	- označavanje granica na rekonstrukciji
	- označavanje u korisničkom sučelje gdje je trava visoka/niska ako robot nije dobro prepoznao?
		-> učenje
	- mogućnost ručnog upravljanja (radi testiranja i zabave)
4) Povezivanje
	- WiFi, bluetooth
5) Upravljanje
	- Mobitel upravljačke signale preko utičnice za slušalice šalje jednostavnom elektroničkom sklopu koji pokreće točkove.
	- upravljanje: 
		1) 2 sinusna signala, frekvencijsko područje određuje radnju (3 područja za svaki kanal)
		3) upravljanje motorima za pomicanje h-mostom pomoću L293
6) Ostali dijelovi
	- energija:
		- punjiva baterija, 5V ili 6V
		- fotonaponska čelija
		- ?
	- mehanika:
		- pokretanje:
			- 2 točka
			- za svaki točak motor sa zupčanicima (kako bi se točkovi sporo okretali)
		- košenje: 
			- ?
<!---
5) Hardver-staro
	- verzija s Raspberry PI-jem:
		- maksimalna potrošnja energije:
			* runmyrobot.com: 6800mAh/4h, 3.7V -> 7W
			- Raspberry Pi 3 (CPU 100%): 730mA (5V) -> 3.65W
			- kamera:
				- RPi-kamera: 260mA -> 1.3W
				- USB-kamera: 260mA -> 1.3W
			- WiFi: 2.5W
			- ukupno: 3.65W + 1.3W + 2.5 = 7.45W
		- dijelovi:
			- elektronika:
				- računalo: Raspberry Pi 3 B
				- kamera: USB-kamera
				- LED uz kameru?
				- senzor za gašenje računala u slučaju slabe baterije
			- energija:
				- punjiva baterija, 5V
				- fotonaponska čelija
			- mehanika:
				- pokretanje:
					- 2 točka
					- za svaki točak motor s prijenosom (kako bi se točkovi sporije okretali)
				- košenje:
					- motor
					- dio za rezanje: čep s komadom žice
		- mogući problemi:
			- Raspberry PI je preslab
			- podaci za učenje
			- dijelovi
			- kiša, vjetar
-->
