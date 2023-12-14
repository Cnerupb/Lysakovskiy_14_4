import npyscreen
from task_objects import Rect
from functions import validate


class InpCoordForm(npyscreen.ActionForm):
    def create(self):
        self.add(npyscreen.Textfield, value="Input coords of First rect", editable=False)
        self.nextrelx += 5
        self.x1 = self.add(npyscreen.TitleText, name="x1:")
        self.y1 = self.add(npyscreen.TitleText, name="y1:")
        self.x2 = self.add(npyscreen.TitleText, name="x2:")
        self.y2 = self.add(npyscreen.TitleText, name="y2:")
        self.nextrelx -= 5
        self.add(npyscreen.Textfield, value="Input coords of Second rect", editable=False)
        self.nextrelx += 5
        self.x3 = self.add(npyscreen.TitleText, name="x3:")
        self.y3 = self.add(npyscreen.TitleText, name="y3:")
        self.x4 = self.add(npyscreen.TitleText, name="x4:")
        self.y4 = self.add(npyscreen.TitleText, name="y4:")
        self.nextrelx -= 5
        self.add(npyscreen.Textfield, value="Now press OK to calculate", editable=False)
        self.nextrelx += 5
        self.union = self.add(npyscreen.TitleText, name="Union:", value="0",
                              hidden=True, editable=False)
        self.intersection = self.add(npyscreen.TitleText, name="Intersection:", value="0",
                                     hidden=True, editable=False)

    def get_coords_vals(self) -> list[str]:
        return [self.x1.value, self.y1.value,
                self.x2.value, self.y2.value,
                self.x3.value, self.y3.value,
                self.x4.value, self.y4.value]

    def on_ok(self):
        coords = self.get_coords_vals()
        if not validate(coords):
            npyscreen.notify_confirm("Invalid coords!", editw=1)
        else:
            coords = list(map(int, coords))
            left_top = coords[:2]
            right_bottom = coords[2:4]
            rect_1 = Rect(left_top, right_bottom)
            left_top = coords[4:6]
            right_bottom = coords[6:]
            rect_2 = Rect(left_top, right_bottom)
            self.union.set_value(str(rect_1.union(rect_2)))
            self.intersection.set_value(str(rect_1.intersection(rect_2)))
            self.union.hidden = False
            self.intersection.hidden = False
            self.union.update()
            self.intersection.update()

    def on_cancel(self):
        is_exit = npyscreen.notify_ok_cancel("Are you sure?", "Confirm Box", editw=1)
        if is_exit:
            self.parentApp.setNextForm(None)

class App(npyscreen.NPSAppManaged):
    def onStart(self):
        self.addForm("MAIN", InpCoordForm, name="Union / Intersection App")