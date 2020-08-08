import random


def random_key_generator(value):
    s_key = value + str(random.randint(0000, 9999))
    return s_key


def reference_id():
    r_key = f"nwbn-{str(random.randint(0000, 9999))}"
    return r_key
