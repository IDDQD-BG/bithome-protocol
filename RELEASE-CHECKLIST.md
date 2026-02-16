# Release Checklist (v0.1.0-alpha)

## Repository basics

- [ ] Repository created as `bithome-protocol`
- [ ] Public visibility enabled
- [ ] Default branch set (`main`)

## Core files

- [ ] `README.md` committed
- [ ] `PROTOCOL.md` committed
- [ ] `examples/` committed
- [ ] `schema/listing-schema.json` committed

## Protocol consistency

- [ ] `kind:30023` defined as canonical source
- [ ] `d` marked REQUIRED everywhere
- [ ] `d` UUIDv4 requirement consistent in docs/examples/schema
- [ ] Replace semantics documented (same pubkey + same d + newer created_at)
- [ ] No extra business logic introduced in protocol docs

## Example validation

- [ ] `listing-basic.json` validates against schema
- [ ] `listing-full.json` validates against schema
- [ ] `listing-updated.json` validates and reuses same `d` as basic
- [ ] `nip99-derived.json` keeps same `d` and remains marked as derived

## Publication

- [ ] Add GitHub topics: `nostr`, `bitcoin`, `real-estate`, `protocol`, `specification`
- [ ] Enable Discussions (optional)
- [ ] Create issue: “v0.2 schema feedback”
- [ ] Announce on Nostr with repository URL
