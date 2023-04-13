def soil_texture(sand, silt, clay):
    if 86 <= sand <=100 and 0<= silt <= 14 and 0 <= clay <= 10:
        return 'Sand'
    elif 70 <= sand <= 86 and 0 <= silt <= 30 and 0 <= clay <= 15:
        return 'Loamy sand'
    elif 44 <= sand <= 85 and 0 <= silt <= 50 and 0 <= clay <= 20:
        return 'Sandy loam'
    elif 23 <= sand <= 52 and 28 <= silt <= 50 and 7 <= clay <= 27:
        return 'Loam'
    elif 20 <= sand <= 50 and 50 <= silt <= 88 and 0 <= clay <= 27:
        return 'Silty loam'
    elif 0 <= sand <= 20 and 80 <= silt <= 100 and 0 <= clay <= 15:
        return 'Silt'
    elif 20 <= sand <= 45 and 15 <= silt <= 40 and 27 <= clay <= 40:
        return 'Clay loam'
    elif 45 <= sand <= 80 and 0 <= silt <= 28 and 20 <= clay <= 35:
        return 'Sandy clay loam'
    elif 0 <= sand <= 20 and 40 <= silt <= 72 and 28 <= clay <= 40:
        return 'Silty clay loam'
    elif 45 <= sand <= 65 and 0 <= silt <= 20 and 35 <= clay <= 55:
        return 'Sandy clay'
    elif 0 <= sand <= 20 and 40 <= silt <= 60 and 40 <= clay <= 60:
        return 'Silty clay'
    elif 0 <= sand <= 45 and 0 <= silt <= 40 and 40 <= clay <= 100:
        return 'Clay'
    else:
        return 'Texture class could not be determined'
# get input percentages from user
sand = float(input('Enter the percentage of sand: '))
silt = float(input('Enter the percentage of silt: '))
clay = float(input('Enter the percentage of clay: '))
# determine soil texture class based on input percentages
texture_class = soil_texture(sand, silt, clay)
# print the determined soil texture class
print('The soil texture class is:', texture_class)
