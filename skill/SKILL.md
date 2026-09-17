---
name: sourcey-docs-validation
version: 0.1.0
description: Deterministically validate the pinned Ory Kratos OpenAPI spec used to generate the published Sourcey documentation site.
---
# Sourcey Docs Validation
Re-fetches the pinned Ory Kratos v26.2.0 OpenAPI spec and asserts it exposes >=20 documented operations, recording a recomputable runx receipt for the published docs at https://milacl007.github.io/sourcey-docs/.
