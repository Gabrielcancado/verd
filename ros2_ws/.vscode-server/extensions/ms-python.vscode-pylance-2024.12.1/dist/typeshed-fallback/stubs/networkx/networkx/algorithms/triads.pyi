from _typeshed import Incomplete
from collections.abc import Generator

from networkx.utils.backends import _dispatchable

@_dispatchable
def triadic_census(G, nodelist: Incomplete | None = None): ...
@_dispatchable
def is_triad(G): ...
@_dispatchable
def all_triplets(G): ...
@_dispatchable
def all_triads(G) -> Generator[Incomplete, None, None]: ...
@_dispatchable
def triads_by_type(G): ...
@_dispatchable
def triad_type(G): ...
@_dispatchable
def random_triad(G, seed: Incomplete | None = None): ...