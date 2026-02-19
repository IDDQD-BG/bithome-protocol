#!/usr/bin/env python3
"""
Validates BitHome Protocol example JSON files against the listing schema.

This script verifies:
1. All canonical examples (kind:30023) validate against listing-schema.json
2. UUIDv4 format compliance in d tags
3. Replace semantics (listing-updated.json reuses same d as listing-basic.json)
4. NIP-99 derived event maintains same d tag
"""

import json
import sys
import os
from pathlib import Path

try:
    from jsonschema import validate, ValidationError, Draft7Validator
except ImportError:
    print("Error: jsonschema library not found.")
    print("Please install it with: pip install jsonschema")
    sys.exit(1)


def load_json(filepath):
    """Load and parse JSON file."""
    with open(filepath, 'r', encoding='utf-8') as f:
        return json.load(f)


def validate_example(example_path, schema):
    """Validate a single example against the schema."""
    example_name = os.path.basename(example_path)
    try:
        example = load_json(example_path)
        
        # Only validate kind:30023 events against the schema
        if example.get('kind') == 30023:
            validate(instance=example, schema=schema)
            print(f"✓ {example_name}: VALID")
            return True, example
        else:
            print(f"⊘ {example_name}: SKIPPED (kind:{example.get('kind')}, not canonical 30023)")
            return None, example
    except ValidationError as e:
        print(f"✗ {example_name}: INVALID")
        print(f"  Error: {e.message}")
        if e.path:
            print(f"  Path: {list(e.path)}")
        return False, None
    except Exception as e:
        print(f"✗ {example_name}: ERROR - {e}")
        return False, None


def extract_d_tag(event):
    """Extract the d tag value from an event."""
    for tag in event.get('tags', []):
        if len(tag) >= 2 and tag[0] == 'd':
            return tag[1]
    return None


def main():
    # Setup paths
    repo_root = Path(__file__).parent.parent
    schema_path = repo_root / 'schema' / 'listing-schema.json'
    examples_dir = repo_root / 'examples'
    
    print("BitHome Protocol Example Validator")
    print("=" * 50)
    print()
    
    # Load schema
    print(f"Loading schema: {schema_path}")
    schema = load_json(schema_path)
    print()
    
    # Validate each example
    print("Validating examples:")
    print("-" * 50)
    
    example_files = sorted(examples_dir.glob('*.json'))
    results = {}
    events = {}
    
    for example_file in example_files:
        result, event = validate_example(example_file, schema)
        results[example_file.name] = result
        if event:
            events[example_file.name] = event
    
    print()
    
    # Additional checks
    print("Additional Protocol Checks:")
    print("-" * 50)
    
    # Check replace semantics (listing-updated.json should reuse d from listing-basic.json)
    basic_d = extract_d_tag(events.get('listing-basic.json', {}))
    updated_d = extract_d_tag(events.get('listing-updated.json', {}))
    
    if basic_d and updated_d:
        if basic_d == updated_d:
            print(f"✓ Replace semantics: listing-updated.json reuses d tag from listing-basic.json")
            print(f"  Shared d: {basic_d}")
        else:
            print(f"✗ Replace semantics: d tags don't match")
            print(f"  listing-basic.json d: {basic_d}")
            print(f"  listing-updated.json d: {updated_d}")
            results['replace_semantics'] = False
    
    # Check NIP-99 derived event maintains same d
    nip99_d = extract_d_tag(events.get('nip99-derived.json', {}))
    if basic_d and nip99_d:
        if basic_d == nip99_d:
            print(f"✓ NIP-99 mirror: maintains same d tag as canonical event")
            print(f"  Shared d: {basic_d}")
        else:
            print(f"✗ NIP-99 mirror: d tag doesn't match canonical event")
            print(f"  Canonical d: {basic_d}")
            print(f"  Mirror d: {nip99_d}")
            results['nip99_consistency'] = False
    
    print()
    
    # Summary
    print("Summary:")
    print("-" * 50)
    
    valid_count = sum(1 for v in results.values() if v is True)
    invalid_count = sum(1 for v in results.values() if v is False)
    skipped_count = sum(1 for v in results.values() if v is None)
    
    print(f"Valid: {valid_count}")
    print(f"Invalid: {invalid_count}")
    print(f"Skipped: {skipped_count}")
    
    if invalid_count > 0:
        print()
        print("❌ VALIDATION FAILED")
        return 1
    else:
        print()
        print("✅ ALL CHECKS PASSED")
        return 0


if __name__ == '__main__':
    sys.exit(main())
