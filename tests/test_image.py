"""Test ui.Chart.image."""

import pygalgee as ui


class TestImage:
    """Test Image."""

    def test_image_series(self):
        """Test ui.Chart.image.series."""
        assert ui.Chart.image.series(test=True) == {"test": True}
