#Kolmannen luennon tehtävä#


##Helppo##
Tunnilla tehdyssä esimerkissä käytimme odmometria topicin asentotietoa, parempi kuitenkin olisi käyttää /robot1/imu tietoa.
Muuta datan tallennus nodea, niin että se käyttää orientaatio datana imu tietoa.

##Normaali##
Samassa kansiossa on myös robotti5, siinä on hieman erillainen anturointi, siinä missä robotti1 käyttää
ultraääni sensoreita, on robotti5 varustettu lidarilla, Tee vastaava datan keräys robotti viidelle ja tallenna orientaatio, lidar tieto, sekä ground truth paikkat x ja y.

##Vaikea##
Sama kuin normaalissa, mutta tallenna orientaatio tieto imu:sta. Liäsksi lidaria käyttämällä voidaan koittaa havainnoida myös vastustajan paikka tieto,
Lisää myös vastustajan(robotti1) paikkatiedon ground truth tieto csv tiedostoon.

