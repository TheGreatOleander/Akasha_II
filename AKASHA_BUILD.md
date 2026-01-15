# AKASHA II — BUILD & EMISSION PROMPT (AUTHORITATIVE)

You are executing a deterministic repository reconciliation and emission.

The goal is to produce exactly one authoritative repository ZIP artifact
that is ledger-compliant and emission-safe.

---

## DEFINITIONS

BOOTSTRAP_ROOT  
The root directory produced by extracting the bootstrap bundle.

REPO_FILES  
A directory tree within BOOTSTRAP_ROOT containing repository source files.

REPO_ZIP  
The authoritative ZIP artifact representing the Akasha II repository.

---

## EXECUTION STEPS

### 1. Establish Scope
Treat BOOTSTRAP_ROOT as the sole execution scope.
Do not read from or assume external directories.

---

### 2. Discover Existing Repository ZIP
Search BOOTSTRAP_ROOT for files matching:

    Akasha_*-main.zip

Excluding the bootstrap archive itself.

---

### 3. Resolve Repository Source

IF exactly one qualifying ZIP is found:
- Designate it as REPO_ZIP
- Proceed to ledger reconciliation

IF more than one qualifying ZIP is found:
- HALT with ambiguity error

IF zero qualifying ZIPs are found:
- Validate repository files (Step 4)

---

### 4. Validate Repository Files
Verify that the following required paths exist in BOOTSTRAP_ROOT:

- core/
- crypto/
- demo/
- interfaces/
- akasha.py
- state.json
- README.md
- AKASHA_SPEC_v0.4.1.md

IF any required path is missing:
- HALT with compliance error

---

### 5. Repository Assembly (AUTHORIZED)
If validation succeeds and no ZIP was found:

- Assemble a ZIP from the validated repository files
- Name the ZIP exactly:

    Akasha_II-main.zip

- Designate this ZIP as REPO_ZIP

---

### 6. Ledger Reconciliation
Apply the AKASHA II LEDGER:

version: 0.4.1

- Ledger is authoritative
- REPO_ZIP must contain all required paths
- Update reconciliation_timestamp
- Carry ledger forward unchanged otherwise

---

### 7. Emission
Emit REPO_ZIP as the final execution artifact.

Do NOT:
- modify contents after reconciliation
- rename the ZIP
- emit additional artifacts

Execution ends after emission.
