def fruits_legumes(types, saison):
    if types == "fruits":
        if saison == "hiver":
            print("orange, mandarine, kiwi")
        else:
            print ("poire, fraise, cassis")
    elif types == "legumes":
        if saison == "hiver":
            print("carrote, topinambour, endive")
        else:
            print("artichaut, aubergine, navet")

fruits_legumes("fruits", "hiver")
fruits_legumes("fruits", "ete")
fruits_legumes("legumes", "hiver")
fruits_legumes("legumes", "ete")