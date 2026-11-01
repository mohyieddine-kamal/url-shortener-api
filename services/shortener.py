import random
import string


def generate_short_code(length: int = 6) -> str:
    caracteres = string.ascii_letters + string.digits
    return "".join(random.choices(caracteres, k=length))