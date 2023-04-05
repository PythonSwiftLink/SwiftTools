from ctypes import c_double, c_float, c_int, c_int16, c_long, c_longdouble, c_longlong, c_short, c_uint16, c_ulong, c_ulonglong
from ctypes import c_uint8
from ctypes import c_uint8
from ctypes import c_int8 
from ctypes import c_uint
from ctypes import c_long
from typing import List,Tuple,TypeVar, TypeAlias, NewType
from typing import Optional


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
    "struct",
    "List",
    "Tuple",
    "callback",
    "call_class",
    "call_target",
    "swift_func",
    "EventDispatcher",
    "wrapper",
    "no_labels",

    "URL",
    "Error",
    "UUID",
    "Optional"
    ]

#from ctypes import c_int8 as
int32 = NewType("int32", int)
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
data = c_uint8
json = c_int8
jsondata = c_uint8
uint = c_uint
double = c_double
float32 = c_float
longdouble = c_longdouble
 
URL = NewType("URL", str)
Error = NewType("Error", str)
UUID = NewType("UUID", str)


def wrapper(py_init=True, debug_mode=False, target: str = None): ...

#def EventDispatcher(_: list[str]): ...

def callback(): ...

def call_class(_: str): ...

def call_target(_: str): ...

def swift_func(): ...



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