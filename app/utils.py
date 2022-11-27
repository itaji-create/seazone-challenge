import string
import random


def gerar_hash(size=30, chars=string.ascii_letters + string.digits):
    return ''.join(random.choice(chars) for _ in range(size))
