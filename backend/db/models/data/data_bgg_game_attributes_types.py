from typing import List


class KeysBggGameAttributesTypes:
    DESIGNERS = "designers"
    ARTISTS = "artists"
    PUBLISHERS = "publishers"
    BOARDGAME_IMPLEMENTATIONS = "boardgame_implementations"
    BOARDGAME_CATEGORIES = "boardgame_categories"
    BOARDGAME_MECHANICS = "boardgame_mechanics"
    BOARDGAME_FAMILY = "boardgame_family"
    BOARDGAME_VERSIONS = "boardgame_versions"
    BOARDGAME_EXPANSIONS = "boardgame_expansions"
    MARKETPLACE = "marketplace"


class DataBggGameAttributesTypes(KeysBggGameAttributesTypes):
    @staticmethod
    def data() -> List[dict]:
        k = KeysBggGameAttributesTypes
        return [
            {"attribute_type_index": 1, "attribute_type_name": k.DESIGNERS},
            {"attribute_type_index": 2, "attribute_type_name": k.ARTISTS},
            {"attribute_type_index": 3, "attribute_type_name": k.PUBLISHERS},
            {"attribute_type_index": 4, "attribute_type_name": k.BOARDGAME_IMPLEMENTATIONS},
            {"attribute_type_index": 5, "attribute_type_name": k.BOARDGAME_CATEGORIES},
            {"attribute_type_index": 6, "attribute_type_name": k.BOARDGAME_MECHANICS},
            {"attribute_type_index": 7, "attribute_type_name": k.BOARDGAME_FAMILY},
            {"attribute_type_index": 8, "attribute_type_name": k.BOARDGAME_VERSIONS},
            {"attribute_type_index": 9, "attribute_type_name": k.BOARDGAME_EXPANSIONS},
            {"attribute_type_index": 10, "attribute_type_name": k.MARKETPLACE}]
