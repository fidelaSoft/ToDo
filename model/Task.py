
class Task:
    def __init__(self, id=0, title="", description="", responsible="", state=""):
        self.id = id
        self.title = title
        self.description = description
        self.responsible = responsible
        self.state = state

    # def change_state_to_proceso(self):
    #     self.state = "En Proceso"
    #
    # def change_state_to_terminado(self):
    #     self.state = "Finalizado"