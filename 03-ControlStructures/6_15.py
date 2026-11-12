###
# Checks if the EAN-13 article number is correct
# and whether the product was manufactured in Poland
#
ean = input("Enter EAN-13 article number: ")

if len(ean) == 13 and ean.isdigit():
    print("Article number is correct")

    if ean[:3] == "590":
        print("Article manufactured in Poland")