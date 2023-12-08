from Crypto.Hash import keccak

def calculate_keccak256(data):
    keccak_hash = keccak.new(digest_bits=256)
    keccak_hash.update(data.encode('utf-8'))
    return keccak_hash.hexdigest()

# Contoh penggunaan
pesan = "Hi, Keccak256!"
hash_result = calculate_keccak256(pesan)
print(f"Pesan: {pesan}")
print(f"Keccak256 Hash: {hash_result}")
