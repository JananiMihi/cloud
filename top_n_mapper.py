import sys
# Loop through each line
for line in sys.stdin:
    parts = line.strip().split('\t')

    # Check if the line has exactly 3 values
    if len(parts) == 3:
        category, revenue, count = parts
        print('ALL' + '\t' + str(float(revenue)) + '\t' + category + '\t' + count)   # 'ALL' is used as a global key
