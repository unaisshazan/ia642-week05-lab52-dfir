# IA 642 Week 05 Lab 5.2 — Live Triage on MERIDIAN-APP01

Eastern Michigan University · Defensive Security · Fall 2026

**Authors:** Unais Ali (E02805019), Hafiz Usama (E02574092)

**Public repo:** https://github.com/unaisshazan/ia642-week05-lab52-dfir

## What this is

Lab 5.2 builds **MERIDIAN-APP01** (Windows Server 2022), stages a LOLBin-style `certutil` trail and an HKCU Run-key persistence entry, acquires live memory with WinPmem, triages with Volatility 3, parses Prefetch/Amcache, and classifies the inert `svcupdate.bin` stand-in.

## Submission files

| File | Description |
|------|-------------|
| `Ali_Week05_Module02_Lab.pdf` | Lab report |
| `Ali_Week05_Module02_Lab.tex` | LaTeX source |
| `evidence/` | Captured Evidence #1–#7 text/CSV artifacts |
| `svcupdate.bin` | Inert malware stand-in used for Part C |
| `make_sample.py` | Generator for the stand-in sample |

## Notes

- Memory images (`.raw` / `.aff4`) are **not** published (size + lab isolation). Hashes are in Evidence #1 of the report.
- Lab VM credentials are **not** published.
- On Server 2022, Prefetch produced 0 `.pf` files and Amcache did not index `certutil`/`calc`/`notepad` InventoryApplicationFile rows; the report documents that finding with corroborating artifacts.

## Tools

- WinPmem / go-winpmem
- Volatility 3
- Eric Zimmerman / Kroll PECmd and AmcacheParser
