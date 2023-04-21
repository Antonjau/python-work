class Jar:
    def __init__(self, capacity=12):
        if not isinstance(capacity, int) or capacity < 0:
            raise ValueError("Capacity must be a non-negative integer.")
        self.capacity = capacity
        self.cookies = 0

    def __str__(self):
        return "🍪" * self.cookies

    def deposit(self, n):
        if not isinstance(n, int) or n < 0:
            raise ValueError("Number of cookies to deposit must be a non-negative integer.")
        if self.cookies + n > self.capacity:
            raise ValueError("Jar capacity exceeded.")
        self.cookies += n

    def withdraw(self, n):
        if not isinstance(n, int) or n < 0:
            raise ValueError("Number of cookies to withdraw must be a non-negative integer.")
        if self.cookies < n:
            raise ValueError("Not enough cookies in the jar.")
        self.cookies -= n

    @property
    def size(self):
        return self.cookies

