# Contributing to CardioGuard

Thank you for your interest in contributing to CardioGuard! We welcome contributions from data scientists, machine learning engineers, frontend developers, and clinicians.

Follow these guidelines to ensure a smooth collaboration process.

---

## 1. Getting Started

1. **Fork the Repository**: Create a personal copy of the repository on GitHub.
2. **Clone the Fork**:
   ```bash
   git clone https://github.com/YOUR-USERNAME/cardioguard.git
   cd cardioguard
   ```
3. **Set Up a Virtual Environment**:
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   pip install -r requirements.txt
   ```

---

## 2. Git Branching Strategy

To keep the repository clean and stable, we use the following branch structure:

* **`main`**: Production-ready release branch. Never commit directly to `main`.
* **`dev`**: Integration branch for upcoming releases. All feature branches should merge into `dev`.
* **Feature Branches**: Create a new branch for every feature or bug fix:
  * Features: `feature/feature-name` (e.g., `feature/resnet-backbone`)
  * Bug fixes: `bugfix/bug-name` (e.g., `bugfix/lstm-dimension-mismatch`)
  * Documentation: `docs/docs-topic` (e.g., `docs/api-guide`)

---

## 3. Code Standards & Style Guide

* **Python Standard**: Follow **PEP 8** style guidelines.
* **Docstrings**: Provide Google-style docstrings for all functions, classes, and modules.
* **Type Hints**: Use Python type hinting for function parameters and return types.
* **Formatting**: We recommend using `black` and `isort` to auto-format your Python scripts before committing.

Example format:
```python
def preprocess_signal(raw_signal: np.ndarray, sampling_rate: int = 500) -> np.ndarray:
    """Applies a bandpass filter to the raw ECG signal.

    Args:
        raw_signal: A 1D numpy array representing voltage readings.
        sampling_rate: The sampling frequency of the signal in Hz.

    Returns:
        A 1D numpy array containing the filtered signal.
    """
    # pre-processing logic
    return filtered_signal
```

---

## 4. Submitting a Pull Request (PR)

1. **Sync your Fork**: Ensure your local branch is up-to-date with `dev` on the main repository.
2. **Run Tests**: Verify your changes do not break existing modules.
3. **Commit Messages**: Write clear, descriptive commit messages:
   * *Good*: `feat: add 1D CNN block to ECG1DNet`
   * *Bad*: `fix code`
4. **Open a PR**: Submit a PR from your feature branch to the main repository's `dev` branch.
5. **Review Process**: At least one other core maintainer must review and approve your code before it can be merged. Address any feedback or requested changes promptly.
