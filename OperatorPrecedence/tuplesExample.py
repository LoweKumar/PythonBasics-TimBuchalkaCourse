# welcome = "Welcome to my Nightmare", "Alice Cooper", 1975
# bad = "Bad Company", "Bad Company", 1974
# budgie = "Nightflight", "Budgie", 1981
# imelda = "More Mayhem", "Emilda May", 2011
# metallica = "Ride the Lightning", "Metallica", 1984
# arijit = "Tum hi ho", "A2", 2010
#
# print(metallica)
# print(metallica[0])
# print(metallica[1])
# print(metallica[2])
#
# print(arijit)
#
# # converting tuple to list
# arijit2 = list(arijit)
# print(arijit2)
#
# a, b, c = arijit
# print(a, b, c)
#
# arijit2[1] = "Ash2"
# print(arijit2)
#
#
 # tuple in a list - albums
albums = [("Welcome to my Nightmare", "Alice Cooper", 1975),
          ("Bad Company", "Bad Company", 1974),
          ("Nightflight", "Budgie", 1981),
          ]

print(len(albums))

for a, b, c in albums:
    print(a, b, c)
