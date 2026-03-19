#!/usr/bin/env python3
"""
Scan a wheel's ELF files for the exact error that auditwheel encounters.
Helps diagnose malformed ELF binaries.
"""
import sys
from pathlib import Path
from elftools.elf.elffile import ELFFile

def scan_wheel_elf(tmpdir):
    found_bad = False
    for so_file in Path(tmpdir).rglob('*.so*'):
        if so_file.is_file():
            try:
                with open(so_file, 'rb') as f:
                    elf = ELFFile(f)
                    list(elf.iter_segments())
                    list(elf.iter_sections())
            except Exception as e:
                print(f"AUDITWHEEL_BAD_ELF {so_file.relative_to(tmpdir)}: {type(e).__name__}: {e}")
                found_bad = True
    if not found_bad:
        print("AUDITWHEEL_SCAN_FOUND_NO_ISSUES")

if __name__ == '__main__':
    if len(sys.argv) < 2:
        print("Usage: scan-elf-errors.py <tmpdir>")
        sys.exit(1)
    scan_wheel_elf(sys.argv[1])
