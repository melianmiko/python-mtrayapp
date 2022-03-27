from mtrayapp import TrayApplication, Menu, MenuItem

from PIL import Image, ImageDraw


def create_image(width, height, color1, color2):
    # Generate an image and draw a pattern
    image = Image.new('RGB', (width, height), color1)
    dc = ImageDraw.Draw(image)
    dc.rectangle(
        (width // 2, 0, width, height // 2),
        fill=color2)
    dc.rectangle(
        (0, height // 2, width // 2, height),
        fill=color2)

    return image


class TestMenu(Menu):
    def __init__(self, parent: TrayApplication):
        super().__init__()
        self.tray = parent

    def on_build(self):
        self.add_item("Disabled item", enabled=False)
        self.add_item("Default item", default=True, action=self.say_hello)
        self.add_separator()

        self.add_item("Test: legacy menu creation", self.set_menu_legacy_way)
        self.add_item("Test: set icon from PIL", self.set_icon_pil)
        self.add_item("Test: set icon from file path", self.set_icon_file)

    def set_icon_file(self):
        self.tray.icon = "icon.png"

    def set_icon_pil(self):
        self.tray.icon = create_image(64, 64, "red", "blue")

    def go_back(self):
        self.tray.menu = self

    def say_hello(self):
        print("Hello!")

    def set_menu_legacy_way(self):
        self.tray.menu = Menu(MenuItem("Go back", action=self.go_back))


# In order for the icon to be displayed, you must provide an icon
if __name__ == "__main__":
    tray = TrayApplication(
        'test name',
        icon=create_image(64, 64, 'black', 'white'))
    tray.menu = TestMenu(tray)
    tray.run()
