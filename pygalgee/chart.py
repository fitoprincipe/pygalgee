"""Chart module to hold all methods."""

from .image import Image
from .table import Table


class Chart:
    """Chart class.

    A namespace to mimic Earth Engine structure.
    """

    class image:
        """Image class."""

        @staticmethod
        def series(**kwargs):
            """Generates a Chart from an ImageCollection.

            Plots derived values of each band in a region across images.
            Usually a time series.
            """
            return Image.series(**kwargs)

    class feature:
        """Feature class."""

        @staticmethod
        def byProperty(**kwargs):
            """Generates a Chart from a set of features.

            Plots property values of one or more features. All properties
            except seriesProperty are included on the x-axis by default.
            """
            return Table.byProperty(**kwargs)
