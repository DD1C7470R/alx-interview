#!/usr/bin/python3
'''script to parse logs'''
from collections import defaultdict


def print_statistics(total_file_size, lines_by_status) -> None:
    print('File size: {:d}'.format(total_file_size))
    for status_code in sorted(lines_by_status):
        print('{}: {:d}'.format(status_code, lines_by_status[status_code]))


if __name__ == "__main__":
    import sys
    lines_by_status = defaultdict(int)
    total_file_size = 0
    line_count = 0
    file_size = 0
    codes = ["200", "301", "400", "401", "403", "404", "405", "500"]
    try:
        for line in sys.stdin:
            line_count += 1
            is_valid_line = line.split()
            # Extract relevant information from the match object
            try:
                status_code = is_valid_line[-2]
                file_size += int(is_valid_line[-1])

                try:
                    if status_code in codes:
                        lines_by_status[status_code] += 1
                except BaseException:
                    pass
            except BaseException:
                pass
            if line_count % 10 == 0:
                print_statistics(file_size, lines_by_status)
        print_statistics(file_size, lines_by_status)
    except KeyboardInterrupt:
        print_statistics(file_size, lines_by_status)
        raise
