# Sourcey Docs Delivery - Ory Kratos v26.2.0

Published API-reference documentation for the maintained OSS library Ory Kratos, generated with Sourcey and validated with a recomputable runx receipt.

- Live documentation site: https://milacl007.github.io/sourcey-docs/ (HTTP 200, navigable and searchable)
- Target library: Ory Kratos, pinned tag v26.2.0, commit 9d7085948039ffb8960160d4979f71527b5cf4d5, license Apache-2.0
- OpenAPI 3.0.3 source: https://raw.githubusercontent.com/ory/kratos/v26.2.0/spec/api.json (sha256 f258cd01)
- Coverage: 56 documented operations across 48 paths; 155 component schemas
- Generator: Sourcey (npm) static-site generator, published to GitHub Pages
- Governance: runx-cli 0.9.1; receipt runx:receipt:sha256:fffd1c20c8ad34dd08649128c0875887f8daf931d382a4ae8d8de266c255ecd9; runx verify reports valid
- Reproduce docs: npx sourcey build skill/api.json
- Reproduce receipt: runx skill ./skill -R ./receipts then runx verify --receipt-dir ./receipts
