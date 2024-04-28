"""Checks module and package names for pep8 compliance."""

import argparse
import re
from collections.abc import Sequence
from enum import Enum
from enum import IntEnum
from enum import auto
from pathlib import Path


class ExitCode(IntEnum):
    """Error codes."""

    OS_FILE = 1
    DATA_ERR = 2
    OK = 0


class Mode(Enum):
    """Enumeration for different modes."""

    STRICT = auto()
    NON_STRICT = auto()


SHORT_NAME_LIMIT_DEFAULT = 30


def check_names(  # noqa: C901, PLR0912
    filenames: Sequence[str | Path],
    short_name_limit: int = SHORT_NAME_LIMIT_DEFAULT,
    ignore_test_files: bool = True,
    mode: Mode = Mode.NON_STRICT,
) -> int:
    """Check the file."""
    for file_to_check in filenames:
        # verify file exists
        if isinstance(file_to_check, str):
            file_path = Path(file_to_check)
        else:
            file_path = file_to_check
        if not file_path.exists():
            print("ERROR: the file doesn't exist")
            return ExitCode.OS_FILE
        module_name = file_path.stem
        package_name = file_path.parent.name
        # check length for module and package name skip test file
        if ignore_test_files and (
            module_name.startswith("test_") or module_name.endswith("_test")
        ):
            continue
        if len(module_name) > short_name_limit:
            print(f"ERROR: module:'{module_name}' is longer than {short_name_limit}")
            return ExitCode.DATA_ERR
        if len(package_name) > short_name_limit:
            print(f"ERROR: package:'{package_name}' is longer than {short_name_limit}")
            return ExitCode.DATA_ERR
        # check module name
        if not re.fullmatch("[A-Za-z_]+", module_name):
            if mode is not Mode.STRICT and re.fullmatch("[A-Za-z0-9_]+", module_name):
                print(
                    f"WARNING: module:'{module_name}' has numbers - allowing but note"
                    "this is not 'strictly' to pep 8 best practices",
                )
            else:
                print(
                    f"ERROR: module:'{module_name}' is not all lowercase with"
                    "underscores",
                )
                return ExitCode.DATA_ERR
        # check package if exists
        # check package name
        if package_name.strip() != "" and not re.fullmatch("[A-Za-z]+", package_name):
            if mode is Mode.NON_STRICT and re.fullmatch("[A-Za-z0-9]+", package_name):
                print(
                    f"WARNING: package:'{package_name}' has numbers - allowing but note"
                    " this is not 'strictly' to pep 8 best practices",
                )
            else:
                print(
                    f"ERROR: package:'{package_name}' is not all lowercase with no"
                    "underscores",
                )
                return ExitCode.DATA_ERR
    return ExitCode.OK


def main() -> int:
    """Get files from passed argument."""
    parser = argparse.ArgumentParser()
    parser.add_argument(
        "filenames",
        nargs="*",
        help="Filenames pre-commit believes are changed.",
    )

    parser.add_argument(
        "-s",
        "--strict",
        action="store_true",
        help="Strict mode",
    )
    parser.add_argument(
        "-l",
        "--short-name-limit",
        help="How long is a 'short' name",
    )
    parser.add_argument(
        "-t",
        "--ignore-test-files",
        action="store_false",
        help="Ignore test files",
    )
    args = parser.parse_args()
    mode = Mode.NON_STRICT
    short_name_limit = (
        int(args.short_name_limit)
        if args.short_name_limit
        else SHORT_NAME_LIMIT_DEFAULT
    )
    if args.strict:
        mode = Mode.STRICT
    return check_names(
        args.filenames,
        short_name_limit=short_name_limit,
        ignore_test_files=args.ignore_test_files,
        mode=mode,
    )


if __name__ == "__main__":
    raise SystemExit(main())
