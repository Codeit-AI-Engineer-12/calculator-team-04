from ops.absolute import absolute
from ops.add import add
from ops.average import average
from ops.divide import divide
from ops.integer_division import integer_division
from ops.multiply import multiply
from ops.root import root
from ops.subtract import subtract
from ops.modulo import modulo   

operations = {
    "+": add,
    "-": subtract,
    "/": divide,
    "*": multiply,
    "//": integer_division,
    "**": root,
    "%": modulo 
    "avg": average,
    "abs": absolute,
}
