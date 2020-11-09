from functools import partial, reduce

def show_table(x=None):
    if x is None:
        return ""
    r1 = x[0]
    r1_name, r1_data = r1
    r1_type = type(r1_data).__name__
    r1_width = 5
    return "\n".join(row_presenter(r1_name, r1_type, r1_data, min_width=r1_width))


def cell_presenter(x, width):
    return "{{:>{}}}".format(width).format(x)


def type_cell_presenter(x, width):
    x = "<{}>".format(x)
    return cell_presenter(x, width)


def row_presenter(name, type, data, min_width):
    width = min_width
    name_header = cell_presenter(name, width)
    type_header = type_cell_presenter(type, width)
    data_list = list(map(partial(cell_presenter, width=width), data))
    return [name_header, type_header] + data_list


class RowPresenter:
    def __init__(self, name, type, data, min_width=5):
        self.name_header = self._ProcessName(name)
        self.type_header = self._ProcessType(type)
        self.data = self._ProcessData(data)
        self.width = self._DetectWidth(min_width)

    def __iter__(self):
        for x in [self.name_header, self.type_header]:
            yield self._AlignCell(x)
        for x in self.data:
            yield self._AlignCell(str(x))

    def _AlignCell(self, x):
        return "{{:>{}}}".format(self.width).format(x)

    def _DetectWidth(self, min_width):
        return max(
            min_width,
            len(self.name_header),
            len(self.type_header),
            reduce(lambda acc, x: max(acc, len(x)), self.data, 0))

    def _ProcessName(self, x):
        return str(x)

    def _ProcessType(self, x):
        return "<{}>".format(x)

    def _ProcessData(self, x):
        return list(map(str, x))
