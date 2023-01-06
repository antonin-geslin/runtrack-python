def phare(nb, cm):
    taille = cm * 0.01
    distance  = (nb * taille) * 2
    semaine = (distance * 5) * 7

    print("Pour", nb,"marches de ",cm,"cm, le gardien parcours",semaine,"m par semaine")




phare(50, 20)