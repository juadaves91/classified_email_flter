from helper_sensitive_censor import HelperSensitiveCensor 


if __name__ == "__main__":
    
    # Note: Only the following categories are contemplated for this functionality.
    list_key_words = ["STREET",
                      "PLACE"
                      "NAME",
                      "LASTNAME",
                      "DISEASE",
                      "MEDICINE",
                      "NATIONALITIES",
                      "DATE_NUM",
                      "DATE_LONG",
                      "DATE_SHORT",
                      "TIME",
                      "POSTAL_CODE",
                      "DIGIT",
                      "IP",
                      "EMAIL",
                      "URL"]   

    text_1 = "De mogelijkheden zijn sinds 2014 groot geworden, zeker vergeleken met 2012, hè Kees? Het systeem maakt " \
             "verschillende bewerkingen mogelijk die hiervoor niet mogelijk waren. De datum is 24-01-2011 (of 24 jan 21 " \
             "of 24 januari 2011). Ik ben te bereiken op naam@hostingpartner.nl en woon in Arnhem. Mijn adres is " \
             "Maasstraat 231, 1234AB. Mijn naam is Thomas Janssen en ik heb zweetvoeten. Oh ja, ik gebruik hier " \
             "heparine ( https://host.com/dfgr/dfdew ) voor. Simòne. Ik heet Lexan."
             
    text_2 = 'Er was eens een meisje, heel mooi, maar ook erg lui. Als ze moest spinnen, dan had ze zo het land, dat ze, als er maar een klein oneffenheidje in het vlas was, meteen een heel brok mee uit trok en naast zich op de grond gooide. Maar ze had een dienstmeisje dat heel vlijtig was, die zocht al dat weggeworpen vlas bij elkaar, haalde het uit de knoop, spon het weer en liet er een mooi jurkje van weven voor zichzelf.' \
             'Nu had een jonge man het luie meisje gevraagd om met hem te trouwen en de bruiloft zou gehouden worden. Op de laatste avond danste het ijverige meisje in haar mooie jurkje vrolijk rond, en toen sprak de bruid:' \
             'Ach, wat danst dat meisje netjes in mijn afvalrestjes!"' \
             "De bruidegom hoorde dat; en hij vroeg aan de bruid, wat ze daarmee zeggen wilde. Toen vertelde ze 't hem, dat het meisje een jurk gemaakt had van alle vlasresten die zij had weggegooid. Toen de bruidegom dat hoorde, en begreep hoe lui ze was, liet hij haar staan, ging naar het andere meisje en koos haar tot vrouw."
             
    text_3 = "Bij de groenteboer " \
             "Groenteboer: Goedemiddag, kan ik u helpen? " \
             "Thomas: Ja, graag. Ik wil graag twee pond aardbeien. " \
             "Groenteboer: Dit zijn verse aardbeien, heerlijk in deze tijd van het jaar. Verder nog iets? " \
             "Thomas: Ja, heeft u ook lekkere appels? " \
             "Groenteboer: Zeker, deze zijn lekker en ook nog in de aanbieding. Zal ik deze doen? " \
             "Thomas: Ja, doe daar maar een kilo van. " \
             "Groenteboer: Verder nog iets? " \
             "Thomas: Euh, ja. Doe maar een pond kersen. " \
             "Groenteboer: Lekkere kersen uit de Betuwe. Anders nog iets? " \
             "Thomas: Nee, dat was het. Hoeveel is het?  " \
             "Groenteboer: Samen is het elf euro 80 cent  " \
             "Thomas: Kijk eens, twaalf euro. Laat de rest maar zitten. " \
             "Groenteboer: Bedankt. Tot ziens! " \
             "Thomas: Tot ziens!"
             
    text_4 = 'Sifan Hassan kan nog amper geloven dat ze Nederland maandag de eerste olympische atletiektitel sinds 1992 heeft bezorgd. De geboren Ethiopische pakte in Tokio overtuigend goud op de 5.000 meter, met dank aan kopjes koffie. ' \
             '"Ik kan het nog niet geloven", zei een trotse Hassan in een eerste reactie bij de NOS. "De laatste 200 meter trok ik de sprint van mijn leven en nu ben ik gewoon olympisch kampioen. Ik ben heel dankbaar." ' \
             'De 28-jarige Hassan schudde zich in de slotfase los van de Keniaanse Hellen Obiri en de Ethiopische Gudaf Tsegay. In de laatste bocht sloeg ze een onoverbrugbaar gat en uiteindelijk kwam ze bijna twee seconden eerder over de finish dan Obiri. ' \
             'De aanloop van Hassan naar de finale van de 5.000 meter was verre van ideaal. De regerend wereldkampioene op de 1.500 meter en de 10 kilometer kwam ten val in de series van de 1.500 meter, maar won haar race wel en plaatste zich simpel voor de halve finales. ' \
             'Toch had Hassan na die valpartij weinig vertrouwen in een goede afloop van de finale op de 5 kilometer. "Toen ik was gevallen op de 1.500 meter, dacht ik: laat die 5.000 meter maar zitten. Het was echt vreselijk. Ik kon ook niet echt geloven dat ik was gevallen", zei de topatlete. ' \
             '"Het leek alsof alle energie uit mijn benen was gezogen toen ik weer van de grond kwam na die valpartij. Ik was zo vermoeid. Zonder koffie had ik nooit olympisch kampioen kunnen worden. Ik had de cafeïne echt nodig. Het voelde alsof ik twintig koppen koffie had gedronken." ' \
             'Hassan, die met haar olympische titel in de voetsporen treedt van onder anderen Fanny Blankers-Koen en Ellen van Langen, gaat op de Olympische Spelen in Tokio ook nog voor goud op de 1.500 meter en de 10 kilometer. ' \
             'Bron: nu.nl'
             
    text_5 = 'Lang geleden ging een man op een zondagmorgen naar het bos om hout te hakken. Van het gehakte hout maakte hij een grote takkenbos, wierp die op zijn schouders en keerde huiswaarts. ' \
             'Onderweg ontmoette hij een kluizenaar, die met toverkracht was begaafd. Deze bleef voor de houthakker staan en sprak tot hem: "Wel man, hoe durf je om op zondag te werken! Weet je dan niet, dat er geschreven staat: zes dagen zul je werken, maar op de zevende dag zul je rusten?" ' \
             '"Och kom," zei de houthakker vloekend, "wat kan het mij schelen, of het zondag of maandag is! Als ik op zondag werken wil, dan doe ik het." En met een vloek in plaats van een groet wilde hij zich verwijderen. ' \
             'Maar de kluizenaar sprak: "Dan zal je voor straf en als waarschuwing voor anderen voor eeuwig met uw takkenbos op de rug in de maan zitten." ' \
             'Hij raakte hem even met zijn toverstaf aan en daar vloog de houthakker naar de maan. Op heldere avonden kunt je hem daar nog altijd met zijn takkenbos zien zitten.'
             
             
    text_5 = 'In de buurt van kasteel Magerhorst in Duiven spookt het als de klokken met Kerstmis twaalf slagen slaan. Dan is er kans, dat men het gekletter van zwaarden hoort, zonder iets te zien. Het zijn de geesten van de Ploen en van de Magerhorst, die dan steeds de strijd aanbinden; een tweegevecht van spoken. ' \
             'Aan kasteel de Ploen herinnert nu alleen maar de Ploenstraat, waaraan kasteel de Magerhorst staat, eens een machtige vesting. Vroeger woonden op beide kastelen vooraanstaande ridders uit Kleef. ' \
             'Het moet rond 1400 gebeurd zijn, dat beide kasteelheren ruzie met elkaar kregen en ze besloten elkaar de eerste kerstdag met het zwaard te lijf te gaan. Wat de pastoor van Duiven ook probeerde, hij kon het gevecht niet verhinderen. Toen het uur van het duel gekomen was en de kerstklokken de nachtmis aankondigden, maakten ' \
             'beide ridders zich klaar voor de strijd. Ze vochten totdat de heer van de Magerhorst dood neer viel. De heer van de Ploen had de strijd wel gewonnen, maar veel plezier heeft hij er niet van gehad. Hij kwam zwaar gewond terug op zijn kasteel, dat kort daarna op raadselachtige wijze in vlammen opging. De geest van de Magerhorst  ' \
             'had zich gewroken, wist men te vertellen.'

    text_6 = "abcdefghijklmnopqrstuwxyz"    
    
    list_test_cases = []
    list_test_cases.append(text_1)
    list_test_cases.append(text_2)
    list_test_cases.append(text_3)
    list_test_cases.append(text_4)
    list_test_cases.append(text_5)
    list_test_cases.append(text_6)
    
    count = 1
    
    print('')
    print('-'*150)
    for test_case in list_test_cases:            
        hsc_obj = HelperSensitiveCensor(list_key_words, test_case)                 
        print('Test case: {}'.format(str(count)))
        print('')
        print('Before:')
        print(test_case)        
        print('')
        print('After:')
        print(hsc_obj.filter())
        print('-'*150)
        count = count + 1
        
        
        
        
        
        