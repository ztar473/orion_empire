class Id():
    id = 0

    # @staticmethod
    def prochainid():
        Id.id += 1
        str_id = "id_" + str(Id.id)
        return str_id
