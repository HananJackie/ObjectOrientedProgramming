def hanoi_recursive(n, source="A", target="C", aux="B"):
    if n == 0:
        return
    hanoi_recursive(n - 1, source, aux, target)
    print(f"Move disk {n} from {source} to {target}")
    hanoi_recursive(n - 1, aux, target, source)


def hanoi_iterative(n, source="A", target="C", aux="B"):
    # Peg stacks tracking disk sizes (largest at bottom)
    pegs = {source: list(range(n, 0, -1)), target: [], aux: []}
    total_moves = (1 << n) - 1  # 2^n - 1 moves

    # If n is even, swap move priorities between target and auxiliary
    p1, p2, p3 = source, target, aux
    if n % 2 == 0:
        p2, p3 = aux, target

    def move_between(peg1, peg2):
        if not pegs[peg1]:
            disk = pegs[peg2].pop()
            pegs[peg1].append(disk)
            print(f"Move disk {disk} from {peg2} to {peg1}")
        elif not pegs[peg2]:
            disk = pegs[peg1].pop()
            pegs[peg2].append(disk)
            print(f"Move disk {disk} from {peg1} to {peg2}")
        elif pegs[peg1][-1] < pegs[peg2][-1]:
            disk = pegs[peg1].pop()
            pegs[peg2].append(disk)
            print(f"Move disk {disk} from {peg1} to {peg2}")
        else:
            disk = pegs[peg2].pop()
            pegs[peg1].append(disk)
            print(f"Move disk {disk} from {peg2} to {peg1}")

    # Make legal moves cyclically
    for i in range(1, total_moves + 1):
        if i % 3 == 1:
            move_between(p1, p2)
        elif i % 3 == 2:
            move_between(p1, p3)
        else:
            move_between(p2, p3)


# Example: solve for 3 disks
hanoi_recursive(3)
hanoi_iterative(3)
