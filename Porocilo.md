# Kaj je GPS?
Vsi poznamo GPS (Global Positioning System). Uporablja se za lociranje naprav, ki ga podpirajo. Ko govorimo o GPS-u ponavadi mislimo na GNSS (Global navigation satelite system). GNSS je sistem za določanje lokacije s pomočjo več satelitov.
Obstaja več implementacij te tehnologije: 
    -   Ameriški GPS
    -   Ruski GLONASS
    -   Evropski Galileo
    -   Kitajski Beidou
    -   ...

Vsak od teh ima svoje prednosti in slabosti. Vsi imajo manj natančni javni del, ki je namenjen za širšo javnost in natančenjši privatni, namenjen za državne namene. Po natančnosti jih težko razporedimo, saj ima vsak svoje idealne pogoje v katerih je najbolj natančen.


# Kako deluje?

Teoretično potrebujemo za določitev pozicije točke v sistemu razdaljo do treh drugih točk.

Za lociranja neke naprave potrebujemo vsaj 3 satelite. Vsak izmed satelitov izmeri razdaljo do naprave.
<img src="./img/3_intersection.png"/>

Izračun preseka bomo razložili v dveh dimenzijah, ampak se to lepo prenese v tri dimenzije. 

Matematična formula za krožnico je $ (x - x_1)^2 + (y - y_1)^2 = r^r $. Kjer je $ (x_1, y_1) $ središče krožnice, $ r $ pa je polmer. Ko imamo krožnice je z lahkoto izračunati njihov presek.

<img src="./img/3d_intersection.png" />

Ko se pomaknemo v tri-dimenzionalni prostor dobimo iz treh sfer dva preseka. Sateliti v resnici ne zaznavajo povsod okoli sebe, ampak le v smer sprejemnika, zato drugega preseka ne zazna.

V praksi se pojavi problem časovnih zakasnitev. Elektromagnetni valovi ne potujejo naskončno hitro, ampak z svetlobno hitrostjo. S tem pride pri meritvah do napak, zaradi katerih bi bilo lociranje ne natančno. Vsi satelit vsebujejo zelo drage atomične ure z katerimi so sinhronizirani. Problem bi rešili tako, da bi sprejemniki tudi vsebovali atomično, vendar bi bilo to zelo cenovno in energetsko ne ugodno.
V praksi imamo pri lociranju vedno na voljo več kot tri satelite (pet do osem), kar nam omogoča detektiranje napak. 

# Izbolšave GPS
GPS lahko deluje le do enega metra natančno. Zato obstajajo tudi izbolšave.

Primera sta:
- WAAS - "Wide Area Augmentation System"
- DGPS - "Differential GPS"
  
Oba uporablata postaje na površju zemlje, ki omogočajo izbolšave do centimetra natančno, vendar mora biti sprejemnik vedno v dosegu teh postaj.

# Opis naprave (sprejemnik)

# Kje se uporablja

Navigacija
Pomoč pri avtonomni vožnji
Droni
IMU
Traktor
Telefon
Vojaški nameni
Sledenje živalim

# Zgodovina

# Demo

# Sources
https://en.wikipedia.org/wiki/Satellite_navigation#Global_navigation_satellite_systems

https://dewesoft.com/products/interfaces-and-sensors/gps-and-imu-devices
# Ideje

Iphone - galileo + glonass + gps
Traktor - rabi natančnost (amerika je slovenija bl slabo)
IMU - avtomobilsa industija DSImu
DGPS, WAAS - za enhancement