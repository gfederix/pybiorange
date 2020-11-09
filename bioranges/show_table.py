from functools import partial

def show_table(x=None):
    if x is None:
        return ""
    r1 = x[0]
    r1_name, r1_data = r1
    r1_width = max(len(r1_name), 10)
    return "\n".join(row_presenter(r1_name, type(r1_data).__name__, r1_data, width=r1_width))


def cell_presenter(x, width):
    return "{{:>{}}}".format(width).format(x)


def type_cell_presenter(x, width):
    x = "<{}>".format(x)
    return cell_presenter(x, width)


def row_presenter(name, type, data, width):
    return ([
        cell_presenter(name, width),
        type_cell_presenter(type, width)] +
        list(map(partial(cell_presenter, width=width), data)))
