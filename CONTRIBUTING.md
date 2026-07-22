# Contributing to CardioGuard: Developer Guidelines

We welcome contributions to CardioGuard! To maintain high code quality, reliability, and clinical safety standards, we enforce a strict integration pipeline.

Please read this document carefully before making changes or opening a pull request.

---

## 1. Development Environment Setup

Ensure you are working in an isolated environment. We require **Python 3.9+**.

### Clone and Environment Initialization
```bash
git clone https://github.com/Raghuvaranlokati/cardioguard.git
cd cardioguard
python -m venv venv
source venv/bin/activate  # Windows: venv\Scripts\activate
pip install -r requirements.txt
```

### Install Dev Dependencies
We use the following tooling for formatting, linting, type-checking, and testing:
```bash
pip install black isort ruff mypy pytest pytest-cov
```

---

## 2. Coding Standards & Integrity Guardrails

To prevent production bugs and model degradation, all code must meet these parameters:

### Python Conventions
* **PEP 8 Compliance**: Enforced strictly via our CI/CD pipeline.
* **Type Hinting**: All public classes, methods, and functions must be fully type-hinted.
* **Docstrings**: Provide Google-style docstrings for every class, method, and function.

### Deep Learning Architectural Invariants
* **PyTorch RNN Padding Invariant**: If you edit models involving RNN/LSTM/GRU sequence extraction (`lstm_out[:, -1, :]`), you **MUST** configure the data loader for **PRE-PADDING** (padding zeros at the beginning). Post-padding is prohibited as it causes hidden states to capture zero vectors, resulting in model collapse.
* **Generalization**: Always include dropout layers (`nn.Dropout1d` / `nn.Dropout2d`) and batch normalization to prevent overfitting on local medical datasets.

---

## 3. Tooling (Format & Lint Checklist)

Before making a commit, run these commands to format and lint your workspace:

### Format Code
```bash
# Auto-format import orders
isort .

# Auto-format code blocks
black .
```

### Lint and Type Check
```bash
# Static code analysis
ruff check .

# Static type checking
mypy --ignore-missing-imports .
```

---

## 4. Git Workflow & Conventional Commits

We use a branching model structured around development updates and production stability:

```
main (Production Release)
  ▲
  │ (Release merges only)
dev (Staging / Integration)
  ▲
  ├── feature/resnet-backbone
  └── bugfix/api-input-validation
```

### Branch Naming Conventions
* **Features**: `feature/short-desc` (e.g., `feature/gradcam-integration`)
* **Bug Fixes**: `bugfix/short-desc` (e.g., `bugfix/nan-loss-prevention`)
* **Docs**: `docs/short-desc` (e.g., `docs/api-specs`)

### Conventional Commit Messages
We follow the [Conventional Commits](https://www.conventionalcommits.org/) specification:
* `feat: ...` -> A new feature (e.g., `feat: integrate ResNet module for visual plots`)
* `fix: ...` -> A bug fix (e.g., `fix: correct pre-padding boundary logic`)
* `docs: ...` -> Documentation updates (e.g., `docs: update setup guidelines`)
* `chore: ...` -> Build tasks, package updates, etc. (e.g., `chore: bump uvicorn version`)

---

## 5. Pull Request Checklists

When you open a Pull Request (PR) to merge changes into the `dev` branch:

1. **Self-Review**: Make sure all comments are meaningful and no diagnostic debugger lines (`print`, temporary files) are left behind.
2. **Run Tests**: Verify all unit tests pass:
   ```bash
   pytest tests/
   ```
3. **Verify CI/CD Status**: Ensure that automated checks for style (Black, Isort, Ruff) and typing (Mypy) pass on GitHub Actions.
4. **Code Review**: At least one maintainer must review and approve the PR. Code reviews are structured to check both logical correctness and deep learning architectural integrity (evaluating padding logic, learning rate bounds, and dropout rates).
