# * python built in exceptions

# built-in exceptions that are automatically raised when an error occurs
# during program execution

# these exceptions are organized into two groups:
# * base class exceptions
# these are high-level superclasses and are not meant to be raised directly.
# They are used to group related exceptions

# * concrete exceptions
# these are actual exceptions that are raised when something goes wrong

# A diagram of the exception hierarchy is below:
#
# BaseException
# ├── BaseExceptionGroup
# ├── GeneratorExit
# ├── KeyboardInterrupt
# ├── SystemExit
# └── Exception
# ├── ArithmeticError
# │    ├── FloatingPointError
# │    ├── OverflowError
# │    └── ZeroDivisionError
# ├── AssertionError
# ├── AttributeError
# ├── BufferError
# ├── EOFError
# ├── ExceptionGroup [BaseExceptionGroup]
# ├── ImportError
# │    └── ModuleNotFoundError
# ├── LookupError
# │    ├── IndexError
# │    └── KeyError
# ├── MemoryError
# ├── NameError
# │    └── UnboundLocalError
# ├── OSError
# │    ├── BlockingIOError
# │    ├── ChildProcessError
# │    ├── ConnectionError
# │    │    ├── BrokenPipeError
# │    │    ├── ConnectionAbortedError
# │    │    ├── ConnectionRefusedError
# │    │    └── ConnectionResetError
# │    ├── FileExistsError
# │    ├── FileNotFoundError
# │    ├── InterruptedError
# │    ├── IsADirectoryError
# │    ├── NotADirectoryError
# │    ├── PermissionError
# │    ├── ProcessLookupError
# │    └── TimeoutError
# ├── ReferenceError
# ├── RuntimeError
# │    ├── NotImplementedError
# │    └── RecursionError
# ├── StopAsyncIteration
# ├── StopIteration
# ├── SyntaxError
# │    └── IndentationError
# │         └── TabError
# ├── SystemError
# ├── TypeError
# ├── ValueError
# │    └── UnicodeError
# │         ├── UnicodeDecodeError
# │         ├── UnicodeEncodeError
# │         └── UnicodeTranslateError
# └── Warning
# ├── BytesWarning
# ├── DeprecationWarning
# ├── EncodingWarning
# ├── FutureWarning
# ├── ImportWarning
# ├── PendingDeprecationWarning
# ├── ResourceWarning
# ├── RuntimeWarning
# ├── SyntaxWarning
# ├── UnicodeWarning
# └── UserWarning
