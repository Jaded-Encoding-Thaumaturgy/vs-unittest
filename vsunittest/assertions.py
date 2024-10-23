import vapoursynth as vs

from .core import VSTestCase
from .types import HoldsVideoFrameT

__all__ = [
    'assert_props_equal',
    'assert_planestats_equal'
]


def assert_props_equal(
    self, clip_a: HoldsVideoFrameT, clip_b: HoldsVideoFrameT,
    props: list[str] | None = None
) -> None:
    """Assert that two clips have equal properties."""

    if props is None:
        props = clip_a.get_frame(0).props.keys()

    for prop in props:
        self.assertEqual(
            clip_a.get_frame(0).props[prop],
            clip_b.get_frame(0).props[prop],
            f"Property '{prop}' does not match"
        )

def assert_planestats_equal(
    self, clip_a: HoldsVideoFrameT, clip_b: HoldsVideoFrameT,
    plane: int = 0, tolerance: float = 0.0
) -> None:
    """Assert that two clips have equal planestats for a specific plane within a given tolerance."""

    stats_a = self.core.std.ShufflePlanes(
        self.core.std.PlaneStats(clip_a, plane=plane),
        plane, vs.GRAY
    )

    stats_b = self.core.std.ShufflePlanes(
        self.core.std.PlaneStats(clip_b, plane=plane),
        plane, vs.GRAY
    )

    frame_a = stats_a.get_frame(0)
    frame_b = stats_b.get_frame(0)

    for stat in ['PlaneStatsMin', 'PlaneStatsMax', 'PlaneStatsAverage']:
        self.assertAlmostEqual(
            frame_a.props[stat],
            frame_b.props[stat],
            delta=tolerance,
            msg=f"{stat} for plane {plane} does not match within tolerance ({tolerance})"
        )

# Add these methods to VSTestCase
VSTestCase.assert_props_equal = assert_props_equal
VSTestCase.assert_planestats_equal = assert_planestats_equal
