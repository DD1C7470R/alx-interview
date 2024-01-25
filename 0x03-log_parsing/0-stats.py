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


def compute_metrics(log_lines):
    '''Retrieves the necessary components from a logged file'''
    total_file_size = 0
    status_codes = {}
    for line in log_lines:
        processed_line = process_log_line(line)
        total_file_size += processed_line['file_size']

        if str(processed_line['status_code']) in list(status_codes.keys()):
            val = status_codes.get('{}'.format(processed_line['status_code']))
            status_codes.update(
                    {'{}'.format(processed_line['status_code']): val + 1}
            )
        else:
            status_codes['{}'.format(processed_line['status_code'])] = 1
    return {
        'total_file_size': total_file_size,
        'status_codes': status_codes
    }


def print_statistics(total_file_size, lines_by_status):
    print(f'File size: {total_file_size}')
    for status_code in sorted(lines_by_status):
        print(f'{status_code}: {lines_by_status[status_code]}')


if __name__ == "__main__":
    lines_by_status = defaultdict(int)
    total_file_size = 0
    line_count = 0

    try:
        for line in iter(input, ''):
            log_entry = process_log_line(line)

            if log_entry:
                total_file_size += log_entry['file_size']
                lines_by_status[log_entry['status_code']] += 1
                line_count += 1

                if line_count % 10 == 0:
                    print_statistics(total_file_size, lines_by_status)

    except KeyboardInterrupt:
        print("\nKeyboard interruption. Printing current statistics:")
        print_statistics(total_file_size, lines_by_status)
