# Release Checklist (v0.1.0-alpha)

## Repository basics

- [x] Repository created as `bithome-protocol`
- [ ] Public visibility enabled
- [ ] Default branch set (`main`)

## Core files

- [x] `README.md` committed
- [x] `PROTOCOL.md` committed
- [x] `examples/` committed
- [x] `schema/listing-schema.json` committed
- [x] `scripts/` directory with validation tools committed

## Protocol consistency

- [x] `kind:30023` defined as canonical source
- [x] `d` marked REQUIRED everywhere
- [x] `d` UUIDv4 requirement consistent in docs/examples/schema
- [x] Replace semantics documented (same pubkey + same d + newer created_at)
- [x] No extra business logic introduced in protocol docs

## Example validation

- [x] `listing-basic.json` validates against schema
- [x] `listing-full.json` validates against schema
- [x] `listing-updated.json` validates and reuses same `d` as basic
- [x] `nip99-derived.json` keeps same `d` and remains marked as derived
- [x] Validation script created and passes all checks

## Publication

- [ ] Add GitHub topics: `nostr`, `bitcoin`, `real-estate`, `protocol`, `specification`
- [ ] Enable Discussions (optional)
- [ ] Create issue: “v0.2 schema feedback”
- [ ] Announce on Nostr with repository URL
