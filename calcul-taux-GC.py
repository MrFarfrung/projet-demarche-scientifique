def annalyse(document):
    file=open(document,"r")
    ligne=file.readlines()
    
    a, c, t, g, n=0,0,0,0,0

    for i in range (1,len(ligne)) :
        y=ligne[i].upper()
        z=y.replace("\n","")
        for e in z :
            if not e in "ATGCN":
                message="erreur dans la séquence"
                return message
            else:
                if e=="A":
                    a+=1
                elif e=="C":
                    c+=1
                elif e=="T":
                    t+=1
                elif e=="G":
                    g+=1
                elif e=="N":
                    n+=1

    nb_gc= g+c
    nb_total= a + c + t + g + n
    txgc=(nb_gc/nb_total)*100

    resultat=" taux GC ="+str(txgc)+"%, nombre Pb :"+str(nb_total)+", nombre GC :"+str(nb_gc)
    return resultat


doc=input("entrez le chemin d'accès du fichier, avec le point ")
print(annalyse(doc))
