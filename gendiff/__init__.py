"""Main package of gendiff."""
from gendiff.diff_builder.diff_generator import generate_diff

# Allow to use 'generate_diff' as a function.
__all__ = ('generate_diff',)  # noqa: WPS410
