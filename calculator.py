from ops.add import add
from ops.divide import divide
from ops.integer_division import integer_division
from ops.multiply import multiply
from ops.subtract import subtract

operations = {
    "+": add,
    "-": subtract,
    "/": divide,
    "*": multiply,
    "//": integer_division,
    "**": root
}
