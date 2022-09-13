Vehicles = {
    'Bajaj': 'Pulsar 160',
    'Kawasaki': 'Ninja 650',
    'RoyalEnfield': 'Classic 600',
    'Tata':'Safari',
}

# adding extra values
Vehicles['Jawa'] = 'Jawa350'
Vehicles['TVS'] = 'Apache200'
# Removing the tata key and value associate with it
del Vehicles['Tata']
# alternate to remove an item
Vehicles.pop("Tata", None)
# changing the value of Bajaj
Vehicles['Bajaj'] = 'Pulsar 220'

# my_bike = Vehicles['RoyalEnfield']
# print(my_bike)
#
# bike = Vehicles.get('Bajaj')
# print(bike)

# for key in Vehicles:
#     print(key, Vehicles[key], sep='-')
# alternate way of printing
for key, value in Vehicles.items():
    print(key, value, sep='-')