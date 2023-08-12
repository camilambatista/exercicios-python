from botcity.core import DesktopBot

class Bot(DesktopBot):
    def action(self, execution=None):

        # Opens the BotCity website.
        self.execute(r"C:\Users\Camila Batista\Desktop\Teams.lnk")

        if not self.find( "campoPesquisar", matching=0.97, waiting_time=10000):
            self.not_found("campoPesquisar")
        self.click()

        self.paste("Camila Batista")

        if not self.find( "pessoaPesquisada", matching=0.97, waiting_time=10000):
            self.not_found("pessoaPesquisada")
        self.click()

        if not self.find("campoMensagem", matching=0.97, waiting_time=10000):
            self.not_found("campoMensagem")
        self.click()

        self.paste("Teste robô python", wait=1000)
        self.enter()

    def not_found(self, label):
        print(f"Element not found: {label}")


if __name__ == '__main__':
    Bot.main()
