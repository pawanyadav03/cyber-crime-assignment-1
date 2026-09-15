# Operation Phantom Swipe
## Part 1 — Cybercrime Classification & Modelling

---

## 1.1 Case Scenario (Working Narrative)

> This narrative is a constructed fictional scenario, created to give the
> rest of the assignment (evidence simulation, artefact analysis,
> cryptography, legal report) a single consistent case to work from.

**Case ID:** OPS-2026-014 "Operation Phantom Swipe"
**Jurisdiction:** Primary — South Delhi, India. Secondary — a neighbouring
country (physical cash-out) and an unconfirmed overseas exchange (partial
crypto conversion).

Between March and mid-March 2026, a cluster of complaints from customers of
four different banks reported unauthorised ATM withdrawals and OTP-linked
online transactions. Tracing the pattern led investigators to a two-person
cell operating out of South Delhi, working across four stages:

1. **Skimming stage** — A covert card-slot overlay and pinhole camera were
   fitted to ATMs at four branches, capturing magnetic-stripe track data and
   PINs. Captured data was periodically offloaded via Bluetooth to a paired
   Android phone.
2. **App stage** — The same phone ran a sideloaded application disguised as
   a bank rewards utility ("SecureBank Rewards+"), which requested SMS-read
   and accessibility permissions and was used to intercept OTPs from a
   second, separate group of victims.
3. **Cloning & cash-out stage** — Captured track data was encoded onto blank
   cards and handed to a courier ("Delivery-9") for domestic use and
   cross-border cash-out.
4. **Laundering stage** — Proceeds were routed through mule accounts opened
   with forged KYC documents, with part of the funds converted to
   cryptocurrency.

Two devices were seized during a raid on the suspects' residence:

- **Exhibit A** — ATM skimmer unit (card-slot overlay, pinhole camera,
  Bluetooth data module, onboard flash storage).
- **Exhibit B** — Suspect's Android phone (fraud app, SMS/chat logs, GPS
  cache, image gallery, a password-protected archive).

---

## 1.2 Identification & Classification of Crimes

| # | Observed Act | Crime Category | Description |
|---|---|---|---|
| 1 | Covert skimmer fitted to ATM card slot | **ATM Skimming (Data Interception)** | Unauthorised interception of card track data and PIN at the point of capture. |
| 2 | Track data encoded onto blank cards | **Credit/Debit Card Cloning (Forgery)** | Creation of a counterfeit payment instrument from stolen data. |
| 3 | Sideloaded fake rewards app harvesting OTPs | **Phishing / Smishing + Unauthorised Access** | Deceptive delivery of a malicious app to obtain unauthorised access to victims' financial credentials. |
| 4 | Cloned cards used for withdrawals/purchases | **Identity Theft & Financial Fraud** | Fraudulent use of another person's financial identity for gain. |
| 5 | Cross-border courier cash-out network | **Organised/Transnational Cybercrime** | Coordinated cross-jurisdiction offending, raising mutual-legal-assistance questions. |
| 6 | Mule accounts on forged KYC, partial crypto conversion | **Money Laundering** | Layering and integration of criminal proceeds through banking and crypto channels. |

---

## 1.3 Mapping to Legal Frameworks

### A. Information Technology Act, 2000 (India, as amended 2008)

| Section | Provision | Applicability to this case |
|---|---|---|
| **Sec. 43** | Penalty for unauthorised access/extraction of data from a computer system | Covers the skimmer's unauthorised capture of track data and the app's unauthorised SMS/OTP reads. |
| **Sec. 43A** | Compensation for a body corporate's failure to protect sensitive personal data | Relevant if bank/ATM-operator security lapses contributed to the exposure. |
| **Sec. 66** | Computer-related offences where Sec. 43 acts are done dishonestly/fraudulently | Applies once the data-capture conduct is shown to be fraudulent. |
| **Sec. 66C** | Identity theft — fraudulent use of another's password/unique identification feature | Covers use of stolen card numbers, PINs and OTPs to impersonate cardholders. |
| **Sec. 66D** | Cheating by personation using a computer resource | Covers the fake rewards app posing as a legitimate bank service. |
| **Sec. 72** | Breach of confidentiality/privacy by a person who obtained access to data under the Act | Applicable to onward disclosure of harvested card data to the cash-out network. |

### B. Indian Penal Code, 1860

| Section | Provision | Applicability |
|---|---|---|
| **Sec. 379** | Theft | Underlying theft of cardholder funds. |
| **Sec. 420** | Cheating and dishonestly inducing delivery of property | Fraudulent withdrawals/purchases obtained by deception. |
| **Sec. 465 / 468** | Forgery / forgery for the purpose of cheating | Cloned cards and forged KYC documents used to open mule accounts. |
| **Sec. 471** | Using a forged document as genuine | Presenting cloned cards at ATMs/POS terminals. |
| **Sec. 120B** | Criminal conspiracy | Coordinated scheme across skimming, encoding, courier and mule-account roles. |
| **Sec. 34** | Acts by several persons in furtherance of common intention | Joint liability of the two-person cell and courier. |

*(The Prevention of Money Laundering Act, 2002 would also apply to the
mule-account/crypto stage; flagged here for completeness, though outside
the assignment's named frameworks.)*

### C. Budapest Convention on Cybercrime (2001)

| Article | Provision | Applicability |
|---|---|---|
| **Art. 2** | Illegal access | Unauthorised access to card data via skimmer/app. |
| **Art. 3** | Illegal interception | Interception of track data / OTP-SMS in transit. |
| **Art. 7** | Computer-related forgery | Creation of cloned cards from captured data. |
| **Art. 8** | Computer-related fraud | Fraudulent withdrawal/purchase causing loss to victims. |
| **Art. 25 / 27** | International cooperation, mutual legal assistance | Governs the cross-border request process for pursuing the cash-out network. |

> **Caveat:** India has not signed or ratified the Budapest Convention. The
> mapping above is used as a **comparative/analytical framework** —
> demonstrating that India's domestic law substantively covers the same
> conduct — rather than as an enforceable treaty basis for this
> investigation. Cross-border cooperation would instead rely on bilateral
> Mutual Legal Assistance Treaties (MLATs) or informal channels.

---

## 1.4 Cybercrime Taxonomy (with Justification)

```
Operation Phantom Swipe – Crime Taxonomy
│
├── 1. Data-Capture Offences
│   ├── ATM Skimming (physical device)         → IT Act 43/66, Budapest Art. 3
│   └── Credential Phishing via malicious app   → IT Act 43/66D, Budapest Art. 2
│
├── 2. Instrument-Forgery Offences
│   └── Magnetic-stripe card cloning            → IPC 465/468/471, Budapest Art. 7
│
├── 3. Financial-Fraud Offences
│   ├── Fraudulent ATM cash withdrawal          → IPC 379/420, IT Act 66C, Budapest Art. 8
│   └── OTP-enabled online fraud                → IPC 420, IT Act 66C/66D, Budapest Art. 8
│
├── 4. Identity-Related Offences
│   └── Identity theft (use of stolen PII)      → IT Act 66C
│
├── 5. Organised/Transnational Offences
│   └── Cross-border cash-out courier network   → IPC 120B/34, Budapest Art. 25 (analytical only – India non-party)
│
└── 6. Proceeds-of-Crime Offences
    └── Money laundering via mule accounts/crypto → PMLA 2002 (supplementary), IPC 468 (forged KYC)
```

**Justification for structure:** the taxonomy follows the *stage of the
crime lifecycle* (capture → forge → defraud → conceal identity → organise →
launder) rather than grouping by device or actor. This mirrors how the
investigation actually proceeded: each stage produced a distinct evidence
type (skimmer firmware/storage, app manifest, encoder-adjacent card data,
transaction/chat/GPS metadata, mule-account records) that maps to a
specific legal provision, and this structure is carried forward into Parts
2 and 3, where each evidence item is tagged back to the category it
supports.

---

*Next: Part 2 — Electronic Evidence Collection Simulation (chain of
custody, disk image/file set generation, SHA-256 hashing).*
