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
    def __init__(self):
        super().__init__()

    def on_build(self):
        self.add_item("Disabled item", enabled=False)
        self.add_item("Default item", default=True, action=self.say_hello)
        self.add_submenu("Submenu", TestSubmenu())
        self.add_separator()

        self.add_item("Test: legacy menu creation", self.set_menu_legacy_way)
        self.add_item("Test: set icon from PIL", self.set_icon_pil)
        self.add_item("Test: set icon from file path", self.set_icon_file)
        self.add_item("Test: notify", lambda: self.application.notify("Hello", "Wooorld"))
        self.add_item("Test: message box", self.message)
        self.add_item("Test: error box", self.error)
        self.add_item("Test: confirm box", self.confirm)

    def message(self):
        self.application.message_box("I'm message", "Test", self.msg_callback)

    def error(self):
        self.application.message_box("I'm error", "Test", self.msg_callback)

    def confirm(self):
        self.application.confirm_box("Do you like pancakes?", "Test", self.confirm_callback)

    @staticmethod
    def msg_callback():
        print("Box closed")

    def confirm_callback(self, result):
        if result:
            self.application.message_box("I'm too", "")
        else:
            self.application.message_box("...", "")

    def set_icon_file(self):
        self.application.icon = "icon.png"

    def set_icon_pil(self):
        self.application.icon = create_image(64, 64, "red", "blue")

    def go_back(self):
        self.application.menu = self

    @staticmethod
    def say_hello():
        print("Hello!")

    def set_menu_legacy_way(self):
        self.application.menu = Menu(MenuItem("Go back", action=self.go_back))


class TestSubmenu(Menu):
    def on_build(self):
        self.add_item("Hello, i'm submenu :-)")


# In order for the icon to be displayed, you must provide an icon
if __name__ == "__main__":
    tray = TrayApplication(
        'test name',
        menu=TestMenu(),
        icon=create_image(64, 64, 'black', 'white'))
    tray.run()
