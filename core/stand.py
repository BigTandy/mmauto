import random as rand, string




def tokenGen(leng=50):
    temp = []
    for i in range(leng):
        temp.append(rand.choice(string.ascii_letters + string.digits))
    return "".join(temp)