from typing import Any, Callable, Iterator, List, Set, Dict, Tuple, Union, Optional, Iterable
from functools import wraps
import inspect

def wrap_builtin(func: Callable) -> Callable:
    """
    빌트인 함수를 래핑하여 시그니처를 보존하는 새로운 함수를 생성합니다.
    """
    @wraps(func)
    def wrapper(*args, **kwargs):
        return func(*args, **kwargs)
    return wrapper

@wrap_builtin
def w_abs(x: Union[int, float, complex]) -> Union[int, float]:
    """Return the absolute value of a number."""
    return abs(x)

@wrap_builtin
def w_all(iterable: Iterable[Any]) -> bool:
    """Return True if all elements of the iterable are true."""
    return all(iterable)

@wrap_builtin
def w_any(iterable: Iterable[Any]) -> bool:
    """Return True if any element of the iterable is true."""
    return any(iterable)

@wrap_builtin
def w_ascii(obj: Any) -> str:
    """Return a string containing a printable representation of an object."""
    return ascii(obj)

@wrap_builtin
def w_bin(number: int) -> str:
    """Convert an integer number to a binary string."""
    return bin(number)

@wrap_builtin
def w_bool(x: Any = False) -> bool:
    """Return a Boolean value."""
    return bool(x)

@wrap_builtin
def w_chr(i: int) -> str:
    """Return a Unicode string of one character."""
    return chr(i)

@wrap_builtin
def w_dict(*args, **kwargs) -> Dict:
    """Create a new dictionary."""
    return dict(*args, **kwargs)

@wrap_builtin
def w_dir(obj: Any = None) -> List[str]:
    """Return the list of valid attributes for an object."""
    return dir(obj)

@wrap_builtin
def w_divmod(a: Union[int, float], b: Union[int, float]) -> Tuple[Union[int, float], Union[int, float]]:
    """Return quotient and remainder of division."""
    return divmod(a, b)

@wrap_builtin
def w_enumerate(iterable: Iterable[Any], start: int = 0) -> Iterator[Tuple[int, Any]]:
    """Return an enumerate object."""
    return enumerate(iterable, start)

@wrap_builtin
def w_eval(expression: str, globals: Optional[Dict] = None, locals: Optional[Dict] = None) -> Any:
    """Evaluate a Python expression."""
    return eval(expression, globals, locals)

@wrap_builtin
def w_filter(function: Optional[Callable], iterable: Iterable[Any]) -> Iterator[Any]:
    """Construct an iterator from elements which function returns True."""
    return filter(function, iterable)

@wrap_builtin
def w_float(x: Union[str, int, float] = 0.0) -> float:
    """Convert a string or number to a floating point number."""
    return float(x)

@wrap_builtin
def w_format(value: Any, format_spec: str = '') -> str:
    """Convert a value to a formatted representation."""
    return format(value, format_spec)

@wrap_builtin
def w_frozenset(iterable: Optional[Iterable[Any]] = None) -> frozenset:
    """Return an immutable set."""
    return frozenset(iterable)

@wrap_builtin
def w_getattr(obj: Any, name: str, default: Any = None) -> Any:
    """Get a named attribute from an object."""
    return getattr(obj, name, default)

@wrap_builtin
def w_globals() -> Dict[str, Any]:
    """Return the current global symbol table."""
    return globals()

@wrap_builtin
def w_hasattr(obj: Any, name: str) -> bool:
    """Return whether the object has an attribute with the given name."""
    return hasattr(obj, name)

@wrap_builtin
def w_hash(obj: Any) -> int:
    """Return the hash value of an object."""
    return hash(obj)

@wrap_builtin
def w_hex(number: int) -> str:
    """Convert an integer to a hexadecimal string."""
    return hex(number)

@wrap_builtin
def w_id(obj: Any) -> int:
    """Return the identity of an object."""
    return id(obj)

@wrap_builtin
def w_input(prompt: str = "") -> str:
    """Read a string from standard input."""
    return input(prompt)

@wrap_builtin
def w_int(x: Union[str, float] = 0, base: int = 10) -> int:
    """Convert a string or number to an integer."""
    return int(x, base)

@wrap_builtin
def w_isinstance(obj: Any, class_or_tuple: Union[type, Tuple[type, ...]]) -> bool:
    """Return whether an object is an instance of a class."""
    return isinstance(obj, class_or_tuple)

@wrap_builtin
def w_issubclass(cls: type, class_or_tuple: Union[type, Tuple[type, ...]]) -> bool:
    """Return whether a class is a subclass of another class."""
    return issubclass(cls, class_or_tuple)

@wrap_builtin
def w_iter(obj: Iterable[Any]) -> Iterator[Any]:
    """Return an iterator object."""
    return iter(obj)

@wrap_builtin
def w_len(obj: Iterable[Any]) -> int:
    """Return the number of items in a container."""
    return len(obj)

@wrap_builtin
def w_list(iterable: Optional[Iterable[Any]] = None) -> List[Any]:
    """Return a list from an iterable."""
    return list(iterable if iterable is not None else [])

@wrap_builtin
def w_map(function: Callable, iterable: Iterable[Any], *iterables: Iterable[Any]) -> Iterator[Any]:
    """Return an iterator that applies function to every item."""
    return map(function, iterable, *iterables)

@wrap_builtin
def w_max(*args: Any, key: Optional[Callable] = None, default: Any = None) -> Any:
    """Return the largest item in an iterable."""
    if default is not None:
        return max(*args, key=key, default=default)
    return max(*args, key=key)

@wrap_builtin
def w_min(*args: Any, key: Optional[Callable] = None, default: Any = None) -> Any:
    """Return the smallest item in an iterable."""
    if default is not None:
        return min(*args, key=key, default=default)
    return min(*args, key=key)

@wrap_builtin
def w_next(iterator: Iterator[Any], default: Any = None) -> Any:
    """Return the next item from the iterator."""
    return next(iterator, default)

@wrap_builtin
def w_oct(number: int) -> str:
    """Convert an integer to an octal string."""
    return oct(number)

@wrap_builtin
def w_ord(c: str) -> int:
    """Return the Unicode code point of a character."""
    return ord(c)

@wrap_builtin
def w_pow(base: Union[int, float], exp: Union[int, float], mod: Optional[Union[int, float]] = None) -> Union[int, float]:
    """Return base to the power exp."""
    if mod is not None:
        return pow(base, exp, mod)
    return pow(base, exp)

@wrap_builtin
def w_print(*args: Any, sep: str = ' ', end: str = '\n', file: Any = None, flush: bool = False) -> None:
    """Print objects to a stream."""
    print(*args, sep=sep, end=end, file=file, flush=flush)

@wrap_builtin
def w_range(stop: int, start: Optional[int] = None, step: int = 1) -> range:
    """Return a sequence of numbers."""
    if start is None:
        return range(stop)
    return range(start, stop, step)

@wrap_builtin
def w_repr(obj: Any) -> str:
    """Return a string containing a printable representation of an object."""
    return repr(obj)

@wrap_builtin
def w_reversed(seq: Iterable[Any]) -> Iterator[Any]:
    """Return a reverse iterator."""
    return reversed(seq)

@wrap_builtin
def w_round(number: float, ndigits: Optional[int] = None) -> Union[int, float]:
    """Round a number to a given precision."""
    if ndigits is not None:
        return round(number, ndigits)
    return round(number)

@wrap_builtin
def w_set(iterable: Optional[Iterable[Any]] = None) -> Set[Any]:
    """Return a new set object."""
    return set(iterable if iterable is not None else [])

@wrap_builtin
def w_slice(*args: int) -> slice:
    """Create a slice object."""
    return slice(*args)

@wrap_builtin
def w_sorted(iterable: Iterable[Any], *, key: Optional[Callable] = None, reverse: bool = False) -> List[Any]:
    """Return a new sorted list from an iterable."""
    return sorted(iterable, key=key, reverse=reverse)

@wrap_builtin
def w_str(obj: Any = "") -> str:
    """Return a string version of an object."""
    return str(obj)

@wrap_builtin
def w_sum(iterable: Iterable[Any], start: Any = 0) -> Any:
    """Return the sum of a sequence of numbers."""
    return sum(iterable, start)

@wrap_builtin
def w_tuple(iterable: Optional[Iterable[Any]] = None) -> Tuple[Any, ...]:
    """Return a tuple containing the elements of an iterable."""
    return tuple(iterable if iterable is not None else ())

@wrap_builtin
def w_type(obj: Any) -> type:
    """Return the type of an object."""
    return type(obj)

@wrap_builtin
def w_vars(obj: Optional[Any] = None) -> Dict[str, Any]:
    """Return the __dict__ attribute of an object."""
    return vars(obj) if obj is not None else locals()

@wrap_builtin
def w_zip(*iterables: Iterable[Any]) -> Iterator[Tuple[Any, ...]]:
    """Aggregate elements from iterables."""
    return zip(*iterables)

# 래핑된 함수들의 리스트 정의
wrapped_builtins = [
    w_abs, w_all, w_any, w_ascii, w_bin, w_bool, w_chr, w_dict,
    w_dir, w_divmod, w_enumerate, w_eval, w_filter, w_float,
    w_format, w_frozenset, w_getattr, w_globals, w_hasattr,
    w_hash, w_hex, w_id, w_input, w_int, w_isinstance, w_issubclass,
    w_iter, w_len, w_list, w_map, w_max, w_min, w_next, w_oct,
    w_ord, w_pow, w_print, w_range, w_repr, w_reversed, w_round,
    w_set, w_slice, w_sorted, w_str, w_sum, w_tuple, w_type,
    w_vars, w_zip
]

# 원본 agent 코드 수정
if __name__ == "__main__":
    from agent_framework import ChatAgent
    from agent_framework.openai import OpenAIChatClient
    import os
    from dotenv import load_dotenv

    load_dotenv()

    agent = ChatAgent(
        chat_client=OpenAIChatClient(
            model_id=os.environ['OPENAI_MODEL_NAME'],
            api_key=os.environ['OPENAI_API_KEY'],
            base_url=os.environ['OPENAI_ENDPOINT']
        ),
        instructions="You are a python itself, you can only use python built-in functions to answer user questions.",
        tools=wrapped_builtins,
    )

    while True:
        user_input = input("User: ")
        if user_input.lower() in ["exit", "quit"]:
            break
        response = agent.chat(user_input)
        print("Agent:", response)
        print()
