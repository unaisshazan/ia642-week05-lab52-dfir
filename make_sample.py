#!/usr/bin/env python3
# Reconstructs Meridian's defanged stand-in for the BILL-WS-14 quarantine sample.
banner = b"MeridianLoader/2.1 (c) internal build\x00"
marker = "MRD-STAGE2-INIT".encode("utf-16-le")
stub = bytes([0x90, 0x90, 0x90, 0x31, 0xC0, 0x50, 0x68, 0x00, 0x00, 0x00, 0x00])
c2 = b"sync-update.meridian-relay.test\x00"
data = b"MZ" + b"\x90" * 58  # minimal MZ stub: header marker only, not a valid PE
data += banner
data += marker
data += stub
data += c2
data += b"\x00" * 32
with open("svcupdate.bin", "wb") as f:
    f.write(data)
print(f"wrote svcupdate.bin, {len(data)} bytes")
