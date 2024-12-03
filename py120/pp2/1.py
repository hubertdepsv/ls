while True:
    doucerie = input("How douce are you? ")

    if doucerie.lower() == "la plus":
        print("Alors je te kiss")
        break
    elif doucerie.lower() == "very" or doucerie.lower() == "very douce":
        print("C'est un élément de réponse")
    else:
        print("Est-ce vrai ?")