from data_capture.data_capture import DataCapture


if __name__ == '__main__':

    # standard tests
    capture = DataCapture()

    capture.add(3)
    capture.add(9)
    capture.add(3)
    capture.add(4)
    capture.add(6)

    stats = capture.build_stats()

    assert stats.less(4) == 2 # should return 2 (only two values 3, 3 are less than 4)
    assert stats.between(3, 6) == 4 # should return 4 (3, 3, 4 and 6 are between 3 and 6)
    assert stats.greater(4) == 2 # should return 2 (6 and 9 are the only two values greater than 4)


    # timing tests
    print('\nTiming tests:')

    lengths = [10000, 100000, 1000000]
    for length in lengths:
        print(f'\nLength: {length}')
        
        capture = DataCapture()
        for i in range(1, length):
            capture.add(i)
        
        stats = capture.build_stats() # O(n)

        stats.less(length/2) # O(1)
        stats.between(length//4, length//1.33) # O(1)
        stats.greater(length/2) # O(1)
