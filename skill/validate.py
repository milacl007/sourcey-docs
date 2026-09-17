import json, urllib.request, hashlib
SPEC = "https://raw.githubusercontent.com/ory/kratos/v26.2.0/spec/api.json"
raw = urllib.request.urlopen(SPEC, timeout=30).read()
spec = json.loads(raw)
methods = ("get", "post", "put", "delete", "patch")
ops = sum(1 for _p, m in spec["paths"].items() for k in m if k.lower() in methods)
obs = {
    "spec_url": SPEC,
    "spec_title": spec["info"]["title"],
    "spec_sha256": hashlib.sha256(raw).hexdigest(),
    "operations": ops,
    "schemas": len(spec.get("components", {}).get("schemas", {})),
    "public_url": "https://milacl007.github.io/sourcey-docs/",
}
print(json.dumps(obs, indent=2))
assert ops >= 20, f"expected >=20 operations, got {ops}"
print("VALIDATION_OK")
