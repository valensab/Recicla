# COMPLETE

from typing import Any, Callable, Dict, Literal, Mapping, NoReturn, Optional, Pattern, Protocol, Sequence, Tuple, TypeVar, Union, overload

from numpy.ma import MaskedArray

from matplotlib._typing import ArrayLike, Scalar, ndarray

_ColorLike = Union[
    str,
    Tuple[float, float, float],
    Tuple[float, float, float, float],
]


_C = TypeVar("_C", bound=Colormap)

class _ColorMapping(dict):
    def __init__(self, mapping) -> None: ...
    
    def __setitem__(self, key, value) -> None: ...
    
    def __delitem__(self, key)-> None: ...

class ColorConverter:
    colors: _ColorMapping = ...
    cache = ...
    to_rgb = ...
    to_rgba = ...
    to_rgba_array = ...

colorConverter: ColorConverter = ...

class Colormap:
    colorbar_extend: bool

    def __init__(self, name: str, N: int = ...) -> None: ...

    @overload
    def __call__(self, X: Scalar, alpha: Optional[float] = ..., bytes: bool = ...) -> Tuple[int, ...]: ... # TOOD: int or float?
    @overload
    def __call__(self, X: ArrayLike, alpha: Optional[float] = ..., bytes: bool = ...) -> ndarray: ...

    def is_gray(self) -> bool: ...

    def reversed(self: _C, name: Optional[str] = ...) -> _C: ...

    def set_bad(self, color: _ColorLike = ..., alpha: Optional[float] = ...) -> None: ...
    def set_over(self, color: _ColorLike = ..., alpha: Optional[float] = ...) -> None: ...
    def set_under(self, color: _ColorLike = ..., alpha: Optional[float] = ...) -> None: ...


class LinearSegmentedColormap(Colormap):
    def __init__(self, name: str, segmentdata: Mapping[str, Sequence[Tuple[float, float, float]]], N: int = ..., gamma: float = ...) -> None: ...

    @staticmethod
    def from_list(name: str, colors: ArrayLike, N: int = ..., gamma: float = ...) -> LinearSegmentedColormap: ...

    def set_gamma(self, gamma: float) -> None: ...


class ListedColormap(Colormap):
    # TODO: without N, colors must be len()-able
    def __init__(self, colors: Union[Sequence[_ColorLike], ArrayLike], name: str = ..., N: Optional[int] = ...) -> None: ...


class Normalize:
    def __init__(self, vmin: Optional[float] = ..., vmax: Optional[float] = ..., clip: bool = ...) -> None: ...

    @overload
    def __call__(self, value: Scalar, clip: Optional[bool] = ...) -> Scalar: ...
    @overload
    def __call__(self, value: ArrayLike, clip: Optional[bool] = ...) -> ndarray: ...

    # See np.asanyarray input type
    def autoscale(self, A: object) -> None: ...
    def autoscale_None(self, A: object) -> None: ...

    def inverse(self, value: ArrayLike) -> ndarray: ...

    @staticmethod
    def process_value(value: Union[Scalar, ArrayLike]) -> Tuple[MaskedArray, bool]: ...
    
    def scaled(self) -> bool: ...


class TwoSlopeNorm(Normalize):
    def __init__(self, vcenter: float, vmin: Optional[float] = ..., vmax: Optional[float] = ...) -> None: ...

class DivergingNorm(TwoSlopeNorm): ...

class LogNorm(Normalize): ...

class SymLogNorm(Normalize):
    def __init__(self, linthresh: float, linscale: float = ..., vmin: Optional[float] = ..., vmax: Optional[float] = ..., clip: bool = ..., *, base: Optional[float] = ...) -> None: ...

class PowerNorm(Normalize):
    def __init__(self, gamma: float, vmin: Optional[float] = ..., vmax: Optional[float] = ..., clip: bool = ...) -> None: ...

class BoundaryNorm(Normalize):
    def __init__(self, boundaries: ArrayLike, ncolors: int, clip: bool = ..., *, extend: Literal['neither', 'both', 'min', 'max'] = ...) -> None: ...

    def inverse(self, value: Any) -> NoReturn: ... # Always raises.

class NoNorm(Normalize): ...


class _BlendModeFunc(Protocol):
    def __call__(self, rgb: ArrayLike, illum: ArrayLike, **kwargs: Any) -> ndarray: ...

class LightSource:
    def __init__(
        self, 
        azdeg: float = ...,
        altdeg: float = ...,
        hsv_min_val: float = ...,
        hsv_max_val: float = ...,
        hsv_min_sat: float = ...,
        hsv_max_sat: float = ...
    ) -> None: ...

    @property
    def direction(self) -> ndarray: ...

    def blend_hsv(
        self,
        rgb: ndarray,
        intensity: ndarray,
        hsv_max_sat: Optional[float] = ...,
        hsv_max_val: Optional[float] = ...,
        hsv_min_val: Optional[float] = ...,
        hsv_min_sat: Optional[float] = ...
    ) -> ndarray: ...

    def blend_overlay(self, rgb: ndarray, intensity: ndarray) -> ndarray: ...
    def blend_soft_light(self, rgb: ndarray, intensity: ndarray) -> ndarray: ...

    def hillshade(self, elevation: ArrayLike, vert_exag: float = ..., dx: float = ..., dy: float = ..., fraction: float = ...) -> ndarray: ...

    def shade(
        self,
        data: ArrayLike,
        cmap: Colormap,
        norm: Optional[Normalize] = ...,
        blend_mode: Union[Literal['hsv', 'overlay', 'soft'], _BlendModeFunc] = ...,
        vmin: Optional[float] = ...,
        vmax: Optional[float] = ...,
        vert_exag: float = ...,
        dx: float = ...,
        dy: float = ...,
        fraction: float = ...,
        **kwargs: Any
    ) -> ndarray: ...

    def shade_normals(self, normals: ndarray, fraction: float = ...) -> ndarray: ...

    def shade_rgb(
        self,
        rgb: ArrayLike,
        elevation: ArrayLike,
        fraction: float = ...,
        blend_mode: Union[Literal['hsv', 'overlay', 'soft'], _BlendModeFunc] = ...,
        vert_exag: float = ...,
        dx: float = ...,
        dy: float = ...,
        **kwargs: Any
    ) -> ndarray: ...


def from_levels_and_colors(
    levels: ArrayLike,
    colors: Sequence[_ColorLike],
    extend: Literal['neither', 'min', 'max', 'both'] = ...
) -> Tuple[Colormap, Normalize]: ...

def hsv_to_rgb(hsv: ArrayLike) -> ndarray: ...
def rgb_to_hsv(arr: ArrayLike) -> ndarray: ...

def to_hex(c: Union[_ColorLike, MaskedArray], keep_alpha: bool = ...) -> str: ...
def to_rgb(c: Union[_ColorLike, MaskedArray]) -> Tuple[float, float, float]: ...
def to_rgba(c: Union[_ColorLike, MaskedArray], alpha: Optional[float] = ...) -> Tuple[float, float, float, float]: ...
def to_rgba_array(c: Any, alpha: Optional[float] = ...) -> ndarray: ...

def is_color_like(c: Any) -> bool: ...
def same_color(c1: Any, c2: Any) -> bool: ...

def makeMappingArray(N: int, data: Union[ArrayLike, Callable[[ndarray], ndarray]], gamma: float = ...) -> ndarray: ...
def get_named_colors_mapping() -> Dict[str, _ColorLike]: ...


# For backwards compatibility; not documented in the docs but explicitly written in the code.

cnames: Dict[str, str]
hexColorPattern: Pattern
def rgb2hex(c: Union[_ColorLike, MaskedArray], keep_alpha: bool = ...) -> str: ...
def hex2color(c: Union[_ColorLike, MaskedArray]) -> Tuple[float, float, float]: ...
