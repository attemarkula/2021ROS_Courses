#ROS Tekoäly - Luento 01 - 12.1.2021#


## Syväoppiminen ##


## Expert systems ##
-- määritellään mitä pitää tehdä missäkin tapauksessa
-- sääntöjä rajoituksia rajallinen määrä.
-- esim. deep blue -- Kasparov (1996)
-- kallis laajentuessaan

## NLP ##
(Natural language processing)
-- kielen prosessointi sääntöjen perusteella
-- aula chatit (triggeri sanat, jne.)


## Robotics ## 
-- Kalman suodin, jos aula botitkin on niin on kalman suodin.
-- SLAM (simultaneous localisation and mapping)
-- Monet SLAM algoritmit eivät välttämättä ole koneoppimista.

## Compuer Vision ##
-- Vanhemmissa konenäöissä opetetaan ominaisuuksia (expert systems).
-- vanhemmissa laitteissa esim. pieni ARM piiri joka tekee kevyttä hahmotusta, jos edes sitä.
-- tunnistaa esim. muodot, liukuhihnat perustuu tähän, koska teollisuudessa olosuhteet on ennalta vakioitu. (valaistu)
-- ympäristön vakioimisen jälkeen hyviä, edullisia ja tehokkaita.
-- ympäristön muuttuessa (valaistus) ei kykyä mukautumaan.

## Computerized speech recognition ##
- perinteinen puheentunnistus toimii vaihtelevasti
- ei murteita, puhetyyliin vaikea mukautua.

## Machine learning ##
- 10 vuoden aikana muuttuneet monikerros netroverkoksi.
- siirrytty näytönohjainten käyttöön. Rinnakkaistaminen .
- "Back propagation" takaisinlaskenta ja virheen laskenta neuroverkon käyttöön.
- pilkottu "kuva" pienempiin osasiin ja hajautettu laskenta osiin, esim. 224x224x3 -> 7x7x512 -> 1x1000 -> jne.


## Supervised learning ##
- on ennalta oikea ja väärä opetettava vastaus
- kuvien luokittelu
- objektien tunnistus
- segmenttien rakentointi
- regressio-mallit


###Kuvien luokittelu ###
- neuroverkko antaa arvon 0..1
- koira..kissa
- tarvitaan dataa, ongelmasta riippuu paljonko tarvitaan.

- opetuskuvat ( ajetaan toistuvastai verkon läpi n=50..100 )
- opetuskuviin muutoksia kierrosten välillä
- validointi kuvat
- validointikuvalla testataan arvo/virheen suunta muutoksille
- testauskuvat
- testauskuvat oltava erillisiä, jotta eivät opeta neuroverkkoa.

- liiallinen testaaminen voi myös laskea tarkkuutta.

#### Konvoluutio neuroverkko ####

32x32 -> (level0) 8x8 nodea -> Level1 4x4 nodea
Level1 4x4 nodea -> level2 1 node.

Supistetaan neuroverkkoa kunnes yksinkertainen binäärivastaus.

#### Objektien tunnistus ####
- Kokokuvasta tunnistetaan bounding box laatikolla ja prosentilla että mikä kuvassa on.
- asetetaan raja esim 65% ei näytetä osumia.
- tehon nälkäinen tyhjästä opetettuna.
- valmiina neuroverkkoja, voi jatkokehittää.
- käytännössä laskettava 
- "boundingbox on about neliö"

### Kuvan segmentointi ###
- erotellaan tarkemmin kuin neliö ja 
käytetään objektien irroittamiseen taustasta.
- objektien tunnistus, esim väistämisessä.
- joskus riittää pelkkä segementointi tunnistamiseen.


### Regressiomallit ###
- ei välttämättä lineaarinen
- yksinkertainen lineaarinen
- esim. jokainen piste tietyllä tasolla riippuu 
_kaikista toisen tason pisteistä_ 


### Reinforcement learning ###
- mahdollisesti neuroverkkoon perustuva, ei välttämättä.
- pisteytetään suoritukset
- Tavallaan jäljitellään ihmisen oppimistapaa ja dopamiinipalkintoa, vähennetään pisteytystä huonoista suorituksista.
- reinf. learning voi vielä kuukausia opetetaan

## Koneoppimisen kirjastot ##
- Tensorflow (Google),ilmainen acoin kokonaisuus
- Darknet, objektin tunnistukseen (YOLO, You only look once).
- PyTorch Facebookin kehittämä kirjasto.

- KERAS (käyttää tensorflow), helpottaa vielä tensorflown käyttöä.(Google)
- PADAS kirjasto, helpottaa datan käsittelyä, manipulointia. kun tuodaan dataa koneoppimiseen.


Gazebo simulaatiot
- SAMK RobotWars
- robotin paikan selvitys ultraäänisensorien datasta.







Ylim. huomiot:
Puuttuu teollisuuden "juttujen" löytäminen.
- kunnon mallintamine sensoreista
- sensori mesh tuo tuloksen esille.
- 


