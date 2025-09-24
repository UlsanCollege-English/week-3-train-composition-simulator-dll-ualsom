class _Car:
    __slots__ = ("id", "prev", "next")
    def __init__(self, id):
        self.id = id
        self.prev = None
        self.next = None

class Train:
    def __init__(self):
        self.head = None
        self.tail = None

    def attach_front(self, car_id):
        """Attach a new car at the front (head) of the train."""
        new_car = _Car(car_id)
        if self.head is None:
            self.head = self.tail = new_car
        else:
            new_car.next = self.head
            self.head.prev = new_car
            self.head = new_car

    def attach_back(self, car_id):
        """Attach a new car at the back (tail) of the train."""
        new_car = _Car(car_id)
        if self.tail is None:
            self.head = self.tail = new_car
        else:
            new_car.prev = self.tail
            self.tail.next = new_car
            self.tail = new_car

    def detach_front(self):
        """Detach the car at the front. Return its id or None if empty."""
        if self.head is None:
            return None
        removed_id = self.head.id
        if self.head == self.tail:
            # Only one car
            self.head = self.tail = None
        else:
            self.head = self.head.next
            self.head.prev = None
        return removed_id

    def detach_back(self):
        """Detach the car at the back. Return its id or None if empty."""
        if self.tail is None:
            return None
        removed_id = self.tail.id
        if self.head == self.tail:
            # Only one car
            self.head = self.tail = None
        else:
            self.tail = self.tail.prev
            self.tail.next = None
        return removed_id

    def detach(self, car_id):
        """
        Detach the first occurrence of car with car_id.
        Return True if detached, False if not found.
        """
        current = self.head
        while current:
            if current.id == car_id:
                # Remove current car from list
                if current.prev:
                    current.prev.next = current.next
                else:
                    # current is head
                    self.head = current.next
                if current.next:
                    current.next.prev = current.prev
                else:
                    # current is tail
                    self.tail = current.prev
                return True
            current = current.next
        return False

    def to_list(self):
        """Return list of car ids from front to back."""
        cars = []
        current = self.head
        while current:
            cars.append(current.id)
            current = current.next
        return cars
