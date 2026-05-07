from lwm.loader.notifier.model import NotifierDefs


def notifierdefs_from_data(data: dict):
    notifier_data = data.get("notifier", None)
    if notifier_data is None:
        notifier = NotifierDefs()
    else:
        notifier = NotifierDefs(**notifier_data)

    return notifier
