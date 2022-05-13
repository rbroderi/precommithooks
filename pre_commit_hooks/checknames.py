"""Checks module and package names for pep8 compliance."""
from __future__ import annotations

import argparse
import re
from enum import IntEnum
from pathlib import Path
from typing import Sequence

try:
    from exit_codes.exit_codes import ExitCode
except ImportError:

    class ExitCode(IntEnum):  # type: ignore
        """Redefine in case ExitCode is not installed."""

        OS_FILE = 1
        DATA_ERR = 2
        OK = 0


SHORT_NAME_LIMIT = 30


def check_names(filenames: Sequence[str]) -> int:
    """Check the file."""
    for file_to_check in filenames:
        # verify file exists
        file_path = Path(file_to_check)
        if not file_path.exists():
            print(f"ERROR: the file:{file_path} doesn't exist")
            return ExitCode.OS_FILE
        module_name = file_path.stem
        package_name = file_path.parent.name
        # check length for module and package name
        if len(module_name) > SHORT_NAME_LIMIT:
            print(f"ERROR: '{module_name}' is longer than {SHORT_NAME_LIMIT}")
            return ExitCode.DATA_ERR
        if len(package_name) > SHORT_NAME_LIMIT:
            print(f"ERROR: '{package_name}' is longer than {SHORT_NAME_LIMIT}")
            return ExitCode.DATA_ERR
        # check module name
        if not re.fullmatch("[A-Za-z_]+", module_name):
            if re.fullmatch("[A-Za-z0-9_]+", module_name):
                print(
                    f"WARNING: '{module_name}' has numbers - allowing but note this is"
                    " not 'strictly' to pep 8 best practices",
                )
            else:
                print(f"ERROR: '{module_name}' is not all lowercase with underscores")
                return ExitCode.DATA_ERR
        # check package if exists
        # check package name
        if package_name.strip() != "" and not re.fullmatch("[A-Za-z]+", package_name):
            if re.fullmatch("[A-Za-z0-9]+", package_name):
                print(
                    f"WARNING: '{package_name}' has numbers - allowing but note"
                    " this is not 'strictly' to pep 8 best practices",
                )
            else:
                print(
                    f"ERROR: '{package_name}' is not all lowercase with no underscores",
                )
                return ExitCode.DATA_ERR
    return ExitCode.OK


def main(argv: Sequence[str] | None = None) -> int:
    """Get files from passed argument."""
    parser = argparse.ArgumentParser()
    parser.add_argument(
        "filenames",
        nargs="*",
        help="Filenames pre-commit believes are changed.",
    )

    args = parser.parse_args(argv)
    if argv is not None:
        return check_names(args.filenames)
    return ExitCode.OK


if __name__ == "__main__":
    raise SystemExit(main())
