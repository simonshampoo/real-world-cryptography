common = 100

alice_priv_key: int = 10

bob_priv_key: int = 5

alice_pub_key: str = hex(alice_priv_key + common)  # 115 = 0x73
bob_pub_key: str = hex(bob_priv_key + common)  # 105 = 0x69


def get_shared(priv: int, pub: int) -> str:
    return hex(priv + pub)


assert get_shared(alice_priv_key, int(bob_pub_key, 16)) == get_shared(
    bob_priv_key, int(alice_pub_key, 16)
)
