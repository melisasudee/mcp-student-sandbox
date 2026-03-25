def average_ratios(numbers):
    """
    Calculate average of ratios (100 / number) for each number in list.
    Skips zeros to avoid division by zero.
    
    Args:
        numbers: List of numeric values
    
    Returns:
        Average of valid ratios, or 0 if no valid numbers
    """
    # Handle empty list
    if not numbers:
        return 0
    
    # Filter out zeros and calculate ratios
    valid_ratios = []
    for num in numbers:
        if num != 0:  # Skip zeros
            valid_ratios.append(100 / num)
    
    # Handle case where all values were zeros
    if not valid_ratios:
        return 0
    
    # Return average of valid ratios
    return sum(valid_ratios) / len(valid_ratios)


if __name__ == "__main__":
    # Only runs when executed directly, not when imported
    print("Test: average_ratios([10, 5, 0]) =", average_ratios([10, 5, 0]))
    print("Test: average_ratios([0, 0, 0]) =", average_ratios([0, 0, 0]))
    print("Test: average_ratios([]) =", average_ratios([]))
