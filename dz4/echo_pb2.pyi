from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Iterable as _Iterable, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class Vect2(_message.Message):
    __slots__ = ["val_x", "val_y"]
    VAL_X_FIELD_NUMBER: _ClassVar[int]
    VAL_Y_FIELD_NUMBER: _ClassVar[int]
    val_x: float
    val_y: float
    def __init__(self, val_x: _Optional[float] = ..., val_y: _Optional[float] = ...) -> None: ...

class RotaryFieldResponce(_message.Message):
    __slots__ = ["point", "field", "direction"]
    POINT_FIELD_NUMBER: _ClassVar[int]
    FIELD_FIELD_NUMBER: _ClassVar[int]
    DIRECTION_FIELD_NUMBER: _ClassVar[int]
    point: Vect2
    field: Vect2
    direction: str
    def __init__(self, point: _Optional[_Union[Vect2, _Mapping]] = ..., field: _Optional[_Union[Vect2, _Mapping]] = ..., direction: _Optional[str] = ...) -> None: ...

class RotaryFieldRequest(_message.Message):
    __slots__ = ["point", "direction", "vector"]
    class VectorEntry(_message.Message):
        __slots__ = ["key", "value"]
        KEY_FIELD_NUMBER: _ClassVar[int]
        VALUE_FIELD_NUMBER: _ClassVar[int]
        key: str
        value: Vect2
        def __init__(self, key: _Optional[str] = ..., value: _Optional[_Union[Vect2, _Mapping]] = ...) -> None: ...
    POINT_FIELD_NUMBER: _ClassVar[int]
    DIRECTION_FIELD_NUMBER: _ClassVar[int]
    VECTOR_FIELD_NUMBER: _ClassVar[int]
    point: Vect2
    direction: str
    vector: _containers.MessageMap[str, Vect2]
    def __init__(self, point: _Optional[_Union[Vect2, _Mapping]] = ..., direction: _Optional[str] = ..., vector: _Optional[_Mapping[str, Vect2]] = ...) -> None: ...

class Sequence(_message.Message):
    __slots__ = ["numbers"]
    NUMBERS_FIELD_NUMBER: _ClassVar[int]
    numbers: _containers.RepeatedScalarFieldContainer[int]
    def __init__(self, numbers: _Optional[_Iterable[int]] = ...) -> None: ...
