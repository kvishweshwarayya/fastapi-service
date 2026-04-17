# This file makes "routers" a package and allows easy imports.
# We can re-export routers here if we want.

from .user import router as gist_router

# Expose gist_router at the package level
__all__ = ["gist_router"]
