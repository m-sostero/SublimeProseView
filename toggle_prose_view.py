# Credit to enteleform https://stackoverflow.com/users/4955183/enteleform 
# See http://stackoverflow.com/a/37872996/926810

import sublime, sublime_plugin

STORED_SETTINGS = {}

class toggle_prose_view(sublime_plugin.TextCommand):
	def run(self, edit):

		view = self.view
		settings = view.settings()

		if settings.get("is_widget"):
			return

		if view.file_name():
			viewID = view.file_name()
		else:
			viewID = str(view)

		global STORED_SETTINGS
		if not viewID in STORED_SETTINGS:
			STORED_SETTINGS[viewID] = {
				"custom_view_enabled": True,
				"font_size": settings.get("font_size"),
				"word_wrap": settings.get("word_wrap"),
				"wrap_width": settings.get("wrap_width"),
				"draw_centered": settings.get("draw_centered"),
				"line_padding_top": settings.get("line_padding_top"),
				"line_padding_bottom": settings.get("line_padding_bottom"),
			}

		storedSettings = STORED_SETTINGS[viewID]

		if storedSettings["custom_view_enabled"]:
			settings.set("font_size", 11)
			settings.set("word_wrap", True)
			settings.set("wrap_width", 69)
			settings.set("draw_centered", True)
			settings.set("line_padding_top", 1)
			settings.set("line_padding_bottom", 1)
		else:
			settings.set("font_size", storedSettings["font_size"])
			settings.set("word_wrap", storedSettings["word_wrap"])
			settings.set("wrap_width", storedSettings["wrap_width"])
			settings.set("draw_centered", storedSettings["draw_centered"])
			settings.set("line_padding_top", storedSettings["line_padding_top"])
			settings.set("line_padding_bottom", storedSettings["line_padding_bottom"])

		storedSettings["custom_view_enabled"] = not storedSettings["custom_view_enabled"]
