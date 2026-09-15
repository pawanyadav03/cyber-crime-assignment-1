# Operation Phantom Swipe
## Part 2 — Electronic Evidence Collection Simulation

---

## 2.1 Devices Seized

| Exhibit | Description | Seizure Location |
|---|---|---|
| **A** | ATM skimmer unit — card-slot overlay + pinhole camera + Bluetooth data module + onboard flash | ATM lobby, Branch 1, South Delhi |
| **B** | Suspect's Android phone — fraud app, SMS logs, chat logs, GPS cache, password-protected archive | Suspect's residence, South Delhi |

Simulated data sets for each exhibit are provided in
`evidence/exhibit-A-skimmer/` and `evidence/exhibit-B-phone/`.

---

## 2.2 Evidence Handling Procedure

**1. Isolation at point of seizure**
- Exhibit A was powered down immediately and placed into a static-shielded
  evidence bag to prevent tampering or a panic-wipe routine from triggering.
- Exhibit B was placed into airplane mode, then a Faraday bag, to cut it off
  from any remote wipe, remote lock, or cloud-sync command before
  acquisition.

**2. Write-blocking**
- Exhibit A's onboard flash was connected only through a hardware
  write-blocker for imaging — the acquisition process is physically
  incapable of writing back to the source medium.
- Exhibit B was extracted using a verified read-only interface mode,
  consistent with standard mobile-forensics practice.

**3. Imaging / extraction**
- Exhibit A: onboard flash dumped to `skimmer_raw_dump.bin`; parsed capture
  records exported to `captured_tracks.csv`; configuration/pairing metadata
  to `device_config.txt`; photographic log to `photo_log.txt`.
- Exhibit B: app manifest/permissions to `fraud_app_manifest.txt`; SMS cache
  to `harvested_sms_log.json`; messaging export to `courier_chat_log.txt`;
  location cache to `gps_coordinates.csv`; gallery metadata to
  `gallery_log.txt`; a locked archive recovered as `protected_evidence.zip`.

**4. Hashing (integrity verification)**
- A SHA-256 hash was generated for every extracted file immediately after
  acquisition (see §2.4) and recorded on the chain-of-custody form at that
  point.
- Hashes are re-verified at every later access (transfer to analyst, copy to
  workstation, before report writing); a mismatch at any stage would mean
  the copy can no longer be treated as forensically sound and must be
  re-acquired.
- Only working copies are analysed; the original media/first image is never
  opened directly, preserving an unaltered master copy for court production.

**5. Documentation**
- Every seizure, transfer, and access event is logged on the chain-of-custody
  form below, signed and timestamped, with no gap in custody permitted.

---

## 2.3 Chain of Custody Form

**Case No.:** OPS-2026-014 — Operation Phantom Swipe
**Investigating Unit:** Cyber Crime Cell (simulated)

### Exhibit A

| Field | Detail |
|---|---|
| Exhibit ID | OPS-2026-014-A |
| Description | ATM skimmer unit (overlay, camera, Bluetooth module, flash storage) |
| Date/Time of Seizure | 18-Mar-2026, 18:40 IST |
| Location of Seizure | ATM lobby, Branch 1, South Delhi |
| Seized By | Investigating Officer (IO-1) |
| Witnesses (Panchas) | Panch Witness 1, Panch Witness 2 |
| Sealed/Bagged | Yes — tamper-evident bag, seal no. TE-30412 |
| Initial Hash (SHA-256, `skimmer_raw_dump.bin`) | `9e6f2808eafef43017fc2d981ed8d8986ca4fbea25a169a890c8965c3eec7a0a` |

| Date/Time | Released By | Received By | Purpose | Signature |
|---|---|---|---|---|
| 18-Mar-2026 18:40 | Scene (Panch witnesses) | IO-1 | Seizure | signed |
| 19-Mar-2026 09:20 | IO-1 | Forensic Lab Custodian | Transport for imaging | signed |
| 19-Mar-2026 10:05 | Lab Custodian | Forensic Analyst-1 | Write-blocked imaging & hashing | signed |
| 19-Mar-2026 14:10 | Forensic Analyst-1 | Evidence Locker | Return to secure storage | signed |

### Exhibit B

| Field | Detail |
|---|---|
| Exhibit ID | OPS-2026-014-B |
| Description | Android phone (fraud app, SMS/chat/GPS data, locked archive) |
| Date/Time of Seizure | 18-Mar-2026, 19:05 IST |
| Location of Seizure | Suspect's residence, South Delhi |
| Seized By | Investigating Officer (IO-1) |
| Witnesses (Panchas) | Panch Witness 1, Panch Witness 2 |
| Sealed/Bagged | Yes — Faraday bag, seal no. TE-30413 |
| Initial Hash (SHA-256, `harvested_sms_log.json`) | `87ac1b39e5f80a4cd3097ee7f771dec0210c3a37e25e6c8bebb85fe270b0fc41` |

| Date/Time | Released By | Received By | Purpose | Signature |
|---|---|---|---|---|
| 18-Mar-2026 19:05 | Scene (Panch witnesses) | IO-1 | Seizure | signed |
| 19-Mar-2026 09:20 | IO-1 | Forensic Lab Custodian | Transport for extraction | signed |
| 19-Mar-2026 10:40 | Lab Custodian | Forensic Analyst-2 | Mobile extraction & hashing | signed |
| 19-Mar-2026 15:20 | Forensic Analyst-2 | Evidence Locker | Return to secure storage | signed |

---

## 2.4 SHA-256 Hash Values of Acquired Files

Full log: `evidence/hashes/sha256_hashlog.txt`. **16 files hashed in
total** — well above the minimum of 5 required for this exercise.

| File | Exhibit | SHA-256 |
|---|---|---|
| `captured_tracks.csv` | A | `4018b7c53934c2e99beb63c0c58f635a274c58f466dcae26036ef581a084df11` |
| `device_config.txt` | A | `50f443746f318a7a10c218fba0425b89dd500c41e173e9c89f3fd125f4ce6dc8` |
| `photo_log.txt` | A | `181722626b7d510af886286c44cac7ce4635be32cb5f5206702d0fccf17e3865` |
| `skimmer_raw_dump.bin` | A | `9e6f2808eafef43017fc2d981ed8d8986ca4fbea25a169a890c8965c3eec7a0a` |
| `photos/IMG_A001.jpg` … `IMG_A006.jpg` (4 files) | A | see hash log |
| `courier_chat_log.txt` | B | `f73b1c72320255b20a293aa7157af26a2d47209f049d0f0355839b8af093c70f` |
| `fraud_app_manifest.txt` | B | `0ae33ff78830b778084315f2e10a8b80b7a980f0019da07ec8dbd9568600ca6a` |
| `gallery_log.txt` | B | `d4c705ae221330fc294301b99981f6012489a236a9f2a91b769eb00c93a9be40` |
| `gps_coordinates.csv` | B | `e530822bc33dd141c74b1829e8dd6677ca248bba4ddd3911755e725cf82a161d` |
| `harvested_sms_log.json` | B | `87ac1b39e5f80a4cd3097ee7f771dec0210c3a37e25e6c8bebb85fe270b0fc41` |
| `protected_evidence.zip` (still locked) | B | `a71ca53d28f86d7fc6fce65d83e1b8680d00cd484af02273e68b6d4240c31d5e` |
| `gallery/IMG_2026-03-12_1.jpg`, `IMG_2026-03-15_1.jpg` | B | see hash log |

The password-protected archive is hashed **before** any crack attempt (see
Part 4, §4.1), so its pre-crack state is provably preserved regardless of
what the password-recovery process later reveals.

> **Note on data authenticity:** all card numbers, phone numbers, names,
> coordinates, chat content, and image content in the evidence files are
> **synthetically generated for this simulation** and do not correspond to
> real individuals, accounts, or devices. Evidence photos are placeholder
> graphics explicitly labelled "EVIDENCE PHOTO — SIMULATED".

---

*Next: Part 3 — Electronic Media Search and Analysis (artefact extraction,
search strategy, evidence log).*
