# Liiketoiminta-analyysi: myynti, peruutukset ja datan laatu

**Aineisto:** UCI Online Retail, Iso-Britannia 2010–2011 (Daqing Chen, 2015), CC BY 4.0.

**Toteutustila:** analyysiputki on toteutettu ja testattu synteettisellä aineistolla. Todellisesta UCI-aineistosta ei esitetä vielä varmistettuja tuloksia.

## Liiketoimintaongelma

Miten johto voi seurata tilausmyynnin kehitystä, tunnistaa tärkeimmät tuotteet ja markkinat sekä varmistaa, ettei huonolaatuinen data johda virheellisiin päätelmiin?

## Käytetyt menetelmät

Excel- ja CSV-aineistojen luku, tietotyyppien tarkistus, duplikaattien käsittely, puuttuvien tunnisteiden raportointi, myynti- ja peruutusrivien erottelu, aikajakso- ja maakohtainen ryhmittely, Power BI -mittarimalli sekä pandas-lukujen riippumaton SQL-vertailu. Kaikki raportit ja kuviot tuotetaan samalla ajolla.

## Johtopäätökset ja suositukset

1. **Luotettavuus ennen raportointinopeutta.** Virheelliset päivämäärät, duplikaatit ja puuttuvat asiakastunnisteet on tuotava näkyviin ennen tulosten tulkintaa.
2. **Erota myynti, peruutukset ja kannattavuus.** Laskujen peruutukset eivät automaattisesti vastaa samaa kuin toteutuneet hyvitykset; hankintakustannusten puuttuessa katetta ei voi laskea.
3. **Tee päätökset yhdessä liiketoiminnan kanssa.** Kun lähdedata on validoitu, voidaan tutkia tuotekohtaisia ja maakohtaisia poikkeamia ja tarkistaa niiden vaikutus toimintaan.
4. **Rakenna jatkuva laadunvalvonta.** Sovitaan dataomistaja, mittarien määritelmät, päivityssykli ja selkeä virheiden käsittely.

## Seuraava tarkistuspiste

Aja analyysi alkuperäisellä 541 909 tapahtumarivin UCI-aineistolla, dokumentoi lähteen versio ja päivitä tämä yhteenveto oikeilla havainnoilla. Tämän jälkeen voidaan toteuttaa Power BI -raportti, jonka mittarit täsmäytetään SQL-tuloksiin.

**Huom.:** Tämä on Google Data Analytics -opintojen jälkeen itsenäisesti rakennettu portfolioesimerkki, ei työnantajan luottamuksellisia tietoja.
