# IA 642 Week 05 Lab 5.2 — Live Triage on MERIDIAN-APP01

Eastern Michigan University · Defensive Security · Fall 2026  
**Authors:** Unais Ali (E02805019), Hafiz Usama (E02574092)

**Public repo:** https://github.com/unaisshazan/ia642-week05-lab52-dfir

> **Week 05 presentation order:** [Lab 5.1 CTI](https://github.com/unaisshazan/ia642-week05-lab51-cti) → **this Lab 5.2 DFIR** → [Bonus STIX/TAXII data](https://github.com/unaisshazan/ia642-week05-lab51-cti/tree/master/Lab5_Bonus_Assignment)  
> Full talk track: https://github.com/unaisshazan/ia642-week05-lab51-cti#readme

---

## What this lab is

Lab 5.2 builds **MERIDIAN-APP01** (Windows Server 2022), stages a LOLBin-style `certutil` trail and an HKCU Run-key persistence entry, acquires live memory with WinPmem, triages with Volatility 3, parses Prefetch/Amcache, and classifies the inert `svcupdate.bin` stand-in.

### How it connects to 5.1 and the Bonus
- **After 5.1:** CTI said Meridian uses Kerberoasting + loader indicators; 5.2 shows **host-level artifacts** for a Meridian-style staging path.
- **Into the Bonus:** `svcupdate.bin` / MeridianLoader become the STIX objects you validate, graph, and serve over TAXII.

---

## Presentation evidence walk (E1–E7)

| Evidence | Artifact in repo | Talk point |
|---|---|---|
| #1 Memory acquisition | `evidence/ev1_winpmem.txt` | WinPmem capture; publish hashes, not the dump |
| #2 Process tree | `evidence/ev2_*.txt` | Volatility `pslist` / `pstree` |
| #3 Network + malfind | `evidence/ev3_*.txt` | `netscan` / `malfind` |
| #4 Prefetch | `evidence/ev4_prefetch.txt` | PECmd: **0 `.pf`** on Server 2022 (honest negative) |
| #5 Amcache | `evidence/ev5_*.txt` | No LOLBin Inventory rows (documented gap) |
| #6 Registry Run | `evidence/ev6_registry.txt` | `MeridianSyncHelper` persistence |
| #7 Static sample | `evidence/ev7_static_triage.txt` + `svcupdate.bin` | Inert stand-in triage + SHA-256 |

Also included: critical-thinking answers and a graded hunt hypothesis in the Canvas report (not required in this data repo beyond the evidence files).

---

## Files in this repo

| File | Description |
|---|---|
| `evidence/` | Captured Evidence #1–#7 text/CSV artifacts |
| `svcupdate.bin` | Inert malware stand-in used for Part C |
| `make_sample.py` | Generator for the stand-in sample |

**Not published:** memory images (`.raw` / `.aff4`) and lab VM credentials. Hashes are in Evidence #1 of the report.

---

## Tools

- WinPmem / go-winpmem  
- Volatility 3  
- Eric Zimmerman / Kroll PECmd and AmcacheParser  
