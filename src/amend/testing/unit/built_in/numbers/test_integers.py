import unittest

from amend.built_in.numbers.integers import amend_integer


class TestAmendInteger(unittest.TestCase):
    def test_no_amendment_needed(self):
        try:
            amend_integer(integer=0)
        except Exception as e:
            self.assert_(
                False,
                f"Threw exception when no amendment was needed: {e}",
            )

    def test_type_mismatch(
        self,
    ):
        integer = "0"
        expected_result = 0

        try:
            result = amend_integer(integer=integer)
        except Exception as e:
            self.assert_(
                False,
                f"Threw exception when amendment was possible: {e}",
            )
        self.assertEqual(
            result,
            expected_result,
        )

        self.assertRaises(
            TypeError,
            amend_integer,
            integer=integer,
            type_mismatch_action="error",
        )

    def test_cast_error(
        self,
    ):
        value_on_cast_error = 1

        self.assertRaises(
            TypeError,
            amend_integer,
            integer=None,
        )
        self.assertRaises(
            ValueError,
            amend_integer,
            integer=None,
            value_on_cast_error="a",
        )

        try:
            result = amend_integer(
                integer=None,
                value_on_cast_error=value_on_cast_error,
            )
        except Exception as e:
            self.assert_(
                False,
                f"Threw exception when value on cast error was valid: {e}",
            )

        self.assertEqual(
            result,
            value_on_cast_error,
        )

    def test_value_violation(
        self,
    ):
        try:
            amend_integer(
                integer=0,
                value_violation_action="error",
            )
        except Exception as e:
            self.assert_(
                False,
                f"Threw exception for value violation without defined limits: {e}",
            )

        try:
            amend_integer(
                integer=0,
                minimum_value=0,
                value_violation_action="error",
            )
        except Exception as e:
            self.assert_(
                False,
                f"Threw exception for value violation with exact minimum: {e}",
            )

        try:
            amend_integer(
                integer=0,
                maximum_value=0,
                value_violation_action="error",
            )
        except Exception as e:
            self.assert_(
                False,
                f"Threw exception for value violation with exact maximum: {e}",
            )

        self.assertRaises(
            ValueError,
            amend_integer,
            integer=0,
            minimum_value=1,
            value_violation_action="error",
        )
        self.assertRaises(
            ValueError,
            amend_integer,
            integer=1,
            maximum_value=0,
            value_violation_action="error",
        )


if __name__ == "__main__":
    unittest.main()
