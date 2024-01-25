#!/usr/bin/python3
'''script to parse logs'''
from collections import defaultdict


def process_log_line(line):
    '''Retrieves the necessary components from a logged file'''
    try:
        is_valid_line = line.split()
        if not is_valid_line:
            return None
        # Extract relevant information from the match object
        status_code = is_valid_line[-2]
        file_size = is_valid_line[-1]
        # Convert file_size to an integer
        file_size = int(file_size)
    except BaseException:
        pass
        # Return a dictionary with the extracted information
    return {
             'status_code': status_code,
            'file_size': file_size
            }


def print_statistics(total_file_size, lines_by_status) -> None:
    print('File size: {:d}'.format(total_file_size))
    for status_code in sorted(lines_by_status):
        print('{}: {:d}'.format(status_code, lines_by_status[status_code]))


if __name__ == "__main__":
    import sys
    lines_by_status = defaultdict(int)
    total_file_size = 0
    line_count = 0
    codes =  ["200", "301", "400", "401", "403", "404", "405", "500"]
    try:
        for line in sys.stdin:
            log_entry = process_log_line(line)
            if log_entry:
                try:
                    total_file_size += log_entry['file_size']
                    if log_entry['status_code'] in codes:
                        lines_by_status[log_entry['status_code']] += 1
                except BaseException:
                    pass
                line_count += 1
                if line_count % 10 == 0:
                    print_statistics(total_file_size, lines_by_status)
        print_statistics(total_file_size, lines_by_status)
    except KeyboardInterrupt:
        print_statistics(total_file_size, lines_by_status)
        raise
