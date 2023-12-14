"""Contain objects solving task.
"""


class Rect:
    """Objects solving task
    """
    def __init__(self,
                 left_top: tuple[int, int],
                 right_bottom: tuple[int, int]):
        # left top
        self.x_1 = left_top[0]
        self.y_1 = left_top[1]
        # right bottom
        self.x_2 = right_bottom[0]
        self.y_2 = right_bottom[1]
        # Normalization
        if self.x_1 > self.x_2:
            self.x_1, self.x_2 = self.x_2, self.x_1
        if self.y_1 > self.y_2:
            self.y_1, self.y_2 = self.y_2, self.y_1

    @property
    def width(self) -> int:
        """Calculate width

        Returns:
            int: width
        """
        return self.x_2 - self.x_1

    @property
    def height(self) -> int:
        """Calculate height

        Returns:
            int: height
        """
        return self.y_2 - self.y_1

    @property
    def area(self) -> int:
        """Calculate area of rect

        Returns:
            int: area
        """
        return self.width * self.height

    def intersection(self, rect) -> int:
        """Count area of intersection with other rect

        Args:
            rect (Rect): Rect object

        Returns:
            int: area
        """
        def get_len(c_1_1, c_1_2, c_2_1, c_2_2):
            return max(0, min(c_1_2, c_2_2) - max(c_1_1, c_2_1))
        width = get_len(self.x_1, self.x_2, rect.x1, rect.x2)
        height = get_len(self.y_1, self.y_2, rect.y1, rect.y2)
        return width * height

    def union(self, rect):
        """Count area of union with other rect

        Args:
            rect (Rect): Rect object

        Returns:
            int: area
        """
        return (self.area + rect.area) - 2*self.intersection(rect)
