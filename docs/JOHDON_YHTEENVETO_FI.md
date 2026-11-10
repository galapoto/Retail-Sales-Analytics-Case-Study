# Liiketoiminta-analyysi: vähittäiskaupan myynti, peruutukset ja datan laatu

**Aineisto:** UCI Online Retail, Iso-Britannia 2010–2011, Chen (2015), CC BY 4.0. **Analyysi varmennettu:** 10.11.2026 GitHub Actionsissa alkuperäisellä 541 909 rivin aineistolla.

## Tavoite

Miten yritys voi seurata historiallista tilausmyyntiä, tunnistaa merkittäviä markkinoita ja tuotteita sekä varmistaa, että puutteelliset lähtötiedot eivät johda vääriin päätöksiin?

## Todelliseen lähdedataan perustuvat tulokset

| Mittari | Tulos |
|---|---:|
| Lähdeaineiston tapahtumarivit | **541 909** |
| Myyntirivit laaduntarkastusten jälkeen | **524 878** |
| Yksilölliset myyntilaskut | **19 960** |
| Bruttomyynti ennen palautuksia ja kustannuksia | **10 642 110,80 £** |
| Keskimääräinen tilausarvo | **533,17 £** |
| Peruutusrivien laskennallinen arvo | **893 979,73 £** |
| Täsmälleen päällekkäiset rivit | **5 268** |
| Asiakastunnuksen puuttuminen lähderiveiltä | **135 080** |

Mittarit on täsmäytetty Pandas-laskennan ja erillisen SQL-kyselyn välillä. [Lähdetulokset ja kuviot](../results/uci/README.md).

## Johtopäätökset

1. **Datan laatu vaikuttaa raportointiin.** Duplikaatit ja puuttuvat asiakastunnisteet on käsiteltävä näkyvästi ennen raportointia. Asiakastunnukseton rivi ei automaattisesti vastaa uutta asiakasta.
2. **Bruttomyynti ei ole voittoa.** Aineistossa ei ole hankintakustannuksia tai käyttökatetta. Peruutuksia ei voi varmasti kohdistaa alkuperäisiin laskuihin, joten niitä raportoidaan erillisenä mittarina.
3. **Raportin on oltava toistettava.** Python-puhdistus, SQL-täsmäytys ja samaan ajoon liitetty automaattinen raportin muodostus vähentävät käsin laskettujen lukujen riskiä.
4. **Analytiikan hyöty syntyy tulkinnasta.** Maa- ja tuotekohtaiset poikkeamat ovat hyödyllisiä tarkistuskohteita, mutta kuvio ei vielä todista syy-seuraussuhdetta.

## Ehdotetut jatkotoimet

Rakenna Power BI -raportin ensimmäinen versio eriytetyillä myynti- ja peruutusmittareilla, dokumentoi tietojen omistaja ja päivityssykli, sekä varmista mittarit SQL-kyselyillä ennen johdon päätöksiä.

**Rajaus:** Tiedot kuvaavat historiallista brittiläistä verkkokauppaa, eivät HOK-Elantoa tai Suomen nykyisiä markkinoita. Tämä on Google Data Analytics -sertifikaatin jälkeen toteutettu itsenäinen portfolioharjoitus.
