"""Regressions for the independently derived Materials teacher-bridge examples.

These checks validate arithmetic and source integration, not the physical
calibration of empirical fatigue/creep models or an official exam answer.
"""
from __future__ import annotations

import math
import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
BOOK = ROOT / "books" / "materiales-mantenimiento-motores"


class MaterialsTeachingBridgeTest(unittest.TestCase):
    def test_sources_are_integrated(self) -> None:
        manual = (BOOK / "main.tex").read_text(encoding="utf-8")
        problems = (BOOK / "problemas.tex").read_text(encoding="utf-8")
        builder = (BOOK / "scripts/build_companions.py").read_text(
            encoding="utf-8"
        )
        self.assertIn(r"\input{content/refuerzo-docente-materiales.tex}", manual)
        self.assertIn(r"\input{content/problemas-puente-profesor.tex}", problems)
        self.assertIn("content/problemas-puente-profesor.tex", builder)
        self.assertTrue((BOOK / "content/refuerzo-docente-materiales.tex").is_file())
        self.assertTrue((BOOK / "content/problemas-puente-profesor.tex").is_file())

    def test_inverse_stress_concentration(self) -> None:
        target_kt = 0.75 * 2.50
        radius_ratio = 0.25 + (1.90 - target_kt) * 0.15 / 0.30
        self.assertAlmostEqual(target_kt, 1.875)
        self.assertAlmostEqual(radius_ratio * 20, 5.25)

    def test_sn_interpolation(self) -> None:
        b = math.log(400 / 720) / math.log(1e6 / 1e3)
        stress = 720 * (1e4 / 1e3) ** b
        cycles = 1e3 * (500 / 720) ** (1 / b)
        self.assertAlmostEqual(b, -0.085090835, places=8)
        self.assertAlmostEqual(stress, 591.890898, places=5)
        self.assertAlmostEqual(cycles, 72627.197, places=2)

    def test_load_to_stress_and_goodman(self) -> None:
        diameter, lever = 0.02, 0.10
        geometry = 4 / (math.pi * diameter**2) + 32 * lever / (
            math.pi * diameter**3
        )
        se = 400 / (1.15 * 1.25 * 1.08 * 1.05 * 1.20)
        fully_reversed_force = se * 1e6 / geometry
        max_repeated_force = (2 * se * 800 / (se + 800)) * 1e6 / geometry
        self.assertAlmostEqual(se, 204.483296, places=5)
        self.assertAlmostEqual(fully_reversed_force, 1566.837125, places=4)
        self.assertAlmostEqual(max_repeated_force, 2495.750213, places=4)

    def test_paris_and_critical_size(self) -> None:
        c = 1e-11
        n_zero = math.log(4) / (c * math.pi * 150**2)
        n_tension = math.log(4) / (c * math.pi * 90**2)
        n_compression_nominal = math.log(4) / (c * math.pi * 190**2)
        ac = (35 / 150) ** 2 / math.pi
        kmax = 150 * math.sqrt(math.pi * 0.004)
        self.assertAlmostEqual(n_zero, 1961205.3347, places=3)
        self.assertAlmostEqual(n_tension, 5447792.5964, places=3)
        self.assertAlmostEqual(n_compression_nominal, 1222357.8956, places=3)
        self.assertLess(kmax, 35)
        self.assertGreater(ac, 0.004)

    def test_centrifugal_creep_and_temperature_ratio(self) -> None:
        omega = 2 * math.pi * 9000 / 60
        sigma_mpa = 8500 * 0.08 * omega**2 * 0.17 / 1e6
        remaining_strain = 0.16 / 80 - sigma_mpa / 200000
        t1_s = remaining_strain / 1e-8
        temperature_factor = math.exp(
            200000 / 8.314462618 * (1 / 990 - 1 / 1000)
        )
        self.assertGreater(remaining_strain, 0)
        self.assertAlmostEqual(sigma_mpa, 102.683364, places=5)
        self.assertAlmostEqual(t1_s / 3600, 41.293977, places=5)
        self.assertAlmostEqual(t1_s * temperature_factor / 3600, 52.651310, places=5)


if __name__ == "__main__":
    unittest.main()
