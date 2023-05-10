from ctypes import c_double, c_float, c_int, c_int16, c_long, c_longdouble, c_longlong, c_short, c_uint16, c_ulong, c_ulonglong
from ctypes import c_uint8
from ctypes import c_uint8
from ctypes import c_int8 
from ctypes import c_uint
from ctypes import c_long
from typing import List,Tuple,TypeVar, TypeAlias, NewType
from typing import Optional
from typing import Sequence as sequence

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
    "no_labels",
    "args_rename",
    "args_alias",
    "no_protocol",
    "protocols",

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
NSNumber = NewType("NSNumber",object) 
URL = NewType("URL", str)
Error = NewType("Error", str)
UUID = NewType("UUID", str)
Array = NewType("Array", sequence)


def wrapper(py_init=True, debug_mode=False, target: str = None): ...

#def EventDispatcher(_: list[str]): ...

def callback(): ...

def callback_options(delegate: str | None = None): ...

def call_class(_: str): ...

def call_target(_: str): ...

def swift_func(): ...

def func_options(**kwargs): ...

def no_protocol(): ...

def args_rename(**names): ...
def args_alias(**names): ...

def no_labels(**labels):
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


def protocols(*protocols: str): ...

class NSObject: ...

class SwiftObject: ...

class SwiftBase: ...