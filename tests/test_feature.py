"""Test table charting."""

import pygalgee as ui


class TestTable:
    """Test Table (feature)."""

    def test_feature_byproperty(self):
        """Test feature.byProperty method."""
        assert ui.Chart.feature.byProperty(test=True) == {"test": True}
