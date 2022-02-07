

if __name__ == "__main__":
   
    stars = 4
    abacus = 1
    incr = 1
    while abacus > 0:
        for i in range( 0, abacus):
            print("*", end="")
        print()
        abacus += incr
        if abacus > stars:   
            abacus = stars - 1
            incr = -1


        