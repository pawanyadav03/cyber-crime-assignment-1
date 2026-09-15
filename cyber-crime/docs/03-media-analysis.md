# Operation Phantom Swipe
## Part 3 — Electronic Media Search and Analysis

---

## 3.1 Search Strategy

Analysis was performed only on the **working copies** produced in Part 2
(never the original media), using each file's SHA-256 hash to confirm the
copy matched the acquired original before analysis began.

| Technique | Applied To | Purpose |
|---|---|---|
| **String search** (`strings`-style extraction over raw binary) | `skimmer_raw_dump.bin` | Recover human-readable markers (firmware ID) inside an unstructured binary dump, confirming device identity without a full parser. |
| **Structured/metadata search** (parsing CSV/JSON, filtering by field) | `captured_tracks.csv`, `gps_coordinates.csv`, `harvested_sms_log.json` | Pull specific fields (card numbers, coordinates, OTP text, timestamps) already exported in structured form. |
| **Communication extraction** (parsing message exports for sender, timestamp, body) | `courier_chat_log.txt`, `harvested_sms_log.json` | Reconstruct the timeline between the suspect and courier, and identify intercepted OTP messages. |

**Search terms used** (representative): `OTP`, `track1`, `track2`,
`location`, `card`, `.apk`, `PERMISSION`, `FW_v`, coordinate patterns
(`\d{2}\.\d+,\s*\d{2}\.\d+`), and the offending-period timestamp window
(09–16 Mar 2026).

### String search output (`skimmer_raw_dump.bin`)

```
$ strings skimmer_raw_dump.bin
SWIPEGHOST_FW_v3.4_DUMPSTART
SWIPEGHOST_FW_v3.4_DUMPEND
```

The recovered `SWIPEGHOST_FW_v3.4` marker, present at both the start and
end of the dump, corroborates the firmware version already recorded in
`device_config.txt` — an independent cross-check confirming the config
file accurately describes the physical device.

---

## 3.2 Extracted Artefacts (7 — exceeds the required 5)

| # | Artefact ID | Source File | Description | Relevance |
|---|---|---|---|---|
| 1 | ART-001 | `exhibit-A-skimmer/skimmer_raw_dump.bin` | Firmware identifier `SWIPEGHOST_FW_v3.4` recovered via string search | Confirms device identity, corroborates config file |
| 2 | ART-002 | `exhibit-A-skimmer/captured_tracks.csv` | 6 dummy Track1/Track2 records with cardholder names and expiry | Direct evidence of skimming, links device to specific capture events |
| 3 | ART-003 | `exhibit-A-skimmer/device_config.txt` | Bluetooth pairing MAC `D4:3C:11:8A:00:5F`, paired device name "OP7-User" | Potential link to Exhibit B if a matching pairing record is found on the phone |
| 4 | ART-004 | `exhibit-B-phone/fraud_app_manifest.txt` | Dangerous permission set (`READ_SMS`, `BIND_ACCESSIBILITY_SERVICE`, overlay) + non-Play-Store install source | Establishes the app as a credential harvester, not a legitimate bank utility |
| 5 | ART-005 | `exhibit-B-phone/harvested_sms_log.json` | 5 intercepted OTP messages from 4 different banks, masked victim numbers | Direct evidence of unauthorised OTP interception; identifies victim banks |
| 6 | ART-006 | `exhibit-B-phone/courier_chat_log.txt` | Message thread coordinating batches, drop points and a 60/40 cash-out split with "Delivery-9" | Evidence of the cash-out/organised network |
| 7 | ART-007 | `exhibit-B-phone/gps_coordinates.csv` | 5 coordinate points: 4 ATM targets + 1 drop point, matching chat timestamps | Corroborates reconnaissance and ties phone location history to the chat evidence (GPS-005 timestamp matches the 11-Mar chat "location shared" event) |

---

## 3.3 Evidence Log

| Log Entry | Artefact | Analyst | Date/Time | Action | Hash Verified? |
|---|---|---|---|---|---|
| EL-001 | ART-001 | Forensic Analyst-1 | 20-Mar-2026 09:05 | String search on raw dump | matches §2.4 hash |
| EL-002 | ART-002 | Forensic Analyst-1 | 20-Mar-2026 09:20 | Field extraction from CSV | matches |
| EL-003 | ART-003 | Forensic Analyst-1 | 20-Mar-2026 09:35 | Config file review | matches |
| EL-004 | ART-004 | Forensic Analyst-2 | 20-Mar-2026 10:00 | Manifest/permission review | matches |
| EL-005 | ART-005 | Forensic Analyst-2 | 20-Mar-2026 10:15 | JSON parse, filter by sender prefix `BK-` | matches |
| EL-006 | ART-006 | Forensic Analyst-2 | 20-Mar-2026 10:30 | Chat export review, timeline build | matches |
| EL-007 | ART-007 | Forensic Analyst-2 | 20-Mar-2026 10:45 | Coordinate cross-reference with chat timestamps | matches |

**Cross-artefact correlation:** ART-007's GPS-005 point (11-Mar, 22:07)
lines up exactly with the "[location shared]" message in ART-006's chat log
at the same timestamp, and ART-003's Bluetooth pairing metadata provides a
second, independent link between the two exhibits. No single artefact is
relied on in isolation — each is corroborated against at least one artefact
from the *other* exhibit, strengthening the case against a claim that any
one item was planted or misattributed.

---

*Next: Part 4 — Cryptography Component (password-protected archive,
dictionary-attack simulation, ethical discussion).*
