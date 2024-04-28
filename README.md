# precommithooks
================================================
![Dynamic TOML Badge](https://img.shields.io/badge/dynamic/toml?url=https%3A%2F%2Fraw.githubusercontent.com%2Frbroderi%2Fprecommithooks%2Fmain%2Fpyproject.toml&query=%24.project.version&label=Version)

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
