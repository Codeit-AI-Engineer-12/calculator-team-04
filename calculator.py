from ops.add import add
from ops.average import average
from ops.divide import divide
from ops.integer_division import integer_division
from ops.min import min
from ops.multiply import multiply
from ops.root import root
from ops.subtract import subtract

operations = {
    "+": add,
    "-": subtract,
    "/": divide,
    "*": multiply,
    "//": integer_division,
    "**": root,
    "min": min,
    "avg": average,
}
