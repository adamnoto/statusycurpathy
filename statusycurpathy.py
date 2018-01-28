import sublime
import sublime_plugin


class StatusycurpathyCommand(sublime_plugin.EventListener):
  def on_activated(self, view):
    path = view.file_name()
    appvars = view.window().extract_variables()

    if path is not None and "folder" in appvars:
      folder = appvars["folder"]
      path = path.replace(folder, "")
      view.set_status("currentPath", path)
    else:
      view.set_status("currentPath", "[NOFILE]")