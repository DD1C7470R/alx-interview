#!/usr/bin/python3
'''script to parse logs'''
import re
from collections import defaultdict


def process_log_line(line):
    '''Retrieves the necessary components from a logged file'''
    pattern = re.compile(r'''
        ^
        (\d+\.\d+\.\d+\.\d+)
        \s-\s\[([^]]+)\]
        \s"GET\s/projects/260\sHTTP/1\.1"\s(\d+)\s(\d+)
        $
        ''', re.VERBOSE)

    is_valid_line = pattern.match(line)

    if not is_valid_line:
        return None

    # Extract relevant information from the match object
    ip_address, date, status_code, file_size = is_valid_line.groups()

    # Convert file_size to an integer
    file_size = int(file_size)

    # Return a dictionary with the extracted information
    return {
            'ip_address': ip_address,
            'date': date, 'status_code': int(status_code),
            'file_size': file_size
            }


def print_statistics(total_file_size, lines_by_status):
    print('File size: {:d}'.format(total_file_size))
    for status_code in sorted(lines_by_status):
        print('{}: {:d}'.format(status_code, lines_by_status[status_code]))


if __name__ == "__main__":
    import sys
    lines_by_status = defaultdict(int)
    total_file_size = 0
    line_count = 0

    try:
        for line in sys.stdin:
            log_entry = process_log_line(line)

            if log_entry:
                total_file_size += log_entry['file_size']
                lines_by_status[log_entry['status_code']] += 1
                line_count += 1

                if line_count % 10 == 0:
                    print_statistics(total_file_size, lines_by_status)

    except KeyboardInterrupt:
        print_statistics(total_file_size, lines_by_status)
        raise
