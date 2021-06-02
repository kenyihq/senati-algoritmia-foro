def foro():
    print(" RUTA OPTIMA ")    
    print("      B       ")
    print("     /|\      ")
    print("    / | \     ")
    print("   /  |  \    ")
    print("  F --|-- J   ")
    print("   \  |  /    ")
    print("    \ | /     ")
    print("     \|/      ")
    print("      A       ")
    
    print("\nINGRESA LA DISTANCIA ENTRE: ")
    dist_FB = int(input("F y B: "))
    dist_FJ = int(input("F y J: "))
    dist_FA = int(input("F y A: "))
    dist_BA = int(input("B y A: "))
    dist_BJ = int(input("B y J: "))
    dist_AJ = int(input("A y J: "))

    run(dist_FB, dist_FJ, dist_FA, dist_BA, dist_BJ, dist_AJ)
    
def run(dist_FB, dist_FJ, dist_FA, dist_BA, dist_BJ, dist_AJ):
    suma = 0
    
    print("\nIndicar punto de partida:")
    partida = input("-> F / B / J / A: ")
    partida = partida.upper()
    
    if partida == "F":
        if dist_FB <= dist_FJ and dist_FB <= dist_FA and dist_BA <= dist_BJ:
            suma = dist_FB + dist_BA + dist_AJ + dist_FJ
            print("\nRuta a seguir: F -> B -> A -> J -> F")
    
        elif dist_FA <= dist_FJ and dist_FA <= dist_FB and dist_BA <= dist_AJ:
            suma = dist_FA + dist_BA + dist_BJ + dist_FJ
            print("\nRuta a seguir: F -> A -> B -> J -> F")
    
        elif dist_FJ <= dist_FB and dist_FJ <= dist_FA and dist_BJ <= dist_AJ:
            suma = dist_FJ + dist_BJ + dist_BA + dist_FA
            print("\nRuta a seguir: F -> J -> B -> A -> F")
    
        elif dist_FJ <= dist_FB and dist_FJ <= dist_FA and dist_AJ <= dist_BJ:
            suma = dist_FJ + dist_AJ + dist_BA + dist_FB
            print("\nRuta a seguir: F -> J -> A -> B -> F")
    
        elif dist_FB <= dist_FJ and dist_FB <= dist_FA and dist_BJ <= dist_BA:
            suma = dist_FB + dist_BJ + dist_AJ + dist_FA
            print("\nRuta a seguir: F -> B -> J -> A -> F")
    
        elif dist_FA <= dist_FJ and dist_FA <= dist_FB and dist_AJ <= dist_BA:
            suma = dist_FA + dist_AJ + dist_BJ + dist_FB
            print("\nRuta a seguir: F -> A -> J -> B -> F")
    
    elif partida == "B":
        if dist_FB <= dist_BA and dist_FB <= dist_BJ and dist_FJ <= dist_FA:
            suma = dist_FB + dist_FJ + dist_AJ + dist_BA
            print("\nRuta a seguir: B -> F -> J -> A -> B")
    
        elif dist_BJ <= dist_BA and dist_BJ <= dist_FB and dist_FJ <= dist_AJ:
            suma = dist_BJ + dist_FJ + dist_FA + dist_BA
            print("\nRuta a seguir: B -> J -> F -> A -> B")
    
        elif dist_BA <= dist_FB and dist_BA <= dist_BJ and dist_AJ <= dist_FA:
            suma = dist_BA + dist_AJ + dist_FJ + dist_FB
            print("\nRuta a seguir: B -> A -> J -> F -> B")
    
        elif dist_BA <= dist_FB and dist_BA <= dist_BJ and dist_FA <= dist_AJ:
            suma = dist_BA + dist_FA + dist_FJ + dist_BJ
            print("\nRuta a seguir: B -> A -> F -> J -> B")
    
        elif dist_BJ <= dist_BA and dist_BJ <= dist_FB and dist_AJ <= dist_FJ:
            suma = dist_BJ + dist_AJ + dist_FA + dist_FB
            print("\nRuta a seguir: B -> J -> A -> F -> B")
    
        elif dist_FB <= dist_BA and dist_FB <= dist_BJ and dist_FA <= dist_FJ:
            suma = dist_FB + dist_FA + dist_AJ + dist_BJ
            print("\nRuta a seguir: B -> F -> A -> J -> B")
    
    elif partida == "J":
        if dist_BJ <= dist_FJ and dist_BJ <= dist_AJ and dist_BA <= dist_FB:
            suma = dist_BJ + dist_BA + dist_FA + dist_FJ
            print("\nRuta a seguir: J -> B -> A -> F -> J")
    
        elif dist_AJ <= dist_FJ and dist_AJ <= dist_BJ and dist_BA <= dist_FA:
            suma = dist_AJ + dist_BA + dist_FB + dist_FJ
            print("\nRuta a seguir: J -> A -> B -> F -> J")
    
        elif dist_FJ <= dist_BJ and dist_FJ <= dist_AJ and dist_FB <= dist_FA:
            suma = dist_FJ + dist_FB + dist_BA + dist_AJ
            print("\nRuta a seguir: J -> F -> B -> A -> J")
    
        elif dist_FJ <= dist_BJ and dist_FJ <= dist_AJ and dist_FA <= dist_FB:
            suma = dist_FJ + dist_FA + dist_BA + dist_BJ
            print("\nRuta a seguir: J -> F -> A -> B -> J")
    
        elif dist_BJ <= dist_FJ and dist_BJ <= dist_AJ and dist_FB <= dist_BA:
            suma = dist_BJ + dist_FB + dist_FA + dist_AJ
            print("\nRuta a seguir: J -> B -> F -> A -> J")
    
        elif dist_AJ <= dist_FJ and dist_AJ <= dist_BJ and dist_FA <= dist_BA:
            suma = dist_AJ + dist_FA + dist_FB + dist_BJ
            print("\nRuta a seguir: J -> A -> F -> B -> J")
    
    elif partida == "A":
        if dist_FA <= dist_BA and dist_FA <= dist_AJ and dist_FJ <= dist_FB:
            suma = dist_FA + dist_FJ + dist_BJ + dist_BA
            print("\nRuta a seguir: A -> F -> J -> B -> A")
    
        elif dist_AJ <= dist_BA and dist_AJ <= dist_FA and dist_FJ <= dist_BJ:
            suma = dist_AJ + dist_FJ + dist_FB + dist_BA
            print("\nRuta a seguir: A -> J -> F -> B -> A")
    
        elif dist_BA <= dist_FA and dist_BA <= dist_AJ and dist_FB <= dist_BJ:
            suma = dist_BA + dist_FB + dist_FJ + dist_AJ
            print("\nRuta a seguir: A -> B -> F -> J -> A")
    
        elif dist_BA <= dist_FA and dist_BA <= dist_AJ and dist_BJ <= dist_FB:
            suma = dist_BA + dist_BJ + dist_FJ + dist_FA
            print("\nRuta a seguir: A -> B -> J -> F -> A")
    
        elif dist_FA <= dist_BA and dist_FA <= dist_AJ and dist_FB <= dist_FJ:
            suma = dist_FA + dist_FB + dist_BJ + dist_AJ
            print("\nRuta a seguir: A -> F -> B -> J -> A")
    
        elif dist_AJ <= dist_BA and dist_AJ <= dist_FA and dist_BJ <= dist_FJ:
            suma = dist_AJ + dist_BJ + dist_FB + dist_FA
            print("\nRuta a seguir: A -> J -> B -> F -> A")
    else:
        print("Ingrese una opción de partida válida")
        
        run(dist_FB, dist_FJ, dist_FA, dist_BA, dist_BJ, dist_AJ)
    
    print("Ruta optima:", suma, "km. ")

foro()