def naivesearch(t,p):
    n = len(t)
    m = len(p)
    for s in range(0, (n-m)+1):
        if p == t[s+1:s+m+1]:
            print("pattern found at indices "+str(s+1)+" to "+str(s+m))

naivesearch("000010001010001","0001")