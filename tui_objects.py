"""Contain interface objects.
"""
import npyscreen
from task_objects import Rect
from functions import validate


class InpCoordForm(npyscreen.ActionForm):
    """Window, which appear in terminal, when we run "main.py"

    Args:
        npyscreen (npyscreen): npyscreen module
    """
    def create(self):
        self.add(npyscreen.Textfield, value="Input coords of First rect",
                 editable=False, max_width=30)
        self.nextrelx += 5
        self.x_1 = self.add(npyscreen.TitleText, name="x1:",
                            begin_entry_at=10, max_width=30)
        self.y_1 = self.add(npyscreen.TitleText, name="y1:",
                            begin_entry_at=10, max_width=30)
        self.x_2 = self.add(npyscreen.TitleText, name="x2:",
                            begin_entry_at=10, max_width=30)
        self.y_2 = self.add(npyscreen.TitleText, name="y2:",
                            begin_entry_at=10, max_width=30)
        self.nextrelx -= 5
        self.add(npyscreen.Textfield, value="Input coords of Second rect",
                 editable=False, max_width=30)
        self.nextrelx += 5
        self.x_3 = self.add(npyscreen.TitleText, name="x3:",
                            begin_entry_at=10, max_width=30)
        self.y_3 = self.add(npyscreen.TitleText, name="y3:",
                            begin_entry_at=10, max_width=30)
        self.x_4 = self.add(npyscreen.TitleText, name="x4:",
                            begin_entry_at=10, max_width=30)
        self.y_4 = self.add(npyscreen.TitleText, name="y4:",
                            begin_entry_at=10, max_width=30)
        self.nextrelx -= 5
        self.add(npyscreen.Textfield, value="Now press OK to calculate", editable=False, max_width=30)
        self.nextrelx += 5
        self.union = self.add(npyscreen.TitleText, name="Union:", value="0",
                              hidden=True, editable=False, max_width=30)
        self.intersection = self.add(npyscreen.TitleText, name="Intersection:", value="0",
                                     hidden=True, editable=False, max_width=30)

    def get_coords_vals(self) -> list[str]:
        """Place rect obj coord attributes in list and return.

        Returns:
            list[str]: list of coordinates.
        """
        return [self.x_1.value, self.y_1.value,
                self.x_2.value, self.y_2.value,
                self.x_3.value, self.y_3.value,
                self.x_4.value, self.y_4.value]

    def on_ok(self):
        """Launch when "ok" button pressed
        """
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
        """Launch when "cancel" button pressed
        """
        is_exit = npyscreen.notify_ok_cancel("Are you sure?",
                                             "Confirm Box", editw=1)
        if is_exit:
            self.parentApp.setNextForm(None)

class App(npyscreen.NPSAppManaged):
    """Application object.
    Contain Form we use to inp coords.

    Args:
        npyscreen (npyscreen): npyscreen module
    """
    def onStart(self):
        self.addForm("MAIN", InpCoordForm, name="Union / Intersection App", lines=20, columns=40)
