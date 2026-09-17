# Sourcey Docs Delivery - Ory Kratos v26.2.0

Published API-reference documentation for the maintained OSS library **Ory Kratos** (Apache-2.0), generated with the Sourcey static-site generator from the OpenAPI spec pinned at commit `9d7085948039ffb8960160d4979f71527b5cf4d5` (tag v26.2.0).

- Live docs: https://milacl007.github.io/sourcey-docs/
- Operations documented: 56 ; Schemas: 155
- Generator: Sourcey (npm)
- runx: runx-cli 0.9.1 ; receipt: `sha256:fffd1c20c8ad34dd08649128c0875887f8daf931d382a4ae8d8de266c255ecd9` (runx verify: valid)

## Reproduce
```
npx sourcey build skill/api.json
runx skill ./skill -R ./receipts
runx verify --receipt-dir ./receipts
```
