import sys, heapq
TOP_N = 5
heap = []
for line in sys.stdin:
    parts = line.strip().split('\t')
    if len(parts) == 4:
        _, revenue, category, count = parts
        heapq.heappush(heap, (float(revenue), category, count))
for rev, cat, cnt in sorted(heap, reverse=True)[:TOP_N]:
    print('RANK' + '\t' + cat + '\t' + str(round(rev, 2)) + '\t' + cnt)