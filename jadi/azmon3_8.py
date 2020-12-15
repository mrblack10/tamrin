def morq_sag (heads,legs):
    leg = heads*2
    morq  = heads
    sag = 0
    while(leg < legs):
        leg  = leg + 2
        morq = morq - 1
        sag = sag + 1
    if leg == legs :
        list = [morq,sag]
        return list
    else:
        return None
    
head = int (input("heads:"))
leg = int (input("legs:"))


print (morq_sag(head,leg))
