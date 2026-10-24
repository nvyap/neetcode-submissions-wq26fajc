from typing import List, Tuple


def best_student(scores: List[Tuple[str, int]]) -> str:
    best = ""
    max_score = 0
    for i in scores:
        name,score = i[0],i[1]
        if score>max_score:
            best = name
            max_score = score
    return best


# do not modify below this line
print(best_student([("Alice", 90), ("Bob", 80), ("Charlie", 70)]))
print(best_student([("Alice", 90), ("Bob", 80), ("Charlie", 100)]))
print(best_student([("Alice", 90), ("Bob", 100), ("Charlie", 70)]))
print(best_student([("Alice", 90), ("Bob", 90), ("Charlie", 80), ("David", 100)]))
