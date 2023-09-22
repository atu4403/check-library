import math
import re


class Check:
    """
    Examples:
        >>> check = Check()
        >>> check.reset() # Reset the internal counter
        >>> check.equal(1, 1) # Passes when objects are equal
        >>> check.notEqual(1, 2) # Passes when objects are not equal
        >>> check.assert_calls(2) # Should pass as exactly two assertions have been made
        >>> check.equal(1, 2, msg='Numbers are not equal!')  # Fails and displays custom message
        Traceback (most recent call last):
            ...
        AssertionError: Numbers are not equal!
    """

    def __init__(self):
        self._count = 0
        self.isTruthy = self.isOk
        self.isFalsy = self.isNotOk
        self.isAtLeast = self.isAboveOrEqual
        self.isAtMost = self.isBelowOrEqual
        self.Is = self.deepEqual

    def _inc(self):
        self._count += 1

    def reset(self):
        """
        Resets the internal assertion counter of the Check instance to its initial state.

        This method is useful for resetting the state of the Check instance when you
        want to start a new set of assertions without creating a new instance.

        Examples:
            >>> check = Check()
            >>> check.reset()
            >>> check.equal(1, 1)  # This will be the first assertion after reset
            >>> check.assert_calls(1)  # Should pass as there's only one assertion after reset
        """
        self._count = 0

    def assert_calls(self, expected, msg=None):
        """
        Validates the number of assertions made on the Check instance.

        Args:
            expected_count (int): The expected number of assertions that should have been made.

        Raises:
            AssertionError: If the number of assertions made does not match the expected_count.

        Examples:
            >>> check = Check()
            >>> check.reset()
            >>> check.equal(1, 1)
            >>> check.notEqual(1, 2)
            >>> check.assert_calls(2)  # Should pass as exactly two assertions have been made
        """
        assert self._count == expected, msg or "expected %d calls, got %d" % (
            expected,
            self._count,
        )

    def isNone(self, obj, msg=None):
        """
        Checks if the given object is None.

        Args:
            obj: The object to be checked for None.
            msg (str, optional): An optional message to be displayed if the check fails.

        Raises:
            AssertionError: If the provided object is not None.

        Examples:
            >>> check.isNone(None)  # Passes when None is provided
            >>> check.isNone(False)  # Fails when False is provided
            Traceback (most recent call last):
                ...
            AssertionError: Object is not None
        """
        self._inc()
        assert obj is None, msg or "Object is not None"

    def isNotNone(self, obj, msg=None):
        """
        Checks if the given object is not None.

        Args:
            obj: The object to be checked.
            msg (str, optional): An optional message to be displayed if the check fails.

        Raises:
            AssertionError: If the object is None.

        Examples:
            >>> check.isNotNone("not None")  # Passes when not None
            >>> check.isNotNone(None)  # Fails when None
            Traceback (most recent call last):
                ...
            AssertionError: Object is None
        """
        self._inc()
        assert obj is not None, msg or "Object is None"

    def isOk(self, obj, msg=None):
        """
        Checks if the given object is truthy (e.g., not 0, None, False).

        Args:
            obj: The object to be checked.
            msg (str, optional): An optional message to be displayed if the check fails.

        Raises:
            AssertionError: If the object is falsy.

        Examples:
            >>> check.isOk(1)  # Passes when object is truthy
            >>> check.isOk(0)  # Fails when object is falsy
            Traceback (most recent call last):
                ...
            AssertionError: Object is falsy
        """
        self._inc()
        assert obj, msg or "Object is falsy"

    def isNotOk(self, obj, msg=None):
        """
        Checks if the given object is falsy (e.g., 0, None, False).

        Args:
            obj: The object to be checked.
            msg (str, optional): An optional message to be displayed if the check fails.

        Raises:
            AssertionError: If the object is truthy.

        Examples:
            >>> check.isNotOk(0)  # Passes when object is falsy
            >>> check.isNotOk(1)  # Fails when object is truthy
            Traceback (most recent call last):
                ...
            AssertionError: Object is truthy
        """
        self._inc()
        assert not obj, msg or "Object is truthy"

    def equal(self, obj1, obj2, msg=None):
        """
        Checks if two given objects are equal.

        Args:
            obj1: The first object to be compared.
            obj2: The second object to be compared.
            msg (str, optional): An optional message to be displayed if the check fails.

        Raises:
            AssertionError: If the objects are not equal.

        Examples:
            >>> check.equal(1, 1)  # Passes when objects are equal
            >>> check.equal(1, 2)  # Fails when objects are not equal
            Traceback (most recent call last):
                ...
            AssertionError: 1 != 2
        """
        self._inc()
        assert obj1 == obj2, msg or f"{obj1} != {obj2}"

    def deepEqual(self, obj1, obj2, msg=None):
        """
        Checks if two given objects are identical (same memory location).

        Args:
            obj1: The first object to be compared.
            obj2: The second object to be compared.
            msg (str, optional): An optional message to be displayed if the check fails.

        Raises:
            AssertionError: If the objects are not identical.

        Examples:
            >>> a = [1, 2, 3]
            >>> b = a
            >>> check.deepEqual(a, b)  # Passes when objects are identical
            >>> check.deepEqual(a, [1, 2, 3])  # Fails when objects are not identical
            Traceback (most recent call last):
                ...
            AssertionError: Objects are not the same (not identical)
        """
        self._inc()
        assert obj1 is obj2, msg or "Objects are not the same (not identical)"

    def notEqual(self, obj1, obj2, msg=None):
        """
        Checks if two given objects are not equal.

        Args:
            obj1: The first object to be compared.
            obj2: The second object to be compared.
            msg (str, optional): An optional message to be displayed if the check fails.

        Raises:
            AssertionError: If the objects are equal.

        Examples:
            >>> check.notEqual(1, 2)  # Passes when objects are not equal
            >>> check.notEqual(1, 1)  # Fails when objects are equal
            Traceback (most recent call last):
                ...
            AssertionError: 1 == 1
        """
        self._inc()
        assert obj1 != obj2, msg or f"{obj1} == {obj2}"

    def notDeepEqual(self, obj1, obj2, msg=None):
        """
        Checks if two given objects are not identical (do not refer to the same memory location).

        Args:
            obj1: The first object to be compared.
            obj2: The second object to be compared.
            msg (str, optional): An optional message to be displayed if the check fails.

        Raises:
            AssertionError: If the objects are identical.

        Examples:
            >>> a = [1, 2, 3]
            >>> check.notDeepEqual(a, [1, 2, 3])  # Passes when objects are not identical
            >>> b = a
            >>> check.notDeepEqual(a, b)  # Fails when objects are identical
            Traceback (most recent call last):
                ...
            AssertionError: Objects are the same (identical)
        """
        self._inc()
        assert obj1 is not obj2, msg or "Objects are the same (identical)"

    def isAbove(self, obj1, obj2, msg=None):
        """
        Checks if the first object is greater than the second object.

        Args:
            obj1: The first object to be compared.
            obj2: The second object to be compared.
            msg (str, optional): An optional message to be displayed if the check fails.

        Raises:
            AssertionError: If obj1 is not greater than obj2.

        Examples:
            >>> check.isAbove(2, 1)  # Passes when obj1 is greater than obj2
            >>> check.isAbove(1, 2)  # Fails when obj1 is not greater than obj2
            Traceback (most recent call last):
                ...
            AssertionError: Object is below
        """
        self._inc()
        assert obj1 > obj2, msg or "Object is below"

    def isBelow(self, obj1, obj2, msg=None):
        """
        Checks if the first object is less than the second object.

        Args:
            obj1: The first object to be compared.
            obj2: The second object to be compared.
            msg (str, optional): An optional message to be displayed if the check fails.

        Raises:
            AssertionError: If obj1 is not less than obj2.

        Examples:
            >>> check.isBelow(1, 2)  # Passes when obj1 is less than obj2
            >>> check.isBelow(2, 1)  # Fails when obj1 is not less than obj2
            Traceback (most recent call last):
                ...
            AssertionError: Object is above
        """
        self._inc()
        assert obj1 < obj2, msg or "Object is above"

    def isAboveOrEqual(self, obj1, obj2, msg=None):
        """
        Checks if the first object is greater than or equal to the second object.

        Args:
            obj1: The first object to be compared.
            obj2: The second object to be compared.
            msg (str, optional): An optional message to be displayed if the check fails.

        Raises:
            AssertionError: If obj1 is not greater than or equal to obj2.

        Examples:
            >>> check.isAboveOrEqual(2, 1)  # Passes when obj1 is greater than or equal to obj2
            >>> check.isAboveOrEqual(1, 2)  # Fails when obj1 is not greater than or equal to obj2
            Traceback (most recent call last):
                ...
            AssertionError: Object is below
        """
        self._inc()
        assert obj1 >= obj2, msg or "Object is below"

    def isBelowOrEqual(self, obj1, obj2, msg=None):
        """
        Checks if the first object is less than or equal to the second object.

        Args:
            obj1: The first object to be compared.
            obj2: The second object to be compared.
            msg (str, optional): An optional message to be displayed if the check fails.

        Raises:
            AssertionError: If obj1 is not less than or equal to obj2.

        Examples:
            >>> check.isBelowOrEqual(1, 2)  # Passes when obj1 is less than or equal to obj2
            >>> check.isBelowOrEqual(2, 1)  # Fails when obj1 is not less than or equal to obj2
            Traceback (most recent call last):
                ...
            AssertionError: Object is above
        """
        self._inc()
        assert obj1 <= obj2, msg or "Object is above"

    def isTrue(self, obj, msg=None):
        """
        Checks if the given object is True.

        Args:
            obj: The object to be checked.
            msg (str, optional): An optional message to be displayed if the check fails.

        Raises:
            AssertionError: If the object is not True.

        Examples:
            >>> check.isTrue(True)  # Passes when object is True
            >>> check.isTrue(False)  # Fails when object is not True
            Traceback (most recent call last):
                ...
            AssertionError: Object not True
        """
        self._inc()
        assert obj is True, msg or "Object not True"

    def isFalse(self, obj, msg=None):
        """
        Checks if the given object is False.

        Args:
            obj: The object to be checked.
            msg (str, optional): An optional message to be displayed if the check fails.

        Raises:
            AssertionError: If the object is not False.

        Examples:
            >>> check.isFalse(False)  # Passes when object is False
            >>> check.isFalse(True)  # Fails when object is not False
            Traceback (most recent call last):
                ...
            AssertionError: Object not False
        """
        self._inc()
        assert obj is False, msg or "Object not False"

    def isZero(self, obj, msg=None):
        """
        Checks if the given object is zero.

        Args:
            obj: The object to be checked.
            msg (str, optional): An optional message to be displayed if the check fails.

        Raises:
            AssertionError: If the object is not zero.

        Examples:
            >>> check.isZero(0)  # Passes when object is 0
            >>> check.isZero(1)  # Fails when object is not 0
            Traceback (most recent call last):
                ...
            AssertionError: Object not 0
        """
        self._inc()
        assert obj == 0, msg or "Object not 0"

    def isNotZero(self, obj, msg=None):
        """
        Checks if the given object is zero.

        Args:
            obj: The object to be checked.
            msg (str, optional): An optional message to be displayed if the check fails.

        Raises:
            AssertionError: If the object is not zero.

        Examples:
            >>> check.isZero(0)  # Passes when object is 0
            >>> check.isZero(1)  # Fails when object is not 0
            Traceback (most recent call last):
                ...
            AssertionError: Object not 0
        """
        self._inc()
        assert obj != 0, msg or "Object is 0"

    def isList(self, obj, msg=None):
        """
        Checks if the given object is a list.

        Args:
            obj: The object to be checked.
            msg (str, optional): An optional message to be displayed if the check fails.

        Raises:
            AssertionError: If the object is not a list.

        Examples:
            >>> check.isList([1, 2, 3])  # Passes when object is a list
            >>> check.isList({"key": "value"})  # Fails when object is not a list
            Traceback (most recent call last):
                ...
            AssertionError: Object is not a list
        """
        self._inc()
        assert isinstance(obj, list), msg or "Object is not a list"

    def isDict(self, obj, msg=None):
        """
        Checks if the given object is a dictionary.

        Args:
            obj: The object to be checked.
            msg (str, optional): An optional message to be displayed if the check fails.

        Raises:
            AssertionError: If the object is not a dictionary.

        Examples:
            >>> check.isDict({"key": "value"})  # Passes when object is a dictionary
            >>> check.isDict([1, 2, 3])  # Fails when object is not a dictionary
            Traceback (most recent call last):
                ...
            AssertionError: Object is not a dict
        """
        self._inc()
        assert isinstance(obj, dict), msg or "Object is not a dict"

    def isInt(self, obj, msg=None):
        """
        Checks if the given object is an integer.

        Args:
            obj: The object to be checked.
            msg (str, optional): An optional message to be displayed if the check fails.

        Raises:
            AssertionError: If the object is not an integer.

        Examples:
            >>> check.isInt(1)  # Passes when object is an integer
            >>> check.isInt(1.5)  # Fails when object is not an integer
            Traceback (most recent call last):
                ...
            AssertionError: Object is not an integer
        """
        self._inc()
        assert isinstance(obj, int), msg or "Object is not an integer"

    def isFloat(self, obj, msg=None):
        """
        Checks if the given object is a float.

        Args:
            obj: The object to be checked.
            msg (str, optional): An optional message to be displayed if the check fails.

        Raises:
            AssertionError: If the object is not a float.

        Examples:
            >>> check.isFloat(1.5)  # Passes when object is a float
            >>> check.isFloat(1)  # Fails when object is not a float
            Traceback (most recent call last):
                ...
            AssertionError: Object is not a float
        """
        self._inc()
        assert isinstance(obj, float), msg or "Object is not a float"

    def isStr(self, obj, msg=None):
        """
        Checks if the given object is a string.

        Args:
            obj: The object to be checked.
            msg (str, optional): An optional message to be displayed if the check fails.

        Raises:
            AssertionError: If the object is not a string.

        Examples:
            >>> check.isStr("hello")  # Passes when object is a string
            >>> check.isStr(1)  # Fails when object is not a string
            Traceback (most recent call last):
                ...
            AssertionError: Object is not a string
        """
        self._inc()
        assert isinstance(obj, str), msg or "Object is not a string"

    def isBool(self, obj, msg=None):
        """
        Checks if the given object is a boolean.

        Args:
            obj: The object to be checked.
            msg (str, optional): An optional message to be displayed if the check fails.

        Raises:
            AssertionError: If the object is not a boolean.

        Examples:
            >>> check.isBool(True)  # Passes when object is a boolean
            >>> check.isBool(1)  # Fails when object is not a boolean
            Traceback (most recent call last):
                ...
            AssertionError: Object is not a boolean
        """
        self._inc()
        assert isinstance(obj, bool), msg or "Object is not a boolean"

    def isCallable(self, obj, msg=None):
        """
        Checks if the given object is callable (e.g., a function or method).

        Args:
            obj: The object to be checked.
            msg (str, optional): An optional message to be displayed if the check fails.

        Raises:
            AssertionError: If the object is not callable.

        Examples:
            >>> check.isCallable(lambda x: x + 1)  # Passes when object is callable
            >>> check.isCallable("not callable")  # Fails when object is not callable
            Traceback (most recent call last):
                ...
            AssertionError: Object is not callable
        """
        self._inc()
        assert callable(obj), msg or "Object is not callable"

    def isListSubset(self, sub_list, main_list, msg=None):
        """
        Checks if the given list is a subset of another list.

        Args:
            subset (list): The subset list to be checked.
            superset (list): The superset list against which to check.
            msg (str, optional): An optional message to be displayed if the check fails.

        Raises:
            AssertionError: If the subset list is not a subset of the superset list.

        Examples:
            >>> check.isListSubset([1], [1, 2, 3])  # Passes when subset is a subset of superset
            >>> check.isListSubset([1, 4], [1, 2, 3])  # Fails when subset is not a subset of superset
            Traceback (most recent call last):
                ...
            AssertionError: sub_list is not in main_list
        """

        self._inc()
        assert all(i in main_list for i in sub_list), (
            msg or "sub_list is not in main_list"
        )

    def isDictSubset(self, sub_dict, main_dict, msg=None):
        """
        Checks if the given dictionary is a subset of another dictionary.

        Args:
            subset (dict): The subset dictionary to be checked.
            superset (dict): The superset dictionary against which to check.
            msg (str, optional): An optional message to be displayed if the check fails.

        Raises:
            AssertionError: If the subset dictionary is not a subset of the superset dictionary.

        Examples:
            >>> check.isDictSubset({'a': 1}, {'a': 1, 'b': 2})  # Passes when subset is a subset of superset
            >>> check.isDictSubset({'a': 1, 'c': 3}, {'a': 1, 'b': 2})  # Fails when subset is not a subset of superset
            Traceback (most recent call last):
                ...
            AssertionError: sub_dict is not in main_dict
        """
        self._inc()
        assert all(item in main_dict.items() for item in sub_dict.items()), (
            msg or "sub_dict is not in main_dict"
        )

    def isNan(self, obj, msg=None):
        """
        Checks if the given object is NaN (Not a Number).

        Args:
            obj: The object to be checked.
            msg (str, optional): An optional message to be displayed if the check fails.

        Raises:
            AssertionError: If the object is not NaN.

        Examples:
            >>> import math
            >>> check.isNan(math.nan)  # Passes when object is NaN
            >>> check.isNan(1)  # Fails when object is not NaN
            Traceback (most recent call last):
                ...
            AssertionError: Object is not NaN
        """
        self._inc()
        assert math.isnan(obj), msg or "Object is not NaN"

    def isInf(self, obj, msg=None):
        """
        Checks if the given object is a finite number.

        Args:
            obj: The object to be checked.
            msg (str, optional): An optional message to be displayed if the check fails.

        Raises:
            AssertionError: If the object is not a finite number.

        Examples:
            >>> check.isInf(float('inf'))  # Passes when object is a finite number
            >>> check.isInf(1)  # Fails when object is not a finite number
            Traceback (most recent call last):
                ...
            AssertionError: Object is not Inf
        """
        self._inc()
        assert math.isinf(obj), msg or "Object is not Inf"

    def isBinary(self, obj, msg=None):
        """
        Checks if the given object is a binary string.

        Args:
            obj: The object to be checked.
            msg (str, optional): An optional message to be displayed if the check fails.

        Raises:
            AssertionError: If the object is not a binary string.

        Examples:
            >>> check.isBinary(b'binary')  # Passes when object is a binary string
            >>> check.isBinary('not binary')  # Fails when object is not a binary string
            Traceback (most recent call last):
                ...
            AssertionError: Object is not a binary string
        """
        self._inc()
        assert isinstance(obj, bytes), msg or "Object is not a binary string"

    def isNotNan(self, obj, msg=None):
        """
        Checks if the given object is not NaN (Not a Number).

        Args:
            obj: The object to be checked.
            msg (str, optional): An optional message to be displayed if the check fails.

        Raises:
            AssertionError: If the object is NaN.

        Examples:
            >>> check.isNotNan(1)  # Passes when object is not NaN
            >>> import math
            >>> check.isNotNan(math.nan)  # Fails when object is NaN
            Traceback (most recent call last):
                ...
            AssertionError: Object is NaN
        """
        self._inc()
        assert not math.isnan(obj), msg or "Object is NaN"

    def isNotInf(self, obj, msg=None):
        """
        Checks if the given object is not an infinite number.

        Args:
            obj: The object to be checked.
            msg (str, optional): An optional message to be displayed if the check fails.

        Raises:
            AssertionError: If the object is infinite.

        Examples:
            >>> check.isNotInf(1)  # Passes when object is not infinite
            >>> import math
            >>> check.isNotInf(math.inf)  # Fails when object is infinite
            Traceback (most recent call last):
                ...
            AssertionError: Object is infinite
        """
        self._inc()
        assert not math.isinf(obj), msg or "Object is infinite"

    def In(self, sub, main, msg=None):
        """
        Checks if the given object exists within the specified iterable.

        Args:
            obj: The object to be checked.
            iterable: The iterable in which to check for the object.
            msg (str, optional): An optional message to be displayed if the check fails.

        Raises:
            AssertionError: If the object does not exist in the iterable.

        Examples:
            >>> check.In(1, [1, 2, 3])  # Passes when object is in iterable
            >>> check.In(4, [1, 2, 3])  # Fails when object is not in iterable
            Traceback (most recent call last):
                ...
            AssertionError: Object not in iterable
        """
        self._inc()
        assert sub in main, msg or "Object not in iterable"

    def notIn(self, sub, main, msg=None):
        """
        Checks if the given object does not exist within the specified iterable.

        Args:
            obj: The object to be checked.
            iterable: The iterable in which to check for the object.
            msg (str, optional): An optional message to be displayed if the check fails.

        Raises:
            AssertionError: If the object exists in the iterable.

        Examples:
            >>> check.notIn(4, [1, 2, 3])  # Passes when object is not in iterable
            >>> check.notIn(1, [1, 2, 3])  # Fails when object is in iterable
            Traceback (most recent call last):
                ...
            AssertionError: Object in iterable
        """
        self._inc()
        assert sub not in main, msg or "Object in iterable"

    def match(self, pattern, text, msg=None):
        """
        Checks if the given string matches the specified regular expression pattern.

        Args:
            pattern (str): The regular expression pattern.
            string (str): The string to be checked.
            msg (str, optional): An optional message to be displayed if the check fails.

        Raises:
            AssertionError: If the string does not match the pattern.

        Examples:
            >>> check.match(r'\d+', '123')  # Passes when string matches the pattern
            >>> check.match(r'\d+', 'abc')  # Fails when string does not match the pattern
            Traceback (most recent call last):
                ...
            AssertionError: pattern `\d+` does not match text `abc`
        """
        self._inc()
        assert re.match(pattern, text), (
            msg or f"pattern `{pattern}` does not match text `{text}`"
        )

    def notMatch(self, pattern, text, msg=None):
        """
        Checks if the given string does not match the specified regular expression pattern.

        Args:
            pattern (str): The regular expression pattern.
            string (str): The string to be checked.
            msg (str, optional): An optional message to be displayed if the check fails.

        Raises:
            AssertionError: If the string matches the pattern.

        Examples:
            >>> check.notMatch(r'\\d+', 'abc')  # Passes when string does not match the pattern
            >>> check.notMatch(r'\\d+', '123')  # Fails when string matches the pattern
            Traceback (most recent call last):
                ...
            AssertionError: Pattern matched
        """
        self._inc()
        assert not re.match(pattern, text), msg or "Pattern matched"

    def lengthOf(self, obj, length, msg=None):
        self._inc()
        assert len(obj) == length, msg or "Object has wrong length"

    def raises(self, fn, exc, msg=None):
        """
        Checks if the given callable raises the specified exception when called.

        Args:
            exc_type (Exception): The type of exception expected.
            callable_obj: The callable object to be checked.
            *args: Arguments to pass to the callable.
            **kwargs: Keyword arguments to pass to the callable.

        Raises:
            AssertionError: If the callable does not raise the expected exception.

        Examples:
            >>> fn = lambda: 2 / 0
            >>> check.raises(fn, ZeroDivisionError)
            >>> check.raises(fn, ValueError)
            Traceback (most recent call last):
                ...
            AssertionError: Function raised ZeroDivisionError
            >>> fn = lambda: 1
            >>> check.raises(fn, ValueError)
            Traceback (most recent call last):
                ...
            AssertionError: Function did not raise exception
        """
        self._inc()
        try:
            fn()
        except exc:
            return
        except Exception as e:
            exception_class = type(e)
            raise AssertionError(
                msg or f"Function raised {exception_class.__name__}"
            ) from None
        else:
            raise AssertionError(msg or "Function did not raise exception")

    def typeFromStr(self, obj: any, expected_type: str, msg=None):
        """
        Asserts that the type of the given object matches the expected type as a string.

        Args:
            obj (any): The object to check the type of.
            expected_type (str): The expected type as a string (e.g., 'int', 'str', 'list').
            msg (str, optional): A custom error message to display if the assertion fails.

        Raises:
            AssertionError: If the type of `obj` does not match the `expected_type`.

        Examples:
            >>> check.typeFromStr(42, 'int')
            >>> check.typeFromStr("Hello, World!", 'str')
            >>> check.typeFromStr([1, 2, 3], 'list')
            >>> check.typeFromStr(1, 'str')
            Traceback (most recent call last):
                ...
            AssertionError: type(1) is int

        Note:
            This function checks if the type of `obj` matches the `expected_type` as a string.
            For example, `typeFromStr(42, 'int')` will pass because the type of 42 is 'int'.
            However, `typeFromStr(42, 'str')` will fail because the type of 42 is 'int'.

        """
        actual_type = str(type(obj)).split("'")[1]
        assert actual_type == expected_type, msg or f"type({obj}) is {actual_type}"


if __name__ == "__main__":
    import doctest

    doctest.testmod(extraglobs={"check": Check()})
