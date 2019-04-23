A=25000000
B=42000000
growthA=0.03
growthB=0.02
counter=0
while B > A:
    A=A+(A*growthA)
    B=B+(B*growthB)
    counter+=1
    print("Number of years",counter)
