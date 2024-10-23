from typing import Any

import vapoursynth as vs

__all__ = [
    'create_blank_clip'
]

core = vs.core


def create_blank_clip(
    width: int = 1920, height: int = 1080,
    format: vs.VideoFormat = vs.YUV420P8,
    length: int = 1, **kwargs: Any
) -> vs.VideoNode:
    """Create a blank clip for testing purposes."""

    return core.std.BlankClip(width=width, height=height, format=format, length=length, **kwargs)
