def drug_calculator():
    age=input('enter your age in years: ')
    if age >18:
        print('age should be below 18 years')
    else:
        weigh=input('enter your weight in kg: ')
        if weigh>100 or weigh<10:
            print('weight of children should be between 10 and 100 kg')
        else:
            dosage=15*weigh
            print(f'drug dosage is {dosage}mg')
            strength=input('enter your drug strength between 120mg/5mL and 250mg/5mL: ')
            if strength not in ['120mg/5mL','250mg/5mL']:
                print('strength should be 120mg/5mL or 250mg/5mL')
            else:
                if strength=='120mg/5mL':
                    volume=dosage*5/120
                    print(f'volume of solution required is {volume}mL')
                else:
                    volume=dosage*5/250
                    print(f'volume of solution required is {volume}mL')
drug_calculator()
#directly input age, weight, strength to use this code
#example:
#enter your age in years: 15
#enter your weight in kg: 60
#enter your drug strength between 120mg/5mL and 250mg/5mL: 120mg/5mL
#drug dosage is 900mg
#volume of solution required is 18.0mL