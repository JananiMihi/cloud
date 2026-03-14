#!/usr/bin/env python3
import sys

for line in sys.stdin:
    line = line.strip()
    if not line or line.startswith('Transaction_ID'):
        continue
    fields = line.split(',')
    try:
        segment      = fields[6].strip()   # Platinum, Basic, Silver
        amount_spent = float(fields[10].strip())
        if segment and amount_spent >= 0:
            print(f'{segment}\t{amount_spent:.2f}')
    except (IndexError, ValueError):
        pass
