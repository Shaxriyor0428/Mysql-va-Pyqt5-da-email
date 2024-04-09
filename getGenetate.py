import random

def generation(cod):
    randNumbers = ['1','2','3','4','5','6','7','8','9']
    result = random.choices(randNumbers,k=cod)

    return "".join(result)

