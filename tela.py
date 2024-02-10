from flet import *

class Cadastro(UserControl):
    def __init__(self, page: Page):
        self.page = page
    
    def build(self):

        def verifica_conteudo_tela():
            if len(self.container_informacoes.content.controls) > 0:
                self.container_informacoes.content.controls.pop()
                self.page.update()

        def montar_tela(event):
            destino = event.data
            destino = int(destino)

            if destino == 0:
                print("Adicionar Pessoa")
                verifica_conteudo_tela()
                self.container_informacoes.content.controls.append(self.container_adicionar_pessoa)
                self.page.update()
            elif destino == 1:
                print("Buscar Todas as Pessoa")
                verifica_conteudo_tela()
                self.container_informacoes.content.controls.append(self.container_buscar_todas_pessoas)
                self.page.update()
            elif destino == 2:
                print("Buscar Pessoa por Email")
                verifica_conteudo_tela()
                self.container_informacoes.content.controls.append(self.container_buscar_pessoa_por_email)
                self.page.update()
            elif destino == 3:
                print("Alterar Dados da Pessoa")
                verifica_conteudo_tela()
                self.container_informacoes.content.controls.append(self.container_alterar_dados)
                self.page.update()
            else:
                print("Excluir Pessoa")
                verifica_conteudo_tela()
                self.container_informacoes.content.controls.append(self.container_excluir_pessoa)
                self.page.update()

        self.page.navigation_bar = NavigationBar(
            destinations=[
                NavigationDestination(label='Adicionar Pessoa', icon=icons.PERSON_ADD_ROUNDED),
                NavigationDestination(label='Buscar Todas as Pessoa', icon=icons.PERSON_SEARCH_ROUNDED),
                NavigationDestination(label='Buscar Pessoa por Email', icon=icons.CONTENT_PASTE_SEARCH_ROUNDED),
                NavigationDestination(label='Alterar Dados da Pessoa', icon=icons.PERSON_ROUNDED),
                NavigationDestination(label='Excluir Pessoa', icon=icons.PERSON_REMOVE_ALT_1_ROUNDED),
            ], on_change=montar_tela
        )

        self.container_adicionar_pessoa = Container(
            content=Column(
                controls=[
                     Text("Adicionar Pessoa", text_align=TextAlign.CENTER, size=30, weight=FontWeight.BOLD),
                     TextField(label="Nome", hint_text="Entre com seu Nome aqui!"),
                     TextField(label="Idade", hint_text="Entre com sua Idade aqui!"),
                     TextField(label="Altura", hint_text="Entre com sua Altura aqui!"),
                     TextField(label="Email", hint_text="Entre com seu Email aqui!"),
                     ElevatedButton(content=Row([Text("Adicionar", size=20)], alignment=MainAxisAlignment.CENTER), width=180, height=50, on_click=None)
                ], alignment=MainAxisAlignment.CENTER, horizontal_alignment=CrossAxisAlignment.CENTER
            ), width=480
        )

        self.container_buscar_todas_pessoas = Container(
            content=Column(
                controls=[
                    Text("Buscar Todas as Pessoa", text_align=TextAlign.CENTER, size=30, weight=FontWeight.BOLD),
                    ElevatedButton(content=Row([Text("Buscar", size=20)], alignment=MainAxisAlignment.CENTER), width=180, height=50, on_click=None)                ], alignment=MainAxisAlignment.CENTER, horizontal_alignment=CrossAxisAlignment.CENTER
            ), width=480
        )

        self.container_buscar_pessoa_por_email = Container(
            content=Column(
                controls=[
                    Text("Buscar Pessoa por Email", text_align=TextAlign.CENTER, size=30, weight=FontWeight.BOLD),
                    TextField(label="Email", hint_text="Digite o email aqui!"),
                    ElevatedButton(content=Row([Text("Buscar", size=20)], alignment=MainAxisAlignment.CENTER), width=180, height=50, on_click=None)
                ], alignment=MainAxisAlignment.CENTER, horizontal_alignment=CrossAxisAlignment.CENTER
            ), width=480
        )

        self.container_alterar_dados = Container(
            content=Column(
                controls=[
                    Text("Alterar Dados da Pessoa", text_align=TextAlign.CENTER, size=30, weight=FontWeight.BOLD),
                    TextField(label="Email", hint_text="Digite o email aqui!"),
                    ElevatedButton(content=Row([Text("Buscar", size=20)], alignment=MainAxisAlignment.CENTER), width=180, height=50, on_click=None)
                ], alignment=MainAxisAlignment.CENTER, horizontal_alignment=CrossAxisAlignment.CENTER
            ), width=480
        )

        self.container_excluir_pessoa = Container(
            content=Column(
                controls=[
                    Text("Excluir Pessoa", text_align=TextAlign.CENTER, size=30, weight=FontWeight.BOLD),
                    TextField(label="Email", hint_text="Digite o email aqui!"),
                    ElevatedButton(content=Row([Text("Excluir", size=20)], alignment=MainAxisAlignment.CENTER), width=180, height=50, on_click=None)
                ], alignment=MainAxisAlignment.CENTER, horizontal_alignment=CrossAxisAlignment.CENTER
            ), width=480
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
