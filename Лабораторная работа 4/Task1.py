import json
from functools import reduce

def task() -> float:
    with open('input.json', 'r') as f:
        data = json.load(f)
        total_sum = reduce(lambda acc, item: acc + item["score"] * item["weight"], data, 0)
        return round(total_sum, 3)


print(task())
