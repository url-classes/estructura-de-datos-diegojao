class Node:

    def __init__(self, value: int):
        self.value: int = value
        self.next:  Node | None = None