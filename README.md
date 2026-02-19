# BitHome Protocol

Bitcoin-native real estate protocol on Nostr.

Live reference platform:
https://bithome.site

This repository defines the **protocol only**.  
It does not contain application code or business logic.

---

## Scope

BitHome Protocol defines the canonical event format for real estate listings
published as Nostr events.

The protocol scope covers:
- event kind and tag semantics
- listing identity and replace/update rules
- canonical pricing units and representation

Out of scope (implementation / business layer):
- escrow, payments, KYC/AML
- chat UX, ranking, recommendations
- brokerage workflows, contracts, legal processes

---

## Canonical Model (v1)

- **Canonical event kind:** `30023`
- **Canonical listing identity:** tuple `(kind=30023, pubkey, d)`
- **Canonical pricing unit:** `sats_per_m2`
- **Optional interoperability mirror:** `kind=30402`
  - derived only
  - not a source of truth

---

## `d` Tag Requirement

- `d` is **REQUIRED**
- `d` MUST be a raw **UUIDv4**
- Lowercase hexadecimal with hyphens
- No prefixes or namespaces are allowed

Invalid examples:
- `listing:550e8400-e29b-41d4-a716-446655440000`
- `urn:uuid:550e8400-e29b-41d4-a716-446655440000`

Example valid UUIDv4:
- `550e8400-e29b-41d4-a716-446655440000`

---

## Replace Semantics

A listing update is published as a new event with:
- the same `kind` (`30023`)
- the same `pubkey`
- the same `d`
- a newer `created_at` value

The newer event **replaces** all older events sharing the same
`(kind, pubkey, d)` identity, according to Nostr replaceable event semantics.

---

## NIP-99 Interoperability

- NIP-99 events are **derived mirrors**
- They MUST be generated deterministically from the canonical `kind:30023` event
- Manual editing of NIP-99 events is forbidden
- Deleting a NIP-99 event MUST NOT affect canonical state

Canonical data always lives in `kind:30023`.

---

## Repository Layout

- `PROTOCOL.md` — normative protocol specification
- `HARDWARE.md` — hardware requirements for clients, developers, and relay operators
- `examples/` — ready-to-test canonical and derived event examples
- `schema/listing-schema.json` — JSON Schema for validation
- `RELEASE-CHECKLIST.md` — publication and consistency checklist
- `scripts/` — generators and verification tools for derived artifacts

---

## Reference Implementation

The BitHome Protocol is actively used by the live platform:
https://bithome.site

This repository serves as the canonical specification for interoperable
clients, indexers, and tooling.
