precommithooks
================================================
[![GitHub License](https://img.shields.io/github/license/rbroderi/precommithooks)](https://github.com/rbroderi/precommithooks/blob/main/LICENSE)
[![Code style: black](https://img.shields.io/endpoint?url=https://raw.githubusercontent.com/astral-sh/ruff/main/assets/badge/v2.json)](https://github.com/astral-sh/ruff)
[![Generic badge](https://img.shields.io/badge/mypy-typed-purple.svg)](http://mypy-lang.org/)
[![Generic badge](https://img.shields.io/badge/beartype-runtime_typed-cyan.svg)](https://github.com/beartype/beartype)
[![Generic badge](https://img.shields.io/badge/bandit-checked-magenta.svg)](https://bandit.readthedocs.io/en/latest/)
[![Generic badge](https://img.shields.io/badge/uv-requirements-yellow.svg)](https://github.com/astral-sh/uv)
[![Dynamic TOML Badge](https://img.shields.io/badge/dynamic/toml?url=https%3A%2F%2Fraw.githubusercontent.com%2Frbroderi%2Fprecommithooks%2Fmain%2Fpyproject.toml&query=%24.project.version&label=Version)](https://github.com/rbroderi/precommithooks/releases)

My custom precommit hooks, including a pep-8 filename check


## Description



Usage:
---

### Default
```
  - repo: https://github.com/rbroderi/precommithooks
    rev: v1.0.1
    hooks:
      - id: python_file_name_check
        name: "Python: File name check"
        verbose: true
```
### Strict mode
```
  - repo: https://github.com/rbroderi/precommithooks
    rev: v1.0.1
    hooks:
      - id: python_file_name_check
        name: "Python: File name check"
        args: [--strict]
        verbose: true
```

## Args
* --strict (default to false)
* --short-name-limit (defaults to 30)
* --ignore-test-files (defaults to false)
