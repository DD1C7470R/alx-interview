#!/usr/bin/python3
'''script to parse logs'''
import re


def process_log_line(line):
    '''Retrieves the necessary components from a logged file'''
    pattern = (
        r'^(\d+\.\d+\.\d+\.\d+) - \[([^]]+)\] "GET /projects/260 HTTP/1.1" (\d+) (\d+)$'
    )
    matcher = re.compile(pattern)
    is_valid_line = matcher.match(line)

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


if __name__ == "__main__":
    max_lines = 10
    lines = []
    computed_file_size = 0
    for line in iter(input, ''):
        if len(lines) < max_lines + 1:
            lines.append(line.strip())
        if len(lines) == 10:
            computed_metrics = compute_metrics(lines)
            if computed_metrics:
                computed_file_size += computed_metrics['total_file_size']
            lines = []
            lines.append(line.strip())
            print(f'File size: {computed_file_size}')
            for key, value in sorted(computed_metrics['status_codes'].items()):
                print(f'{key} {value}')
