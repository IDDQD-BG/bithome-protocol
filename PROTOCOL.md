# BitHome Protocol Specification

Version: 0.1.0-alpha  
Date: 2026-02-16  
Status: Draft

## 1. Purpose

This specification defines the canonical Nostr event format for BitHome real-estate listings.

## 2. Canonical Event

### 2.1 Kind

- MUST use `kind: 30023`.

### 2.2 Required tags

A valid listing event MUST include:
- `["bithome", "v1"]`
- `["d", "<uuidv4>"]`
- `["type", "<type>"]`
- `["exp", "<unix_seconds>"]`
- `["lat", "<float>"]`
- `["lon", "<float>"]`
- `["sats_per_m2", "<positive_integer>"]`

`type` MUST be one of:
- `sell`
- `rent_out`
- `want_buy`
- `want_rent`

## 3. Listing Identity (`d`)

### 3.1 Requirements

- `d` is REQUIRED.
- `d` MUST be a UUIDv4 in raw canonical format:
  - lowercase hex
  - hyphenated
  - no prefixes
- Example: `550e8400-e29b-41d4-a716-446655440000`

### 3.2 Uniqueness

The tuple below uniquely identifies a listing:
- `(kind:30023, pubkey, d)`

### 3.3 Rationale for UUIDv4

UUIDv4 is used because it provides:
- collision resistance for decentralized creation
- client-side generation without server coordination
- stable identity across updates and mirrors

## 4. Replace / Update Semantics

An event replaces previous listing state when all are true:
- same `kind` (`30023`)
- same `pubkey`
- same `d`
- newer `created_at`

Consumers SHOULD treat the newest event as current state and older ones as historical versions.

## 5. Canonical Pricing

- Canonical price is `sats_per_m2`.
- UI display fields (for example fiat strings) are non-canonical.

## 6. Optional Interop Mirror (NIP-99)

BitHome MAY emit a derived `kind:30402` mirror for discovery.

Rules:
- canonical source remains `kind:30023`
- mirror MUST reuse the same `d`
- mirror updates are regenerated from canonical event updates

## 7. Non-goals

This protocol does NOT define:
- payment/escrow execution
- ranking/recommendation logic
- legal/contractual workflows
