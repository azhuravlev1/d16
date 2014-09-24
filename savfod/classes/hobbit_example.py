class Ring:
    magic_power = 10
    owner = None
    label = "Made in Mordor"
    def make_stronger(self, diff):
        self.magic_power += diff

class Hobbit:
    ring = None
    def set_ring(self, ring):
        if ring.owner:
            ring.owner.ring = None
        self.ring = ring
        ring.owner = self

ring = Ring()

bilbo = Hobbit()
bilbo.set_ring(ring)
frodo = Hobbit()
frodo.set_ring(ring)
print("Frodo's ring:", frodo.ring)
print("Bilbo's ring:", bilbo.ring)
