# BitHome Protocol

Bitcoin-native real estate protocol on Nostr.

## Scope

BitHome Protocol defines the canonical event format for listings published as Nostr events.

Protocol scope covers:
- event kind and tags
- identity and replace/update semantics
- canonical pricing unit

Out of scope (implementation/business layer):
- escrow, payments, KYC/AML
- chat UX, ranking, recommendation
- brokerage workflows, contracts, legal processes

## Canonical Model (v1)

- Canonical event kind: `30023`
- Canonical listing identity: tuple `(kind=30023, pubkey, d)`
- Canonical price unit: `sats_per_m2`
- Optional interoperability mirror: `kind=30402` (derived only, not source of truth)

## `d` tag requirement

- `d` is REQUIRED.
- `d` MUST be a raw UUIDv4 (lowercase hex + hyphens).
- No prefix/namespaces are allowed (`listing:`, `urn:uuid:` etc. are invalid).

Example valid UUIDv4:
- `550e8400-e29b-41d4-a716-446655440000`

## Replace semantics

A listing update is published as a new event with:
- same `kind` (`30023`)
- same `pubkey`
- same `d`
- newer `created_at`

The newer event replaces older versions for that `(kind, pubkey, d)` identity.

## Repository layout

- `PROTOCOL.md` — normative protocol specification
- `examples/` — ready-to-test event examples
- `schema/listing-schema.json` — JSON Schema for validation
- `RELEASE-CHECKLIST.md` — publication checklist
