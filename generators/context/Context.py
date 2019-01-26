assigned = {}


def add_variable(k: str, v: str):
    assigned[k.strip()] = v.strip()


def get_variable(k: str):
    return assigned[k.strip()]
