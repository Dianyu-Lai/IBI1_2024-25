def drug_calculator(weigh, strength):

    #check if weight is in the range
    if weigh > 100 or weigh < 10:
        print('weight of children should be between 10 and 100 kg')
    else:
        dosage=15 * weigh
        #check if the strength is in the range
        if strength not in ['120mg/5mL','250mg/5mL']:
            print('strength should be 120mg/5mL or 250mg/5mL')
        else:
            if strength == '120mg/5mL':
                volume=dosage*5/120

            else:
                volume=dosage*5/250
            
            return volume
        
weigh = int(input('enter your weight in kg: '))
strength = input('enter your drug strength between 120mg/5mL and 250mg/5mL: ') #please notice that mg/mL the "L" is capitalized
volume = drug_calculator(weigh,strength)
print(f"the volume of solution required is {volume}mL")
#example:
#enter your weight in kg: 60
#enter your drug strength between 120mg/5mL and 250mg/5mL: 120mg/5mL (please notice that mg/mL the "L" is capitalized)
#drug dosage is 900mg
#volume of solution required is 37.5mL