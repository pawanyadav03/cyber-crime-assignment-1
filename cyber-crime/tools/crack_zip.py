#!/usr/bin/env python3
"""
crack_zip.py — Dictionary attack against a password-protected ZIP archive.

Simulates the workflow of `zip2john` + `john --wordlist=password.lst` (or
`hashcat -m 17200`) for this coursework exercise. The Debian/Ubuntu 'john'
package does not ship the jumbo-patch helper scripts (including zip2john),
so this script performs the equivalent attack directly using Python's
zipfile module: same wordlist, same "try password, check if it opens"
logic as John the Ripper would use.

Usage:
    python3 crack_zip.py <path_to_protected_zip> [wordlist_path]

If no wordlist is given, it falls back to a small built-in candidate list
that includes common weak/reused passwords (a stand-in for John the
Ripper's default password.lst in this sandboxed environment).
"""

import sys
import time
import zipfile

# Fallback wordlist (subset of common weak passwords, standing in for
# John the Ripper's default password.lst where that file isn't available
# in this environment).
FALLBACK_WORDLIST = [
    "123456", "password", "12345678", "qwerty", "123456789",
    "letmein", "welcome", "monkey", "login", "abc123",
    "starwars", "dragon", "master", "hello", "freedom",
    "whatever", "trustno1", "princess1", "football1", "baseball1",
    "sunshine1", "iloveyou1", "shadow1", "michael1", "superman1",
]


def attempt(password, zf):
    try:
        zf.extractall(pwd=password.encode("latin-1"), path="/tmp/crack_zip_test_out")
        return True
    except Exception:
        return False


def main():
    if len(sys.argv) < 2:
        print("Usage: python3 crack_zip.py <protected.zip> [wordlist.txt]")
        sys.exit(1)

    zip_path = sys.argv[1]
    wordlist_path = sys.argv[2] if len(sys.argv) > 2 else None

    if wordlist_path:
        with open(wordlist_path, "r", encoding="latin-1") as f:
            candidates = [line.rstrip("\n") for line in f]
    else:
        candidates = FALLBACK_WORDLIST

    zf = zipfile.ZipFile(zip_path)
    start = time.time()
    tried = 0

    for pw in candidates:
        tried += 1
        if attempt(pw, zf):
            elapsed = time.time() - start
            print(f"[+] PASSWORD FOUND: '{pw}'")
            print(f"[+] Attempts: {tried}")
            print(f"[+] Time elapsed: {elapsed:.3f}s")
            return

    print(f"[-] Password not found after {tried} attempts.")


if __name__ == "__main__":
    main()
