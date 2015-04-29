import TRNG
rng = TRNG.RNG()
rng.generate()
rng.xor()
rng.hex()
print rng.getSelf()
rng.shuffle()
print rng.getSelf()
