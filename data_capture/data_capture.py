from typing import List
from collections import OrderedDict

from data_capture.utils import execution_time


class Stats:
    """Structure to process statistics based on input from DataStructure."""

    def __init__(self, data:List[int]) -> None:
        # TODO build_stats at most linear O(n)
        self.input = OrderedDict()
        for inp in sorted(data):
            self.input.setdefault(inp, 0)
            self.input[inp] += 1

    @execution_time
    def less(self, value:int) -> None:
        """Quantity of elements on input lower than a reference.
        Args:
            value (int): Reference value for statistics
        Return:
            Integer with statistics.
        """
        # TODO constant time O(1)
        count = 0
        for key, qty in self.input.items():
            if key < value:
                count += qty
            else:
                break
        
        return count

    @execution_time
    def between(self, ge:int, le:int) -> None:
        """Quantity of elements on input between a reference range.
        Args:
            ge (int): 'Greater or equal' reference value for statistics
            le (int): 'Lower or equal' reference value for statistics
        Return:
            Integer with statistics.
        """
        # TODO constant time O(1)
        count = 0
        for key, qty in self.input.items():
            if key >= ge and key <= le:
                count += qty
            elif key > le:
                break

        return count

    @execution_time
    def greater(self, value:int) -> None:
        """Quantity of elements on input greater than a reference.
        Args:
            value (int): Reference value for statistics
        Return:
            Integer with statistics.
        """
        # TODO constant time O(1)
        count = 0
        for key, qty in reversed(self.input.items()):
            if key > value:
                count += qty
            else:
                break
        
        return count


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
        
        if isinstance(value, int) and value > 0:
            self.data.append(value)
        else:
            print('Invalid input.')

    @execution_time
    def build_stats(self) -> Stats:
        """Creates a Stats object to evaluate the current instance input."""
        self.stats = Stats(self.data)
        return self.stats
