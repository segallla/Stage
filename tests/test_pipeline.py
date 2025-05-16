import unittest
from bess.pipeline import analyze_address

ADDRESS1 = "44933 Fern Ave, Lancaster, CA 93534"
ADDRESS2 = "456 Elm St, Compton, CA 90220"
ADDRESS3 = "5300 Sheila St, Commerce, CA 90040"


class TestPipeline(unittest.TestCase):
    def test_address1_feasibility(self):
        result = analyze_address(ADDRESS1)
        feas = result["STEP6_INTERCONNECTION_FEASIBILITY"]
        self.assertTrue(feas["feasible"])
        self.assertEqual(feas["recommended_max_MW"], 5)
        bess = result["STEP7_OPTIMAL_BESS_CONFIG"]
        self.assertEqual(bess["power_MW"], 4.9)
        self.assertEqual(bess["duration_hr"], 4)

    def test_address2_feasibility(self):
        result = analyze_address(ADDRESS2)
        feas = result["STEP6_INTERCONNECTION_FEASIBILITY"]
        self.assertFalse(feas["feasible"])
        self.assertEqual(feas["recommended_max_MW"], 0.5)
        bess = result["STEP7_OPTIMAL_BESS_CONFIG"]
        self.assertEqual(bess["power_MW"], 0.5)
        self.assertEqual(bess["duration_hr"], 4)

    def test_address3_feasibility(self):
        result = analyze_address(ADDRESS3)
        feas = result["STEP6_INTERCONNECTION_FEASIBILITY"]
        self.assertTrue(feas["feasible"])
        self.assertEqual(feas["recommended_max_MW"], 5)
        bess = result["STEP7_OPTIMAL_BESS_CONFIG"]
        self.assertEqual(bess["power_MW"], 4.9)
        self.assertEqual(bess["duration_hr"], 4)


if __name__ == "__main__":
    unittest.main()
