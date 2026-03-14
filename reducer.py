#!/usr/bin/env python3
import sys

current_segment = None
total_revenue = 0.0
order_count = 0

for line in sys.stdin:
    line = line.strip()
    if not line:
        continue
    parts = line.split('\t')
    if len(parts) != 2:
        continue
    segment = parts[0]
    try:
        amount = float(parts[1])
    except ValueError:
        continue

    if segment == current_segment:
        total_revenue += amount
        order_count += 1
    else:
        if current_segment is not None:
            print(current_segment + '\t' + str(round(total_revenue, 2)) + '\t' + str(order_count))
        current_segment = segment
        total_revenue = amount
        order_count = 1

if current_segment is not None:
    print(current_segment + '\t' + str(round(total_revenue, 2)) + '\t' + str(order_count))