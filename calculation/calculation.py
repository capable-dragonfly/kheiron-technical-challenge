from typing import List, Tuple, Iterator, Callable, NewType

OPERATORS = {
    '+': lambda x, y: x + y,
    '-': lambda x, y: x - y,
    '*': lambda x, y: x * y,
    '/': lambda x, y: x // y,
}


def resolve_calculation(calculation: str, notation: str = 'prefix') -> int:
    calculation_elements = calculation.split()
    resolve_method = get_resolve_method(notation)
    result = resolve_method(iter(calculation_elements))
    return result

class UnknownNotation(Exception):
    pass

def get_resolve_method(notation: str) -> Callable[[Iterator[str]], int]:
    if notation == 'prefix':
        return resolve_prefix_calculation
    if notation == 'infix':
        return resolve_infix_calculation
    raise UnknownNotation(notation)


def resolve_prefix_calculation(calculation_iter: Iterator[str]) -> int:
    next_element = next(calculation_iter)
    if next_element in OPERATORS:
        first_operand = resolve_prefix_calculation(calculation_iter)    
        second_operand = resolve_prefix_calculation(calculation_iter)
        return OPERATORS[next_element](first_operand, second_operand)
    return int(next_element)

def resolve_infix_calculation(calculation_iter: Iterator[str]) -> int:
    next_element = next(calculation_iter)
    if next_element == '(':
        first_operand = resolve_infix_calculation(calculation_iter)
        operator = next(calculation_iter)
        second_operand = resolve_infix_calculation(calculation_iter)
        closing_bracket = next(calculation_iter)
        return OPERATORS[operator](first_operand, second_operand)
    return int(next_element)
