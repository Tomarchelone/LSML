import sys
import csv
import re
from collections import Counter

def mapper():
    pattern = re.compile(r"[a-z]+")
    for row in csv.reader(iter(sys.stdin.readline, '')):
        region = row[3]
        content = row[2]
        for match in pattern.finditer(content.lower()):
            word = match.group(0)
            if len(word) > 2:
                print(f"{region}+{word}")


def reducer():
    cnt = Counter()
    region, word = next(sys.stdin).split('+')
    word = word.strip()
    region = region.strip()
    cnt[word] += 1
    for line in sys.stdin:
        current_region, current_word = line.split('+')
        current_word = current_word.strip()
        current_region = current_region.strip()
        if current_region != region:
            print(region)
            for w, c in cnt.most_common(10):
                print(f"    {w} {c}")
            cnt = Counter()
            region = current_region
            cnt[current_word] += 1
        else:
            cnt[current_word] += 1
    print(region)
    for w, c in cnt.most_common(10):
        print(f"    {w} {c}")


if __name__ == '__main__':
    mr_command = sys.argv[1]
    {
        'map': mapper,
        'reduce': reducer
    }[mr_command]()
