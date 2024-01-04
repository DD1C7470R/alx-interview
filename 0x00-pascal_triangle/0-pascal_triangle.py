#!/usr/bin/python3
'''implements the pascal triangle
'''


def pascal_triangle(n):
    triangle = []
    if n <= 0:
        return []
    else:
        old_results = [1, 1]
        for i in range(0, n):
            if i == 0:
                results = [1]
            else:
                results = [1]
                counter = 0
                for num in old_results:
                    if len(old_results) == 2 and len(results) == 2 and i > 1:
                        results.append(1)
                    elif i > 1 and counter != len(old_results) - 1:
                        results.append(num + old_results[counter + 1])
                    else:
                        if len(results) == 2 and i == 1:
                            pass
                        else:
                            results.append(1)

                    counter += 1
                old_results = results
            triangle.append(results)
    return triangle
