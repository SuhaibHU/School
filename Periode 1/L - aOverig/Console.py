# score = int(input('Geef je score: '))
#
# if score > 15:
#     print('Gefeliciteerd')
#
# print('Met een score van 18 ben je geslaagd!')
#
# leeftijd = int(input('Geef je leeftijd: '))
# paspoort = input('Nederlands paspoort ja/nee: ')
#
# if leeftijd >= 18 and paspoort == 'ja':
#     print('Gefeliciteerd, je mag stemmen!')
#
# else:
#     print('Helaas, je mag niet stemmen.')

# dagen = ['maandag', 'dinsdag', 'woensdag']
# for word in dagen:
#     print(word[0:2])

# for i in range (0, 31 ,2):
#     print(i, end=' ')

# s = 'Guido van Rossum heeft programmeertaal Python bedacht.'
# klinker = ['a', 'e', 'i', 'o', 'u']
#
# for char in s:
#     if char in klinker:
#         print(char)

# def som(getal1, getal2, getal3):
#     res = getal1 + getal2 + getal3
#     return res



# def som(getallenLijst):
#     res = sum(getallenLijst)
#     return res
#
# print(som([4,3,8,9]))

# def rng(i):
#     res = max(i) - min(i)
#     return res
#
# print(rng([4,0,1,-2]))

# def name(name):
#     return ('Hello ' + name + ' to the world of Python.')
#
# print(name('Suhaib'))

# def lang_genoeg(lengte):
#     if lengte >= 120:
#         return 'Je bent lang genoeg voor de attractie!'
#     else:
#         return 'Sorry, je bent te klein.'
#
# print(lang_genoeg(130))

# def new_password(oldpassword, newpassword):
#     if oldpassword != newpassword and len(newpassword) > 5:
#         return 'Je wachtwoord is nu veranderd'
#     else:
#         return 'Je wachtwoord moet minimaal 6 tekens lang zijn.'
#
# print(new_password('boii', input('Voer een nieuw wachtwoord in: ')))

# import math
#
# def kwadraten_som(grondgetallen):
#     resultaat = 0
#     for number in grondgetallen:
#         if number >= 0:
#             resultaat = (number ** 2) + resultaat
#     return resultaat
#
# print(kwadraten_som([4,5,3,-81]))


# def wijzig(letterlijst):
#     letterlijst.clear()
#     letterlijst.extend(["d", "e", "f"])
#
#
# lijst = ['a', 'b', 'c']
# print(lijst)
# wijzig(lijst)
# print(lijst)

# def BMI(gewicht, hoogte):
#     index = (gewicht * 703) / hoogte ** 2
#     print(index)
#     if index > 25.0:
#         print("Overweight")
#     elif index < 18.5:
#         print("Underweight")
#     else:
#         print('Normal')
#
# print(BMI(190, 75))
#
def nested(n):
    for j in range(n):
        for i in range(n):
            print(i, end=' ')
        print()

nested(5)