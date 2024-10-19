

from typing import *
from numbers import Number
from  typing import Callable, TypeAlias
import typing
import _collections_abc
__all__ = [
    "long",
    "ulong",
    "longlong",
    "ulonglong",
    "uint8",
    "int16",
    "uint16",
    "int32",
    "uint32"
    "data",
    "json",
    "jsondata",
    "uint",
    "double",
    "float32",
    ## other types
    "TypeVar",
    "NewType",
    "struct",
    "List",
    "Tuple",
    "sequence",
    "Array",
    "data",
    "NSNumber",

    "func_options",

    "callback",
    "callback_options"
    "call_class",
    "call_target",
    "swift_func",
    "EventDispatcher",
    "wrapper",
    "wrapper_base",
    "no_labels",
    "args_rename",
    "args_alias",
    "no_protocol",
    "protocols",
    "Protocol"
    "URL",
    "Error",
    "UUID",
    "Optional",
    "SwiftClass",
    "NSObject",
    "SwiftObject",
    "SwiftBase"
    ]

#from ctypes import c_int8 as
int32 = NewType("int32", int)
uint32 = NewType("uint32", int)
#int32 = c_int
long = c_long
ulong = c_ulong
longlong = c_longlong
ulonglong = c_ulonglong
uint8 = c_uint8
short = c_int16
int16 = c_int16
ushort = c_uint16
uint16 = c_uint16
data = NewType("data", bytes)
json = c_int8
jsondata = c_uint8
uint = c_uint
double = c_double
float32 = c_float
longdouble = c_longdouble
=======

    "NSObject",
    "SwiftObject",
    "SwiftBase",
    "bases",
    
    
    "Hashable",
    "SupportsInt",
    "SupportsFloat",
    "SupportsIndex",
    "SupportsBytes",

    "Str",
    "Sequence",
    "MutableSequence",
    "Mapping",
    "MutableMapping",

    "AsyncIterable",
    "AsyncGenerator",
    "Awaitable",

    "Number",

    "Buffer",
    "Bytes",
    "WrappedProperty",
    
    "Callable",
    "CallableOnce",
    "T",
    "R",
    "LoggedVar"
]


class Buffer(BinaryIO):
    ...
    
class Bytes:
    """Conforms to bytes() with method __bytes__."""
    
    def __bytes__(self) -> bytes:
        pass
      
SupportsBytes
Float = SupportsFloat
Int = SupportsInt

class int8(int):
        """Swift IntegerLiteralType
        ```swift
        Int8
        ```
        A 8-bit unsigned integer value
        """
    

class uint8(int):
    """Swift IntegerLiteralType
    ```swift
    UInt8
    ```
    A 8-bit signed integer value
    """


class int16(int):
    """Swift IntegerLiteralType
    ```swift
    Int16
    ```
    A 16-bit unsigned integer value
    """


class uint16(int):
    """Swift IntegerLiteralType
    ```swift
    UInt16
    ```
    A 16-bit signed integer value
    """


class int32(int):
    """Swift IntegerLiteralType
    ```swift
    Int32
    ```
    A 32-bit unsigned integer value
    """


class uint32(int):
    """Swift IntegerLiteralType
    ```swift
    UInt32
    ```
    A 32-bit signed integer value
    """


class int64(int):
    """Swift IntegerLiteralType
    ```swift
    Int64
    ```
    A 64-bit unsigned integer value
    """


class uint64(int):
    """Swift IntegerLiteralType
    ```swift
    UInt64
    ```
    A 64-bit signed integer value
    """
    
class int(int):
    """Swift IntegerLiteralType
    ```swift
    Int64
    ```
    A 64-bit unsigned integer value
    """


class uint(int):
    """Swift IntegerLiteralType
    ```swift
    UInt64
    ```
    A 64-bit signed integer value
    """
    
    
class double(float):
    """Swift FloatLiteralType
    ```swift
    Double
    ```
    A 64-bit floating point type.
    """

class float32(float):
    """Swift FloatLiteralType
    ```swift
    Float32
    ```
    A 32-bit floating point type.
    """
    

float = double
long = int64
ulong = uint64
longlong = int64
ulonglong = uint64
short = int16
ushort = uint16
longdouble = c_longdouble


data = NewType("data", bytes)
json = str
jsondata = NewType("jsondata", bytes)

NSNumber = NewType("NSNumber",object) 
URL = NewType("URL", str)
Error = NewType("Error", str)
UUID = NewType("UUID", str)
Array = NewType("Array", sequence)

class String(str): ...


def wrapper_base(): ...

def wrapper(py_init=True, new=False,  debug_mode=False, target: str = None) -> Callable:
    """
    ```python
    
    @wrapper()
    class MySwiftClass:
        
        # float getter only
        x = property(float, setter=False)
        # float getter only
        y = property(float, setter=False)
        # float getter/setter
        z = property(float)
        
        def send_string(self, message: str): ...
        
        def join_strings(self, strings: list[str]) -> str: ...
        
    ```

    Args:
        py_init (bool, optional): _description_. Defaults to True.
        debug_mode (bool, optional): _description_. Defaults to False.
        target (str, optional): _description_. Defaults to None.
    """
AnyClass = Generic[object]
#def EventDispatcher(_: list[str]): ...

def throws(_) -> Self: ...

def bases(*args) -> Callable:
    """_summary_
    ```python
    @bases(Sequence, Hashable, Mapping)
    ```
    now the Wrapper conforms to Sequence Hashable and Mapping.
    of course now you got a lot of functions to fill out in swift :-)
    
    Args:
        types (list[AnyClass]): _description_
    """

def callback(): ...

def callback_options(delegate: str | None = None): ...

def call_class(_: str) -> Callable: ...

def call_target(_: str) -> Callable: ...

def swift_func(): ...



def args_rename(**names) -> Callable: ...
def args_alias(**names) -> Callable: ...

def no_labels(**labels) -> Callable:
    """
    ```python
    #python
    @no_labels
    def my_func(self, arg: str, arg2: str, arg3: str): ...
    ```

    in swift:
    ```swift
    // without
    func my_func(arg: String, arg2: String, arg3: String)
    ```
    ................................
    
    after:
    ```swift
    // with
    func my_func(_ arg: String, _ arg2: String, _ arg3: String)
    ```

    #####################################
    ```python
    #python
    @no_labels(arg2=True)
    def my_func(self, arg: str, arg2: str, arg3: str): ...
    ```

    in swift:
    ```swift
    // without
    func my_func(arg: String, arg2: String, arg3: String)
    ```
    ................................
    
    after:
    ```swift
    // with
    func my_func(arg: String, _ arg2: String, arg3: String)
    ```

    """

T = NewType("Type", type)

class SwiftClass(object):

    def __getattribute__(self, __name: str) -> type: ...


    def __len__(self) -> int: ...
    def __iter__(self) -> T: ...
    __hash__: ClassVar[None]  # type: ignore[assignment]
    @overload
    def __getitem__(self, __i: SupportsIndex) -> T: ...
    @overload
    def __getitem__(self, __s: slice) -> list[_T]: ...
    @overload
    def __setitem__(self, __key: SupportsIndex, __value: _T) -> None: ...
    @overload
    def __setitem__(self, __key: slice, __value: Iterable[_T]) -> None: ...
    def __delitem__(self, __key: SupportsIndex | slice) -> None: ...

    def __repr__(self) -> str: ...


def protocols(*protocols: str) -> Callable: ...

T = TypeVar("T", tuple, list, None)
R = TypeVar("R", object, None)
class _CallableType(Generic(T,R),_root=True):
    # def copy_with(self, params):
    #     return _CallableGenericAlias(self.__origin__, params,
    #                                  name=self._name, inst=self._inst,
    #                                  _paramspec_tvars=True)
    def __getitem__(self, params: T, returns: R): ...
    def __agetitem__(self, params):
        if not isinstance(params, tuple) or len(params) != 2:
            raise TypeError("Callable must be used as "
                            "Callable[[arg, ...], result].")
        args, result = params
        # This relaxes what args can be on purpose to allow things like
        # PEP 612 ParamSpec.  Responsibility for whether a user is using
        # Callable[...] properly is deferred to static type checkers.
        if isinstance(args, list):
            params = (tuple(args), result)
        else:
            params = (args, result)
        return self.__getitem_inner__(params)

    # @_tp_cache
    # def __getitem_inner__(self, params):
    #     args, result = params
    #     msg = "Callable[args, result]: result must be a type."
    #     result = _type_check(result, msg)
    #     if args is Ellipsis:
    #         return self.copy_with((_TypingEllipsis, result))
    #     if not isinstance(args, tuple):
    #         args = (args,)
    #     args = tuple(_type_convert(arg) for arg in args)
    #     params = args + (result,)
    #     return self.copy_with(params)
class LoggedVar(Generic[T]):
    def __init__(self, value: T, name: str, logger: Logger) -> None:
        self.name = name
        self.logger = logger
        self.value = value

    def set(self, new: T) -> None:
        self.log('Set ' + repr(self.value))
        self.value = new

    def get(self) -> T:
        self.log('Get ' + repr(self.value))
        return self.value
    
def abc(a: LoggedVar[str]): ...

class __Callable(_CallableType):...

CallableOnce = _collections_abc.Callable
"""
Will keep a strong reference to a callable object, and deref it after being called by swift.
this annotation should only be used for callbacks that will executed only once..

Example: 
    ``CallableOnce[[int, str], float]`` == ``(int, str) -> float``
"""
#class CallableOnce(_collections_abc.Callable): ...
    
    # def __init__(self, args: T, returns: R): ...
    # def __getitem__(self, args: T, returns: R) -> typing.Callable[T,R]: ...
    
    # def set(self, new: T) -> None:
    #     self.log('Set ' + repr(self.value))
    #     self.value = new

    # def get(self) -> T:
    #     self.log('Get ' + repr(self.value))
    #     return self.value


class WrappedProperty:
    
    def __init__(self, type: object, readonly: bool = False, alias: str | None = None) -> None: ...

class NSObject: ...

class SwiftObject: ...

class SwiftBase: ...
