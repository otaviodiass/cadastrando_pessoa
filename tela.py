from flet import *

class Cadastro(UserControl):
    def __init__(self, page: Page):
        self.page = page
    
    def build(self):

        self.page.navigation_bar = NavigationBar(
            destinations=[
                NavigationDestination(label='Adicionar Pessoa'),
                NavigationDestination(label='Buscar Todas as Pessoa'),
                NavigationDestination(label='Buscar Pessoa por Email'),
                NavigationDestination(label='Alterar Dados da Pessoa'),
                NavigationDestination(label='Excluir Pessoa'),
            ]
        )

        self.container_botoes = Container(
            content=Column(
                controls=[
                   Text("Hello", text_align=TextAlign.CENTER)
                ], horizontal_alignment=MainAxisAlignment.CENTER
            ),
            bgcolor=colors.AMBER_100
        )

        self.container_informacoes = Container(
            content=Column(
                controls=[
                    self.container_botoes
                ]
            ), alignment=alignment.center
        )

        return self.container_informacoes

def main(page: Page):
    page.title = "Registro"
    page.theme_mode = ThemeMode.LIGHT
    
    cadastro = Cadastro(page)
    cadastro.build()
    page.add(
        cadastro.build()
    )
    page.update()

app(target=main)
