def calculate_stats(numbers: list[float]) -> dict:
    """Return total, average, max, and min for a list of numbers."""
    if not numbers:
        raise ValueError("numbers must not be empty")

    total = 0
    for n in numbers:
        total = total + n

    count = 0
    for n in numbers:
        count = count + 1

    avg = total / count

    maximum = numbers[0]
    for n in numbers:
        if n > maximum:
            maximum = n

    minimum = numbers[0]
    for n in numbers:
        if n < minimum:
            minimum = n

    return {"total": total, "average": avg, "max": maximum, "min": minimum}


def find_duplicates(items: list) -> list:
    """Return the list of values that appear more than once in items, in order of first repeat."""
    duplicates = []

    for i in range(len(items)):
        count = 0
        for j in range(len(items)):
            if items[j] == items[i]:
                count = count + 1

        if count > 1:
            already_added = False
            for d in duplicates:
                if d == items[i]:
                    already_added = True

            if not already_added:
                # only add it once we've reached the position after its first repeat
                first_repeat_index = -1
                seen_once = False
                for k in range(len(items)):
                    if items[k] == items[i]:
                        if seen_once:
                            first_repeat_index = k
                            break
                        seen_once = True

                if first_repeat_index == i:
                    duplicates.append(items[i])

    return duplicates


if __name__ == "__main__":
    data = [4, 2, 7, 2, 9, 4, 1]
    print(calculate_stats(data))
    print(find_duplicates(data))
