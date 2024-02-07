from flet import *

class Cadastro(UserControl):
    def __init__(self):
        pass
    
    def build(self):
        self.botao_adicionar_pessoa = TextButton(on_click=None, content=Row([Text("Adicionar Pessoa", text_align=TextAlign.CENTER)], alignment=CrossAxisAlignment.CENTER))
        self.botao_buscar_todas_pessoa = TextButton(text="Buscar Todas as Pessoa", on_click=None)
        self.botao_buscar_pessoa_email = TextButton(text="Buscar Pessoa por Email", on_click=None)
        self.botao_alterar_dados_pessoa = TextButton(text="Alterar Dados da Pessoa", on_click=None)
        self.botao_excluir_pessoa = TextButton(on_click=None, content=Row([Text("Excluir Pessoa", text_align=TextAlign.CENTER)]))

        self.container_botoes = Container(
            content=Column(
                controls=[
                    self.botao_adicionar_pessoa,
                    self.botao_buscar_todas_pessoa,
                    self.botao_buscar_pessoa_email,
                    self.botao_alterar_dados_pessoa,
                    self.botao_excluir_pessoa
                ], horizontal_alignment=MainAxisAlignment.CENTER
            ),
            bgcolor=colors.AMBER_100,
            width=300
        )

        self.container_informacoes = Container(
            content=Column(
                controls=[
                    self.container_botoes
                ]
            ),alignment=alignment.center
        )

        return self.container_informacoes

def main(page: Page):
    page.title = "Registro"
    page.theme_mode = ThemeMode.LIGHT
    cadastro = Cadastro()
    cadastro.build()
    page.add(
        cadastro.build()
    )
    page.update()

app(target=main)
