# Scripts Directory

This directory contains validation and verification tools for the BitHome Protocol.

## Available Scripts

### `validate_examples.py`

Validates all example JSON files against the protocol schema and checks protocol compliance.

**Usage:**
```bash
python3 scripts/validate_examples.py
```

**What it checks:**
- All canonical examples (kind:30023) validate against `listing-schema.json`
- UUIDv4 format compliance in `d` tags
- Replace semantics: `listing-updated.json` reuses the same `d` tag as `listing-basic.json`
- NIP-99 derived events maintain the same `d` tag as their canonical source

**Requirements:**
- Python 3.6+
- `jsonschema` library: `pip install jsonschema`

**Exit codes:**
- `0`: All validations passed
- `1`: One or more validations failed
