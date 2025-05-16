from .data import ADDRESSES


def is_feasible(address: str) -> bool:
    """Return True if the address has data available."""
    return address in ADDRESSES
