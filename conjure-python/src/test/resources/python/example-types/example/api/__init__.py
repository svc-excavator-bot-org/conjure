# this is package example.api
from conjure import *
from typing import Dict
from typing import List
from typing import Optional
from typing import Set
from typing import Tuple

class StringExample(ConjureBeanType):

    @classmethod
    def _fields(cls):
        # type: () -> Dict[str, ConjureFieldDefinition]
        return {
            'string': ConjureFieldDefinition('string', str)
        }

    _string = None # type: str

    def __init__(self, string):
        # type: (str) -> None
        self._string = string

    @property
    def string(self):
        # type: () -> str
        return self._string

class IntegerExample(ConjureBeanType):

    @classmethod
    def _fields(cls):
        # type: () -> Dict[str, ConjureFieldDefinition]
        return {
            'integer': ConjureFieldDefinition('integer', int)
        }

    _integer = None # type: int

    def __init__(self, integer):
        # type: (int) -> None
        self._integer = integer

    @property
    def integer(self):
        # type: () -> int
        return self._integer

class SafeLongExample(ConjureBeanType):

    @classmethod
    def _fields(cls):
        # type: () -> Dict[str, ConjureFieldDefinition]
        return {
            'safe_long_value': ConjureFieldDefinition('safeLongValue', int)
        }

    _safe_long_value = None # type: int

    def __init__(self, safe_long_value):
        # type: (int) -> None
        self._safe_long_value = safe_long_value

    @property
    def safe_long_value(self):
        # type: () -> int
        return self._safe_long_value

class RidExample(ConjureBeanType):

    @classmethod
    def _fields(cls):
        # type: () -> Dict[str, ConjureFieldDefinition]
        return {
            'rid_value': ConjureFieldDefinition('ridValue', str)
        }

    _rid_value = None # type: str

    def __init__(self, rid_value):
        # type: (str) -> None
        self._rid_value = rid_value

    @property
    def rid_value(self):
        # type: () -> str
        return self._rid_value

class BearerTokenExample(ConjureBeanType):

    @classmethod
    def _fields(cls):
        # type: () -> Dict[str, ConjureFieldDefinition]
        return {
            'bearer_token_value': ConjureFieldDefinition('bearerTokenValue', str)
        }

    _bearer_token_value = None # type: str

    def __init__(self, bearer_token_value):
        # type: (str) -> None
        self._bearer_token_value = bearer_token_value

    @property
    def bearer_token_value(self):
        # type: () -> str
        return self._bearer_token_value

class DoubleExample(ConjureBeanType):

    @classmethod
    def _fields(cls):
        # type: () -> Dict[str, ConjureFieldDefinition]
        return {
            'double_value': ConjureFieldDefinition('doubleValue', float)
        }

    _double_value = None # type: float

    def __init__(self, double_value):
        # type: (float) -> None
        self._double_value = double_value

    @property
    def double_value(self):
        # type: () -> float
        return self._double_value

class BinaryExample(ConjureBeanType):

    @classmethod
    def _fields(cls):
        # type: () -> Dict[str, ConjureFieldDefinition]
        return {
            'binary': ConjureFieldDefinition('binary', BinaryType())
        }

    _binary = None # type: Any

    def __init__(self, binary):
        # type: (Any) -> None
        self._binary = binary

    @property
    def binary(self):
        # type: () -> Any
        return self._binary

class OptionalExample(ConjureBeanType):

    @classmethod
    def _fields(cls):
        # type: () -> Dict[str, ConjureFieldDefinition]
        return {
            'item': ConjureFieldDefinition('item', OptionalType(str))
        }

    _item = None # type: Optional[str]

    def __init__(self, item):
        # type: (Optional[str]) -> None
        self._item = item

    @property
    def item(self):
        # type: () -> Optional[str]
        return self._item

class ListExample(ConjureBeanType):

    @classmethod
    def _fields(cls):
        # type: () -> Dict[str, ConjureFieldDefinition]
        return {
            'items': ConjureFieldDefinition('items', ListType(str))
        }

    _items = None # type: List[str]

    def __init__(self, items):
        # type: (List[str]) -> None
        self._items = items

    @property
    def items(self):
        # type: () -> List[str]
        return self._items

class SetExample(ConjureBeanType):

    @classmethod
    def _fields(cls):
        # type: () -> Dict[str, ConjureFieldDefinition]
        return {
            'items': ConjureFieldDefinition('items', ListType(str))
        }

    _items = None # type: List[str]

    def __init__(self, items):
        # type: (List[str]) -> None
        self._items = items

    @property
    def items(self):
        # type: () -> List[str]
        return self._items

class MapExample(ConjureBeanType):

    @classmethod
    def _fields(cls):
        # type: () -> Dict[str, ConjureFieldDefinition]
        return {
            'items': ConjureFieldDefinition('items', DictType(str, str))
        }

    _items = None # type: Dict[str, str]

    def __init__(self, items):
        # type: (Dict[str, str]) -> None
        self._items = items

    @property
    def items(self):
        # type: () -> Dict[str, str]
        return self._items

class EnumExample(ConjureEnumType):
    '''This enumerates the numbers 1:2.
'''

    ONE = 'ONE'
    '''ONE'''
    TWO = 'TWO'
    '''TWO'''
    UNKNOWN = 'UNKNOWN'
    '''UNKNOWN'''

class BooleanExample(ConjureBeanType):

    @classmethod
    def _fields(cls):
        # type: () -> Dict[str, ConjureFieldDefinition]
        return {
            'coin': ConjureFieldDefinition('coin', bool)
        }

    _coin = None # type: bool

    def __init__(self, coin):
        # type: (bool) -> None
        self._coin = coin

    @property
    def coin(self):
        # type: () -> bool
        return self._coin

class AnyExample(ConjureBeanType):

    @classmethod
    def _fields(cls):
        # type: () -> Dict[str, ConjureFieldDefinition]
        return {
            'any': ConjureFieldDefinition('any', object)
        }

    _any = None # type: Any

    def __init__(self, any):
        # type: (Any) -> None
        self._any = any

    @property
    def any(self):
        # type: () -> Any
        return self._any

class AnyMapExample(ConjureBeanType):

    @classmethod
    def _fields(cls):
        # type: () -> Dict[str, ConjureFieldDefinition]
        return {
            'items': ConjureFieldDefinition('items', DictType(str, object))
        }

    _items = None # type: Dict[str, Any]

    def __init__(self, items):
        # type: (Dict[str, Any]) -> None
        self._items = items

    @property
    def items(self):
        # type: () -> Dict[str, Any]
        return self._items

class PrimitiveOptionalsExample(ConjureBeanType):

    @classmethod
    def _fields(cls):
        # type: () -> Dict[str, ConjureFieldDefinition]
        return {
            'num': ConjureFieldDefinition('num', OptionalType(float)),
            'bool': ConjureFieldDefinition('bool', OptionalType(bool)),
            'integer': ConjureFieldDefinition('integer', OptionalType(int)),
            'safelong': ConjureFieldDefinition('safelong', OptionalType(int)),
            'rid': ConjureFieldDefinition('rid', OptionalType(str)),
            'bearertoken': ConjureFieldDefinition('bearertoken', OptionalType(str))
        }

    _num = None # type: Optional[float]
    _bool = None # type: Optional[bool]
    _integer = None # type: Optional[int]
    _safelong = None # type: Optional[int]
    _rid = None # type: Optional[str]
    _bearertoken = None # type: Optional[str]

    def __init__(self, num, bool, integer, safelong, rid, bearertoken):
        # type: (Optional[float], Optional[bool], Optional[int], Optional[int], Optional[str], Optional[str]) -> None
        self._num = num
        self._bool = bool
        self._integer = integer
        self._safelong = safelong
        self._rid = rid
        self._bearertoken = bearertoken

    @property
    def num(self):
        # type: () -> Optional[float]
        return self._num

    @property
    def bool(self):
        # type: () -> Optional[bool]
        return self._bool

    @property
    def integer(self):
        # type: () -> Optional[int]
        return self._integer

    @property
    def safelong(self):
        # type: () -> Optional[int]
        return self._safelong

    @property
    def rid(self):
        # type: () -> Optional[str]
        return self._rid

    @property
    def bearertoken(self):
        # type: () -> Optional[str]
        return self._bearertoken

class ManyFieldExample(ConjureBeanType):

    @classmethod
    def _fields(cls):
        # type: () -> Dict[str, ConjureFieldDefinition]
        return {
            'string': ConjureFieldDefinition('string', str),
            'integer': ConjureFieldDefinition('integer', int),
            'integer_example': ConjureFieldDefinition('integerExample', IntegerExample),
            'double_value': ConjureFieldDefinition('doubleValue', float),
            'optional_item': ConjureFieldDefinition('optionalItem', OptionalType(str)),
            'items': ConjureFieldDefinition('items', ListType(str)),
            'set': ConjureFieldDefinition('set', ListType(str)),
            'map': ConjureFieldDefinition('map', DictType(str, str))
        }

    _string = None # type: str
    _integer = None # type: int
    _integer_example = None # type: IntegerExample
    _double_value = None # type: float
    _optional_item = None # type: Optional[str]
    _items = None # type: List[str]
    _set = None # type: List[str]
    _map = None # type: Dict[str, str]

    def __init__(self, string, integer, integer_example, double_value, optional_item, items, set, map):
        # type: (str, int, IntegerExample, float, Optional[str], List[str], List[str], Dict[str, str]) -> None
        self._string = string
        self._integer = integer
        self._integer_example = integer_example
        self._double_value = double_value
        self._optional_item = optional_item
        self._items = items
        self._set = set
        self._map = map

    @property
    def string(self):
        # type: () -> str
        return self._string

    @property
    def integer(self):
        # type: () -> int
        return self._integer

    @property
    def integer_example(self):
        # type: () -> IntegerExample
        return self._integer_example

    @property
    def double_value(self):
        # type: () -> float
        return self._double_value

    @property
    def optional_item(self):
        # type: () -> Optional[str]
        return self._optional_item

    @property
    def items(self):
        # type: () -> List[str]
        return self._items

    @property
    def set(self):
        # type: () -> List[str]
        return self._set

    @property
    def map(self):
        # type: () -> Dict[str, str]
        return self._map

class UnionTypeExample(ConjureUnionType):
    '''A type which can either be a StringExample, a set of strings, or an integer.'''

    _string_example = None # type: StringExample
    _set = None # type: List[str]
    _number = None # type: int

    @classmethod
    def _options(cls):
        # type: () -> Dict[str, ConjureFieldDefinition]
        return {
            'string_example': ConjureFieldDefinition('stringExample', StringExample),
            'set': ConjureFieldDefinition('set', ListType(str)),
            'number': ConjureFieldDefinition('number', int)
        }

    def __init__(self, string_example=None, set=None, number=None):
        if (string_example is not None) + (set is not None) + (number is not None) != 1:
            raise ValueError('a union must contain a single member')

        if string_example is not None:
            self._string_example = string_example
            self._type = 'stringExample'
        if set is not None:
            self._set = set
            self._type = 'set'
        if number is not None:
            self._number = number
            self._type = 'number'

    @property
    def string_example(self):
        # type: () -> StringExample
        '''Docs for when UnionTypeExample is of type StringExample.'''
        return self._string_example

    @property
    def set(self):
        # type: () -> List[str]
        return self._set

    @property
    def number(self):
        # type: () -> int
        return self._number

class UnionTypeKeywordFields(ConjureUnionType):

    __return = None # type: str
    __if = None # type: int
    __and = None # type: float
    __lambda = None # type: UnionTypeExample

    @classmethod
    def _options(cls):
        # type: () -> Dict[str, ConjureFieldDefinition]
        return {
            '_return': ConjureFieldDefinition('return', str),
            '_if': ConjureFieldDefinition('if', int),
            '_and': ConjureFieldDefinition('and', float),
            '_lambda': ConjureFieldDefinition('lambda', UnionTypeExample)
        }

    def __init__(self, _return=None, _if=None, _and=None, _lambda=None):
        if (_return is not None) + (_if is not None) + (_and is not None) + (_lambda is not None) != 1:
            raise ValueError('a union must contain a single member')

        if _return is not None:
            self.__return = _return
            self._type = 'return'
        if _if is not None:
            self.__if = _if
            self._type = 'if'
        if _and is not None:
            self.__and = _and
            self._type = 'and'
        if _lambda is not None:
            self.__lambda = _lambda
            self._type = 'lambda'

    @property
    def _return(self):
        # type: () -> str
        return self.__return

    @property
    def _if(self):
        # type: () -> int
        return self.__if

    @property
    def _and(self):
        # type: () -> float
        return self.__and

    @property
    def _lambda(self):
        # type: () -> UnionTypeExample
        return self.__lambda

class EmptyObjectExample(ConjureBeanType):

    @classmethod
    def _fields(cls):
        # type: () -> Dict[str, ConjureFieldDefinition]
        return {
        }



