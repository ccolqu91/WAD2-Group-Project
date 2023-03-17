import random
from .models import *

def get_voucher():
    alphabet = ["A","B","C","D","E","F","G","H","I","J","K","L","M","N","O","P","Q","R","Z","T","U","V","W","Y","Z"]

    randomInt = random.randint(1000000,9999999)
    listInt = list(map(int, str(randomInt)))
    lengthListInt = len(listInt)

    numOfLetters = random.randint(1,2)

    for x in range(numOfLetters):
        pos = random.randint(0,lengthListInt-1)
        letter = random.choice(alphabet)

        listInt[pos] = letter


    voucher = ''.join(map(str, listInt))
    if Survey.objects.filter(voucher_code = voucher).exists():
        voucher=get_voucher()
    return voucher