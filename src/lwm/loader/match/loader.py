from lwm.loader.match.model import MatchDefs


def matchdefs_from_data(data: dict) -> MatchDefs:
    match_data = data.get("match", None)
    if match_data is None:
        matches = MatchDefs()
    else:
        matches = MatchDefs(**match_data)

    return matches
