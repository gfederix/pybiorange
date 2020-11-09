def show_table(x=None):
    if x is None:
        return ""
    r1 = x[0]
    r1_name, r1_data = r1
    return r1_name + "\n<" + type(r1_data).__name__ + ">\n" + "\n".join(map(str, r1_data))
