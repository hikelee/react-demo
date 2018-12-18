def init_models(sender, **kwargs):
    from snippets.models.field import init_fields
    from snippets.models.contenttype import init_contenttype
    type_map = init_contenttype()
    init_fields(type_map)