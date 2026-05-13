from lwm.model.cursor import CursorDefs


def cursordefs_from_data(data: dict) -> CursorDefs:
    cursor_data = data.get("cursor", {})
    cursor = CursorDefs(**cursor_data)
    return cursor
