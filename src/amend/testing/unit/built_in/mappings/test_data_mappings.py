import unittest

from amend.built_in.mappings.data_mappings import amend_mutable_data_mapping


class TestAmendMutableDataMapping(unittest.TestCase):
    def test_no_amendment_needed(
        self,
    ):
        try:
            amend_mutable_data_mapping(
                mutable_data_mapping={
                    "a": 1,
                    "b": 2,
                }
            )
        except Exception as e:
            self.assert_(
                False,
                f"Threw exception when no amendment was needed: {e}",
            )

    def test_type_mismatch(
        self,
    ):
        data_mapping = (
            ("a", 1),
            ("b", 2),
        )
        expected_result = {
            "a": 1,
            "b": 2,
        }

        try:
            result = amend_mutable_data_mapping(mutable_data_mapping=data_mapping)
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
            amend_mutable_data_mapping,
            mutable_data_mapping=data_mapping,
            type_mismatch_action="error",
        )

    def test_cast_error(
        self,
    ):
        self.assertRaises(
            TypeError,
            amend_mutable_data_mapping,
            mutable_data_mapping=None,
        )
        self.assertRaises(
            ValueError,
            amend_mutable_data_mapping,
            mutable_data_mapping=None,
            value_on_cast_error=1,
        )
        self.assertRaises(
            ValueError,
            amend_mutable_data_mapping,
            mutable_data_mapping=None,
            value_on_cast_error=(1, 2),
        )
        self.assertRaises(
            ValueError,
            amend_mutable_data_mapping,
            mutable_data_mapping=None,
            value_on_cast_error=(
                ("a", 1),
                2,
            ),
        )

        try:
            result = amend_mutable_data_mapping(
                mutable_data_mapping=None,
                value_on_cast_error=(
                    ("a", 1),
                    ("b", 2),
                ),
            )
        except Exception as e:
            self.assert_(
                False,
                f"Threw exception when value on cast error was valid: {e}",
            )

        self.assertEqual(
            result,
            {
                "a": 1,
                "b": 2,
            },
        )

    def test_case_with_length_violation(
        self,
    ):
        data_mapping = {
            "a": 1,
            "b": 2,
        }

        try:
            amend_mutable_data_mapping(
                mutable_data_mapping=data_mapping,
                length_violation_action="error",
            )
        except Exception as e:
            self.assert_(
                False,
                f"Threw exception for length violation without defined limits: {e}",
            )

        try:
            amend_mutable_data_mapping(
                mutable_data_mapping=data_mapping,
                minimum_length=0,
                length_violation_action="error",
            )
        except Exception as e:
            self.assert_(
                False,
                f"Threw exception for length violation with minimum 0 length: {e}",
            )

        try:
            amend_mutable_data_mapping(
                mutable_data_mapping=data_mapping,
                maximum_length=len(data_mapping),
                length_violation_action="error",
            )
        except Exception as e:
            self.assert_(
                False,
                "Threw exception for length violation with exact maximum length",
            )

        self.assertRaises(
            ValueError,
            amend_mutable_data_mapping,
            mutable_data_mapping=data_mapping,
            minimum_length=len(data_mapping) + 1,
            length_violation_action="error",
        )
        self.assertRaises(
            ValueError,
            amend_mutable_data_mapping,
            mutable_data_mapping=data_mapping,
            maximum_length=len(data_mapping) - 1,
            length_violation_action="error",
        )


if __name__ == "__main__":
    unittest.main()
