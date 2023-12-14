class Rect:
    def __init__(self,
                 left_top: tuple[int, int],
                 right_bottom: tuple[int, int],
                 *args, **kwargs):
        # left top
        self.x1 = left_top[0]
        self.y1 = left_top[1]
        # right bottom
        self.x2 = right_bottom[0]
        self.y2 = right_bottom[1]
        # Normalization
        if self.x1 > self.x2:
            self.x1, self.x2 = self.x2, self.x1
        if self.y1 > self.y2:
            self.y1, self.y2 = self.y2, self.y1

    @property
    def width(self) -> int:
        return self.x2 - self.x1

    @property
    def height(self) -> int:
        return self.y2 - self.y1
    
    @property
    def area(self) -> int:
        return self.width * self.height

    def intersection(self, rect) -> int:
        def get_len(a, b, c, d):
            return max(0, min(b, d) - max(a, c))
        width = get_len(self.x1, self.x2, rect.x1, rect.x2)
        height = get_len(self.y1, self.y2, rect.y1, rect.y2)
        return width * height

    def union(self, rect):
        return (self.area + rect.area) - 2*self.intersection(rect)





