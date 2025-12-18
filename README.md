# GitHub Actions CI Pipeline

This project demonstrates the design and implementation of an engineering-grade **Continuous Integration (CI) pipeline** using GitHub Actions. The pipeline enforces automated quality checks, validates application behavior, and builds Docker container artifacts only after all validation stages pass.

The project is intentionally scoped to focus on **CI best practices**, including fail-fast quality gates, deterministic execution, and clear pipeline observability. Continuous Deployment (CD) and runtime infrastructure are deliberately excluded to maintain a strong separation of concerns.

## Key Highlights

- Automated CI triggered on push and pull requests
- Static code analysis using linting as a quality gate
- Deterministic application execution in CI
- Docker image build gated behind validation steps
- Fail-fast pipeline behavior with clear failure feedback
- Intentional failure simulation and recovery validation

## Technology Stack

- Git & GitHub
- GitHub Actions
- Python
- flake8 (linting)
- Docker
- GitHub-hosted Linux runners

---
