"""Independent arithmetic and source-integration checks for fracture lecture supplement."""
from __future__ import annotations

import math
import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
BOOK = ROOT / "books" / "materiales-mantenimiento-motores"


class FractureLectureTest(unittest.TestCase):
    def test_both_books_and_generator_are_wired(self) -> None:
        manual = (BOOK / "main.tex").read_text(encoding="utf-8")
        workbook = (BOOK / "problemas.tex").read_text(encoding="utf-8")
        generator = (BOOK / "scripts/build_companions.py").read_text(encoding="utf-8")
        self.assertIn(r"\input{content/fractura-docente-complemento.tex}", manual)
        self.assertIn(r"\input{content/fractura-problemas-docentes.tex}", workbook)
        self.assertIn("content/fractura-problemas-docentes.tex", generator)
        for file in ("fractura-docente-complemento.tex", "fractura-problemas-docentes.tex"):
            self.assertTrue((BOOK / "content" / file).is_file())

    def test_griffith_and_energy(self) -> None:
        sigma = math.sqrt(2 * 70e9 * 1.0 / (math.pi * .001)) / 1e6
        g_plane_stress = (30e6) ** 2 / 70e9
        g_plane_strain = g_plane_stress * (1 - .33**2)
        self.assertAlmostEqual(sigma, 6.675581178, places=7)
        self.assertAlmostEqual(g_plane_stress, 12857.142857, places=5)
        self.assertAlmostEqual(g_plane_strain, 11457.0, places=5)

    def test_finite_width_implicit_crack(self) -> None:
        def intensity(a: float) -> float:
            return 180 * math.sqrt(math.pi*a/math.cos(math.pi*a/.05))
        a = .005
        self.assertAlmostEqual(intensity(a), 23.132857408, places=6)
        self.assertLess(intensity(.009), 35.0)
        self.assertGreater(intensity(.010), 35.0)
        lo, hi = .009, .010
        for _ in range(80):
            mid = (lo + hi) / 2
            if intensity(mid) < 35:
                lo = mid
            else:
                hi = mid
        self.assertAlmostEqual((lo + hi) / 2, .00981707097746, places=11)

    def test_edge_polynomial_and_ct(self) -> None:
        x = .1
        y = 1.12 - .231*x + 10.55*x**2 - 21.72*x**3 + 30.39*x**4
        ki = y*100*math.sqrt(math.pi*.005)
        self.assertAlmostEqual(y, 1.183719, places=6)
        self.assertAlmostEqual(ki, 14.835717573, places=7)
        x = .4
        f = (2+x)*(.886+4.64*x-13.32*x**2+14.72*x**3-5.6*x**4)/(1-x)**1.5
        ki_ct = 4000/(.012*math.sqrt(.05))*f/1e6
        self.assertAlmostEqual(f, 7.278729982, places=7)
        self.assertAlmostEqual(ki_ct, 10.850490019, places=7)

    def test_thickness_is_not_only_criterion(self) -> None:
        scale_mm = 2.5*(40/950)**2*1000
        self.assertAlmostEqual(scale_mm, 4.432132964, places=7)
        self.assertGreater(5, scale_mm)
        self.assertLess(2, scale_mm)
        self.assertGreater(25-2, scale_mm)


if __name__ == "__main__":
    unittest.main()
