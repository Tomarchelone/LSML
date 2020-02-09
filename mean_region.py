import sys
import csv
import re


def mapper():
    pattern = re.compile(r"[a-z]+")
    for row in csv.reader(iter(sys.stdin.readline, '')):
        region = row[3]
        content = row[2]
        words = 0
        for match in pattern.finditer(content.lower()):
            words += 1
        print(f"{region}\t{words}")


def reducer():
    region, number = next(sys.stdin).split('\t')
    number = int(number)
    amount = 1
    for line in sys.stdin:
        current_region, current_number = line.split('\t')
        current_number = int(current_number)
        if current_region != region:
            print(f"{region}\t{number/amount:.1f}")
            amount = 1
            region = current_region
            number = current_number
        else:
            number += current_number
            amount += 1
    print(f"{region}\t{number/amount:.1f}")


if __name__ == '__main__':
    mr_command = sys.argv[1]
    {
        'map': mapper,
        'reduce': reducer
    }[mr_command]()
