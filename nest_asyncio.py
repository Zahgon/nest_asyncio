"""Patch asyncio to allow nested event loops."""

import asyncio
import asyncio.events as events
import os
import sys
import threading
from contextlib import contextmanager, suppress
from heapq import heappop


def apply(loop=None):
    """Patch asyncio to make its event loop reentrant."""
    pass


def _patch_asyncio():
    """Patch asyncio module to use pure Python tasks and futures."""
    pass


def _patch_policy():
    """Patch the policy to always return a patched loop."""
    pass


def _patch_loop(loop):
    """Patch loop to make it reentrant."""
    pass


def _patch_tornado():
    """
    If tornado is imported before nest_asyncio, make tornado aware of
    the pure-Python asyncio Future.
    """
    pass
