# 💻 Technology Stack

![Documentation](https://img.shields.io/badge/Documentation-Tech_Stack-blue?style=for-the-badge&logo=markdown)
![Stack](https://img.shields.io/badge/Stack-Python_Docker_GitHub_Actions-purple?style=for-the-badge)

---

## 📋 Overview

This project uses a carefully selected set of tools and technologies to demonstrate a modern, production-relevant **Continuous Integration (CI)** workflow. Each component of the stack was chosen for its reliability, industry adoption, and suitability for CI-focused use cases.

---

## 🔄 Version Control & Collaboration

### <img src="https://git-scm.com/images/logos/downloads/Git-Icon-1788C.png" width="30"/> Git
**Git is used for source code version control, enabling:**
*   Change tracking.
*   Branch-based development.
*   Clear commit history.

### <img src="https://github.githubassets.com/images/modules/logos_page/GitHub-Mark.png" width="30"/> GitHub
**GitHub serves as the central code hosting platform:**
*   Repository management.
*   Pull request workflows.
*   Native integration with GitHub Actions.

---

## ⚙️ CI Platform

### <img src="https://github.githubassets.com/images/modules/logos_page/GitHub-Mark.png" width="30"/> GitHub Actions
**GitHub Actions is the CI engine for this project. It enables:**
*   Event-driven pipeline execution.
*   YAML-based workflow definitions.
*   GitHub-hosted runners for consistent execution.

> [!NOTE]
> GitHub Actions allows for a cloud-native, managed environment without additional infrastructure overhead.

---

## 🐍 Programming Language

### Python
**Python is used to create a lightweight, deterministic application for CI validation.**

| Feature | Benefit |
| :--- | :--- |
| **Fast Startup** | Reduces CI wait times. |
| **Readable Syntax** | Ensures clear code examples. |
| **Ecosystem** | Strong support and integration with CI tools. |

---

## 🔍 Code Quality & Analysis

### flake8
**flake8 is used for static code analysis and linting.**

*   Enforces PEP 8 coding standards.
*   Detects syntax and style issues early.
*   **Fail-fast behavior**: Linting acts as a hard quality gate.

---

## 🐳 Containerization

### Docker
**Docker is used to package the application into a container image.**

*   Ensures **environment consistency**.
*   Produces **portable artifacts**.
*   Aligns with modern deployment workflows.

*Docker image builds are executed within the CI pipeline only after all validation steps pass.*

---

## 🖥️ CI Execution Environment

### GitHub-Hosted Runners
The pipeline uses standard Linux runners (`ubuntu-latest`), providing:
*   ✅ Clean, ephemeral environments.
*   ✅ Pre-installed Docker support.
*   ✅ Consistent and predictable behavior.

---

## 🧰 Supporting Tools (Development)

The following tools are used for local development but do not effect CI execution:
*   **Python** (Local runtime)
*   **Docker Desktop** (Local validation)
*   **VS Code** (IDE)

---

## 📝 Summary

The technology stack selected for this project reflects common tools used in modern DevOps and platform engineering environments. The combination of **GitHub Actions, Python, flake8, and Docker** provides a strong foundation for building reliable, scalable CI pipelines.

---

<div align="center">

**[⏪ Previous: Strategy & Design](./04_ci_strategy_and_design.md) | [Next: Architecture ➤](./06_architecture.md)**

</div>