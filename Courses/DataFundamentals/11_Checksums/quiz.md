# Checksums - Quiz

Test your knowledge on "Hashes and Checksums".

---

## Question 1: Hash Function

What does a hash function do?

A) Compresses data

B) Creates a backup

C) Transforms data of arbitrary size into a fixed-length string

D) Encrypts data

---

## Question 2: MD5 Length

What is the length of an MD5 hash?

A) 128 characters

B) 64 characters

C) 32 characters

D) 40 characters

---

## Question 3: SHA-256 Length

What is the length of a SHA-256 hash?

A) 40 characters

B) 32 characters

C) 128 characters

D) 64 characters

---

## Question 4: MD5 Security

Why is MD5 not recommended for security?

A) Collisions found (algorithm compromised)

B) Not supported by modern systems

C) Hash is too long

D) Too slow

---

## Question 5: sha256sum

What command computes SHA-256 in Linux?

A) `hashsum -256 file.txt`

B) sha256sum file.txt

C) `shasum file.txt`

D) `sha256 file.txt`

---

## Question 6: Hash Verification

What sha256sum flag verifies a file with hashes?

A) `-x`

B) `-t`

C) -c

D) `-v`

---

## Question 7: Irreversibility

Can you recover original data from a hash?

A) Yes, always

B) No, hash is irreversible

C) Only with a key

D) Only for short data

---

## Question 8: Avalanche Effect

What is the avalanche effect in hash functions?

A) Hash increases with input size

B) Hash can be split into parts

C) Hash is computed in cascade

D) Small input change causes large hash change

---

## Question 9: Collision

What is a hash collision?

A) Computation error

B) Two different inputs produce the same hash

C) Hash is too long

D) Impossible to compute hash

---

## Question 10: Python hashlib

How do you compute SHA-256 of a string in Python?

A) hashlib.sha256("text".encode()).hexdigest()

B) `hash("text", "sha256")`

C) `sha256("text")`

D) `hashlib.sha256("text").hexdigest()`

---

## Question 11: File Hash

Why are files read in chunks when hashing?

A) Algorithm requirement

B) For security

C) To avoid loading entire file into memory

D) For speed

---

## Question 12: SHA-1 in Git

What algorithm does Git use for commit identification?

A) BLAKE2

B) SHA-256

C) MD5

D) SHA-1

---

## Question 13: Passwords

What algorithm is recommended for password storage?

A) MD5

B) SHA-256

C) bcrypt or argon2

D) CRC32

---

## Question 14: macOS shasum

How do you compute SHA-256 on macOS?

A) `md5 -sha256 file`

B) `hash256 file`

C) `sha256sum file`

D) shasum -a 256 file

---

## Question 15: echo -n

Why is the `-n` flag important in `echo -n "text" | sha256sum`?

A) For numeric format output

B) For binary output

C) For compatibility

D) To avoid adding newline to input

---

## Question 16: SHA-512 Length

What is the length of SHA-512 hash in hex characters?

A) 512 characters

B) 128 characters

C) 256 characters

D) 64 characters

---

## Question 17: BLAKE3

What advantage does BLAKE3 have over SHA-256?

A) Built into all systems

B) Doesn't require libraries

C) Very fast while cryptographically strong

D) Shorter hash

---

## Question 18: Deduplication

How can hashes be used to find duplicate files?

A) Rename files

B) Delete all files

C) Compress files and compare sizes

D) Compare hashes of all files, identical = duplicates

---

## Question 19: Hash vs Encryption

What distinguishes hash from encryption?

A) Hash is faster

B) Hash is irreversible and doesn't require a key

C) Hash creates larger output

D) Hash only works with text

---

## Question 20: hashlib.new

How do you create a hash object for an arbitrary algorithm in Python?

A) hashlib.hash('sha512')

B) hashlib.get('sha512')

C) hashlib.create('sha512')

D) hashlib.new('sha512')

---

---

## Answer Key

| # | Answer | Explanation |
|---|--------|-------------|
| 1 | C | Hash transforms input of any size into fixed-length string (fingerprint). |
| 2 | A | MD5 = 128 bits = 32 hex characters. |
| 3 | D | SHA-256 = 256 bits = 64 hex characters. |
| 4 | A | Practical collisions found for MD5, cryptographically insecure. |
| 5 | A | `sha256sum` — standard command in Linux. |
| 6 | C | `-c` (check) verifies files against hash list. |
| 7 | D | Hash — one-way function, cannot recover input. |
| 8 | C | Changing one bit of input changes ~50% of hash bits. |
| 9 | B | Collision — when different inputs produce same hash. |
| 10 | D | Need `.encode()` to convert str to bytes. |
| 11 | D | Chunk reading allows hashing files larger than RAM. |
| 12 | B | Git uses SHA-1 (migration to SHA-256 planned). |
| 13 | C | bcrypt/argon2 specifically designed for passwords (slow, with salt). |
| 14 | D | On macOS, use `shasum -a 256`. |
| 15 | C | Without `-n`, echo adds `\n`, changing the hash. |
| 16 | A | SHA-512 = 512 bits = 128 hex characters. |
| 17 | C | BLAKE3 very fast while cryptographically strong. |
| 18 | D | Identical hash = identical file contents. |
| 19 | C | Hash irreversible and no key; encryption reversible with key. |
| 20 | D | `hashlib.new('algorithm')` creates object for any algorithm. |

---

## Scoring Guide

| Result | Rating | Recommendations |
|--------|--------|----------------|
| **17-20 correct (85-100%)** | 🏆 Excellent! | You master hashing! |
| **14-16 correct (70-84%)** | ✅ Good | Review hash security. |
| **10-13 correct (50-69%)** | ⚠️ Satisfactory | Re-read hash applications. |
| **Less than 10 correct (<50%)** | 📚 Needs Review | Recommended to re-read the lecture. |

---
