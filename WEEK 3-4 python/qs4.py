def count_occurrences(numbers):
    """Function to count and print occurrences of each number in a list"""
    if not numbers:
        print("The list is empty")
        return
    
    occurrence_count = {}
    
    for num in numbers:
        if isinstance(num, (int, float)):
            if num in occurrence_count:
                occurrence_count[num] += 1
            else:
                occurrence_count[num] = 1
        else:
            print(f"Ignoring non-numeric value: {num}")
    
    print("\nNumber Occurrences:")
    print("------------------")
    for num, count in sorted(occurrence_count.items()):
        print(f"{num}: {count} time(s)")

# Test cases
def test_count_occurrences():
    # Test 1: Normal case with integers
    print("\nTest 1: Normal case with integers")
    count_occurrences([2, 3, 2, 5, 3, 7, 5, 5, 3])
    
    # Test 2: Mixed numbers and non-numbers
    print("\nTest 2: Mixed numbers and non-numbers")
    count_occurrences([1, 'a', 2.5, 1, 2.5, None, 3])
    
    # Test 3: Empty list
    print("\nTest 3: Empty list")
    count_occurrences([])
    
    # Test 4: All same numbers
    print("\nTest 4: All same numbers")
    count_occurrences([4, 4, 4, 4])
    
    # Test 5: Floating point numbers
    print("\nTest 5: Floating point numbers")
    count_occurrences([1.5, 2.0, 1.5, 3.5, 2.0, 2.0])
    
    # Test 6: Large numbers
    print("\nTest 6: Large numbers")
    count_occurrences([1000000, 999999, 1000000, 888888, 999999])

# Run the tests
if __name__ == "__main__":
    print("TESTING NUMBER OCCURRENCE COUNTER")
    print("--------------------------------")
    test_count_occurrences()