import sys
for line in sys.stdin:
    parts = line.strip().split('\t')
    if len(parts) == 3:
        category, revenue, count = parts
        print('ALL' + '\t' + str(float(revenue)) + '\t' + category + '\t' + count)