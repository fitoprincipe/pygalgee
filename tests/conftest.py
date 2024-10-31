"""Pytest session configuration."""

import pytest_gee


def pytest_configure() -> None:
    """Initialize earth engine according to the environment."""
    pytest_gee.init_ee_from_service_account()
