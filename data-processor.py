def calculate_stats(numbers: list[float]) -> dict:
    """Return total, average, max, and min for a list of numbers."""
    if not numbers:
        raise ValueError("numbers must not be empty")

    return {
        "total": sum(numbers),
        "average": sum(numbers) / len(numbers),
        "max": max(numbers),
        "min": min(numbers),
    }


def find_duplicates(items: list) -> list:
    """Return the list of values that appear more than once in items, in order of first repeat."""
    seen = set()
    already_added = set()
    duplicates = []

    for item in items:
        if item in seen and item not in already_added:
            duplicates.append(item)
            already_added.add(item)
        seen.add(item)

    return duplicates


if __name__ == "__main__":
    data = [4, 2, 7, 2, 9, 4, 1]
    print(calculate_stats(data))
    print(find_duplicates(data))
