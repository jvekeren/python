def isPriem(getal):
    if getal > 1 :
        for i in range(2,getal):
            if (getal % i ) == 0:
                print(i,"keer",getal//i,"is",getal)
                return (False)
            else:
                return (True)
    else:
        
        return (False)

isPriem(28)
