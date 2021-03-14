from typing import List, Tuple, Callable, NewType

OPERATORS = {
    '+': lambda x, y: x + y,
    '-': lambda x, y: x - y,
    '*': lambda x, y: x * y,
    '/': lambda x, y: x // y,
}


def resolve_calculation(calculation: str, notation: str = 'prefix') -> int:
    calculation_elements = calculation.split()
    resolve_method = get_resolve_method(notation)
    result, _ = resolve_method(calculation_elements)
    return result

class UnknownNotation(Exception):
    pass

def get_resolve_method(notation: str) -> Callable[[List[str]], Tuple[int, List[str]]]:
    if notation == 'prefix':
        return resolve_prefix_calculation
    raise UnknownNotation(notation)


def resolve_prefix_calculation(calculation_elements: List[str]) -> Tuple[int, List[str]]:
    next_element, *rest = calculation_elements
    if next_element in OPERATORS:
        first_operand, rest = resolve_prefix_calculation(rest)    
        second_operand, rest = resolve_prefix_calculation(rest)
        return OPERATORS[next_element](first_operand, second_operand), rest
    return int(next_element), rest
