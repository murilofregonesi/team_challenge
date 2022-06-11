from typing import List

from data_capture.utils import execution_time, is_positive


class Stats:
    """Structure to process statistics based on input from DataStructure."""

    def __init__(self, data:List[int]) -> None:
        """Stats initialization.
        Args:
            data ([int]): Input data of positive integers
        """

        # store input data as a sorted dict of accumulated values
        # example: data = [5, 1, 5] => _input = { 1: 1, 5: 3 }

        sorted_data = sorted(data)
        self._lower_limit = sorted_data[0]
        self._total = len(data)
        self._input = {}

        for i, inp in enumerate(sorted_data):
            accumulated = i + 1
            self._input.setdefault(inp, accumulated)
            self._input[inp] = accumulated

    def _left_search_key(self, initial_key:int) -> int:
        """Returns the left closer key with available data.
        If initial_key has available data, returns initial_key.
        Args:
            initial_key (int): Initial search position
        Return:
            Key of the closer element with available data.
        """
        
        _search_key = initial_key
        
        # shift left until data is found or the end of the input
        while self._input.get(_search_key) is None:
            _search_key -= 1
            if _search_key < self._lower_limit:
                return None
        
        return _search_key
        
    @execution_time
    def less(self, value:int) -> None:
        """Quantity of elements on input lower than a reference.
        Args:
            value (int): Reference value for statistics
        Return:
            Integer with statistics.
        """

        search_key = self._left_search_key(value - 1)
        if search_key:
            return self._input.get(search_key)
        
        return 0

    @execution_time
    def between(self, ge:int, le:int) -> None:
        """Quantity of elements on input between a reference range.
        Args:
            ge (int): 'Greater or equal' reference value for statistics
            le (int): 'Lower or equal' reference value for statistics
        Return:
            Integer with statistics.
        """

        between = self._total
        
        # remove accumulated before lower key
        below_key = self._left_search_key(ge - 1)
        if below_key:
            between -= self._input.get(below_key)
        
        # remove accumulated after upper key
        upper_key = self._left_search_key(le)
        if upper_key:
            between -= self._total - self._input.get(upper_key)
        else:
            between = 0

        return between

    @execution_time
    def greater(self, value:int) -> None:
        """Quantity of elements on input greater than a reference.
        Args:
            value (int): Reference value for statistics
        Return:
            Integer with statistics.
        """

        search_key = self._left_search_key(value)
        if search_key:
            return self._total - self._input.get(search_key)

        return self._total


class DataCapture:
    """Structure to capture input data for statistics evaluation."""

    def __init__(self) -> None:
        self.data = []
        self.stats = None
    
    def add(self, value:int) -> None:
        """Append a new positive value to the input.
        Args:
            value (int): Positive value to be appended
        """
        
        if is_positive(value):
            self.data.append(value)
        else:
            print('Invalid input.')

    @execution_time
    def build_stats(self) -> Stats:
        """Creates a Stats object to evaluate the current instance input."""
        if not self.data:
            print('No input defined.')
            return

        self.stats = Stats(self.data)
        return self.stats
