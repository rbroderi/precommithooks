# flake8: noqa
from __future__ import annotations

import sys
import unittest
from pathlib import Path

from precommithooks import check_names, Mode

sys.path.append(str(Path(__file__).parent.parent))
RESOURCES = Path(__file__).parent / "resources"


class TestCheckNames(unittest.TestCase):
    def test_check_names_no_files(self) -> None:
        self.assertEqual(check_names([]), 0)

    def test_check_names_file(self) -> None:
        self.assertEqual(
            check_names([str(x) for x in {RESOURCES / "withoutunderscore.txt"}]),
            0,
        )
        self.assertEqual(
            check_names([str(x) for x in {RESOURCES / "with_underscore.txt"}]),
            0,
        )
        self.assertNotEqual(check_names([str(x) for x in {RESOURCES / "!.txt"}]), 0)
        self.assertEqual(
            check_names([str(x) for x in {RESOURCES / "with_underscore.txt"}]),
            0,
        )
        self.assertNotEqual(
            check_names(
                [
                    str(x)
                    for x in {RESOURCES / "with_underscores" / "withoutunderscore.txt"}
                ],
            ),
            0,
        )
        self.assertNotEqual(
            check_names(
                [str(x) for x in {RESOURCES / "loooooooooooooooooooongfilename.txt"}],
            ),
            0,
        )
        self.assertEqual(
            check_names(
                [str(x) for x in {RESOURCES / "loooooooooooooooooooongfilename.txt"}],
                short_name_limit=40,
            ),
            0,
        )
        self.assertEqual(
            check_names(
                [str(x) for x in {RESOURCES / "namewithnums123.txt"}],
            ),
            0,
        )
        self.assertNotEqual(
            check_names(
                [str(x) for x in {RESOURCES / "namewithnums123.txt"}],
                mode=Mode.STRICT,
            ),
            0,
        )


if __name__ == "__main__":
    unittest.main()
