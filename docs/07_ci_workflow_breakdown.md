# ⚙️ CI Workflow Breakdown

![Documentation](https://img.shields.io/badge/Documentation-Workflow_Breakdown-blue?style=for-the-badge&logo=markdown)
![Engine](https://img.shields.io/badge/Engine-GitHub_Actions-2088FF?style=for-the-badge&logo=github-actions&logoColor=white)

---

## 📋 Workflow Overview

This document provides a detailed explanation of the GitHub Actions workflow used in this project. Each trigger, job, and step is described to explain its purpose and contribution to the overall CI strategy.

The CI workflow is defined in: **[`ci.yml`](../.github/workflows/ci.yml)**

> [!NOTE]
> The workflow is designed to automatically **validate** code changes and **build** a Docker image *only* when all quality checks pass.

---

## ⚡ Workflow Triggers

The workflow is triggered by the following events:

```yaml
on:
  push:
    branches: [ "main" ]
  pull_request:
    branches: [ "main" ]
```

**Purpose:**
*   Ensures all changes to the `main` branch are validated.
*   Enforces CI checks before pull request merges.
*   Provides immediate feedback on code changes.

---

## 🏗️ Job Definition

The workflow defines a single job to keep execution simple and easy to debug:

```yaml
jobs:
  ci:
    runs-on: ubuntu-latest
```

*   **Platform**: Uses a consistent Linux-based execution environment (`ubuntu-latest`).
*   **Strategy**: Avoids unnecessary complexity for a CI-focused project.

---

## 🪜 Step-by-Step Breakdown

### 1. Checkout Source Code
```yaml
  name: Checkout source code
  uses: actions/checkout@v4
```
*   **Purpose**: Retrieves the latest version of the repository to ensure the pipeline operates on the correct commit.

### 2. Set Up Python Environment
```yaml
- name: Set up Python
  uses: actions/setup-python@v5
  with:
    python-version: "3.11"
```
*   **Purpose**: Enforces a fixed Python runtime version for **deterministic execution**.

### 3. Install Dependencies
```yaml
- name: Install dependencies
  run: |
    python -m pip install --upgrade pip
    pip install -r requirements.txt
```
*   **Purpose**: Installs required dependencies in a clean environment.

### 4. Run Static Code Analysis (Linting)
```yaml
- name: Run linting (flake8)
  run: |
    flake8 app/
```
*   **Purpose**: Acts as a **quality gate**.
    *   Enforces coding standards.
    *   Stops the pipeline immediately on failure.

### 5. Run the Application
```yaml
- name: Run application
  run: |
    python app/main.py
```
*   **Purpose**: Validates basic runtime behavior in the CI environment.

### 6. Build Docker Image
```yaml
- name: Build Docker image
  run: |
    docker build -t ci-pipeline-image .
```
*   **Purpose**: Creates a container image from validated code.
    *   *Executes only if all previous steps succeed.*

---

## 🚨 Failure Behavior

The workflow follows a **fail-fast model**:

*   If **any** step fails, the job terminates immediately.
*   Downstream steps are skipped automatically.
*   Logs clearly indicate the failure point.

> [!TIP]
> This behavior simplifies debugging and improves pipeline efficiency.

---

## 🔍 Observability and Debugging

**GitHub Actions provides:**
*   Step-level logs.
*   Execution timing for each stage.
*   Clear success and failure indicators.

---

## 📝 Summary

The CI workflow is designed to be **clear, deterministic, and enforceable**. By structuring the pipeline into logical steps and placing quality gates early, the workflow ensures that only validated code results in build artifacts.

---

<div align="center">

**[⏪ Previous: Architecture](./06_architecture.md) | [Next: Failure Simulation ➤](./08_failure_simulation_and_recovery.md)**

</div>