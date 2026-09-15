# Operation Phantom Swipe
## Part 4 — Cryptography Component

---

## 4.1 The Password-Protected Archive

During extraction of Exhibit B, one file was found to be password-protected:

- **File:** `evidence/exhibit-B-phone/protected_evidence.zip`
- **SHA-256 (of the still-locked archive, taken before any crack attempt):**
  `a71ca53d28f86d7fc6fce65d83e1b8680d00cd484af02273e68b6d4240c31d5e`
- **Contents once opened:** `laundering_notes.txt` (dummy mule-account list
  and proceeds split ratio) and `target_bank_list.txt` (dummy list of
  target branches) — both synthetic, for this simulation.

The locked archive is hashed *before* any recovery attempt so that its
pre-crack state is provable independently of what the password-recovery
process later reveals.

---

## 4.2 Cracking Approach

**Intended tool-chain (typical lab setup):** `zip2john` to extract a
crackable representation of the archive, then `john --wordlist=password.lst
hash.txt` (or `hashcat -m 17200` for legacy ZipCrypto). This is the
command-line workflow the assignment brief references.

**What was actually run in this environment:** the Debian/Ubuntu `john`
package does not ship the jumbo-patch helper scripts (including
`zip2john`), so a Python script (`tools/crack_zip.py`) was written that
performs the equivalent attack directly — iterating a candidate wordlist
and attempting `zipfile.extractall(pwd=...)` for each entry. This is
functionally identical to what `zip2john` + `john` would do: same
"try password, check if it opens" logic, just implemented directly.

```
$ python3 tools/crack_zip.py evidence/exhibit-B-phone/protected_evidence.zip
[+] PASSWORD FOUND: 'sunshine1'
[+] Attempts: 21
[+] Time elapsed: 0.002s
```

The password `sunshine1` was recovered in 21 attempts, in a couple of
milliseconds. This is a **dictionary attack**, not a brute-force attack: it
succeeded because the suspect reused a common, easily guessable password
rather than because of raw compute power.

*(A true exhaustive brute-force run — trying every possible character
combination up to the password's length — was not additionally executed,
since the dictionary attack already succeeded; in practice, brute-force is
typically only escalated to after a wordlist pass fails, since it is far
more time- and compute-intensive.)*

---

## 4.3 Ethical Implications: Brute-Forcing vs. Lawful Decryption

| | Brute-force / dictionary cracking by investigators | Lawful decryption request (compelled disclosure / vendor assistance) |
|---|---|---|
| **Basis** | Technical — exploits weak/reused passwords | Legal — court order or statutory power (e.g. Sec. 69 IT Act, Sec. 91 CrPC production order) |
| **Reliability** | Not guaranteed — a strong, unique password may resist indefinitely | Compels the party who knows the password to cooperate; more reliable when it succeeds |
| **Rights implications** | Circumvents an access-control measure without the owner's consent, ahead of any court authorisation | Respects due process — the subject typically has notice and a route to challenge the order |
| **Risk of overreach** | Investigators could technically reach material beyond what a warrant specifically authorised | Legal orders can be scoped narrowly to what's actually needed |
| **When justified** | Widely accepted for evidence already lawfully seized under a valid warrant, applied only to that evidence, and documented | Preferred where the subject or a third party can be compelled — avoids self-incrimination disputes |

**Key ethical tension:** compelling a suspect to disclose a password
directly can raise self-incrimination concerns in some legal systems, which
is one reason technical cracking — applied only to already-lawfully-seized
evidence, and fully documented as in §4.2 — is often the preferred route
over compelled disclosure.

---

## 4.4 Reflection: Strength of User-Created Passwords in Criminal Scenarios

This case illustrates a pattern seen repeatedly in real digital-forensics
work: **operational security failures are usually the actual point of
compromise**, not sophisticated cryptanalysis.

- `sunshine1` follows a common weak-password template — a dictionary word
  plus a trailing digit to satisfy a "must contain a number" policy — and
  offers negligible resistance to a wordlist any investigator (or attacker)
  can obtain for free.
- Criminal actors frequently reuse personal-style passwords across
  legitimate accounts and concealment archives, because remembering a
  unique strong password purely to hide evidence competes with everyday
  convenience — the same psychology that makes weak passwords a problem for
  ordinary users makes them an evidentiary opportunity when used by
  criminals.
- From a forensic-readiness standpoint, this means a dictionary attack
  should always be attempted **before** committing resources to a full
  brute-force run — the cost/reward ratio strongly favours trying
  known-weak and reused passwords first.
- This has a direct policy implication for Part 5's recommendations: SOPs
  should mandate an early, low-cost wordlist pass on any protected evidence
  container before requesting more resource-intensive avenues.

---

*Next: Part 5 — Legal-Ethical Report (see `report/` folder for the
consolidated 4–6 page report).*
