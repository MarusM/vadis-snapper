LANGUAGE = "en"

TEXT = {

    "button.snap": "SNAP",

    "button.folder": "Open Screenshot Folder",

    "group.capture": "Capture Mode",

    "mode.window": "Active Window",

    "mode.monitor": "Active Monitor",

    "mode.desktop": "Entire Desktop",

    "status.ready": "Status  : Ready",

    "status.capturing": "Status  : Capturing...",

    "status.saved": "Status  : Screenshot saved",

    "status.failed": "Status  : Capture failed"

}


def tr(key):

    return TEXT.get(key, key)