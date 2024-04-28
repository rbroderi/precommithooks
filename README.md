# precommithooks

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
        args: [-s]
        verbose: true
```
