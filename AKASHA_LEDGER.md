AKASHA II LEDGER

version: 0.4.1
prior_ledger_hash: null
reconciliation_timestamp: null

required_paths:
- core/
- crypto/
- demo/
- interfaces/
- akasha.py
- state.json
- README.md
- AKASHA_SPEC_v0.4.1.md

rules:
- Ledger is authoritative
- Repository must be compliant
- Ledger is updated and carried forward after every reconciliation
