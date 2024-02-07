#!/usr/bin/python3
"""docs"""


def print_statistics(total_size, status_count):
    """docs"""
    print("File size: {}".format(total_size))
    for key in sorted(status_count):
        print("{}: {}".format(key, status_count[key]))


if __name__ == "__main__":
    import sys

    total_size = 0
    status_count = {}
    valid_codes = ['200', '301', '400', '401', '403', '404', '405', '500']
    count = 0

    try:
        for line in sys.stdin:
            if count == 10:
                print_statistics(total_size, status_count)
                count = 1
            else:
                count += 1

            line = line.split()

            try:
                total_size += int(line[-1])
            except (IndexError, ValueError):
                pass

            try:
                if line[-2] in valid_codes:
                    if status_count.get(line[-2], -1) == -1:
                        status_count[line[-2]] = 1
                    else:
                        status_count[line[-2]] += 1
            except IndexError:
                pass

        print_statistics(total_size, status_count)

    except KeyboardInterrupt:
        print_statistics(total_size, status_count)
        raise
