import os
import sys
from gi.repository import Gtk, Adw
from .preferences import UserPreferences
from .app_types import NSFWOption


def resource_path(*parts):
    if getattr(sys, "frozen", False) and hasattr(sys, "_MEIPASS"):
        base = sys._MEIPASS
    else:
        base = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))
    return os.path.join(base, *parts)


PREFERENCES_UI_FILE = resource_path("data", "ui", "preferences.ui")


class PreferencesWindow(Adw.PreferencesWindow):
    __gtype_name__ = "PreferencesWindow"

    def __init__(self, **kwargs):
        super().__init__(**kwargs)

        builder = Gtk.Builder.new_from_file(PREFERENCES_UI_FILE)
        page = builder.get_object("preferences_page")
        self.nsfw_dropdown = builder.get_object("nsfw_dropdown")
        self.auto_reload_seconds = builder.get_object("auto_reload_seconds")

        self.settings = UserPreferences()
        self._nsfw_options = [option.value for option in NSFWOption]

        self.set_default_size(500, 300)
        self.set_search_enabled(False)

        self.add(page)

        model = Gtk.StringList.new(self._nsfw_options)
        self.nsfw_dropdown.set_model(model)

        current = self.settings.get_preference("nsfw_mode") or NSFWOption.BLOCK_NSFW
        try:
            index = self._nsfw_options.index(current)
        except ValueError:
            index = 0

        self.nsfw_dropdown.set_selected(index)
        self.nsfw_dropdown.connect("notify::selected", self.on_nsfw_change)

        seconds = self.settings.get_preference("auto_reload_interval")
        try:
            seconds = int(seconds) if seconds is not None else 30
        except Exception:
            seconds = 30

        if seconds < 1:
            seconds = 1

        self.auto_reload_seconds.set_value(seconds)
        self.auto_reload_seconds.connect("value-changed", self.on_auto_reload_seconds_change)

    def on_nsfw_change(self, dropdown, _):
        index = dropdown.get_selected()
        if index is None or index < 0 or index >= len(self._nsfw_options):
            return
        self.settings.set_preference("nsfw_mode", self._nsfw_options[index])

    def on_auto_reload_seconds_change(self, spin):
        seconds = int(spin.get_value())
        if seconds < 1:
            seconds = 1
        self.settings.set_preference("auto_reload_interval", seconds)