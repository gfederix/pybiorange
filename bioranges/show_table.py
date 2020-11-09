def show_table(x=None):
    if x is None:
        return ""
    r1 = x[0]
    r1_name, r1_data = r1
    return "\n".join(row_presenter(r1_name, type(r1_data).__name__, r1_data))

def row_presenter(name, type, data):
    return [str(name), "<{}>".format(type)] + list(map(str, data))
