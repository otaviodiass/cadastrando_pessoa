from flet import *
from typing import List, Dict
from requisicoes import Requisicoes

class Cadastro(UserControl):
    def __init__(self, page: Page):
        self.page = page
        self.requisicoes = Requisicoes()
    
    def verifica_conteudo_tela(self):
        if len(self.container_informacoes.content.controls) > 0:
            self.container_informacoes.content.controls.pop()
            self.page.update()

    def formatar_dados(self, lista: List) -> Dict:
        dados_dict = {
            'nome': lista[0].value,
            'idade': lista[1].value,
            'altura': lista[2].value,
            'email': lista[3].value
        }
        return dados_dict
    
    def limpar_campos(self, container: Container):
        for i in container.content.controls:
            if isinstance(i, TextField):
                i.value = None
    

    def build(self):

        def adicionar_pessoa_valores(event):
            self.verifica_conteudo_tela()
            lista_valores: List = self.container_adicionar_pessoa.content.controls.copy()
            lista_valores.pop(0)
            lista_valores.pop()
            dados_formatados = self.formatar_dados(lista_valores)
            resposta = self.requisicoes.requisitar_adicionar_pessoa(dados_formatados)
            tabela = DataTable(
                columns=[
                    DataColumn(Text("Nome")),
                    DataColumn(Text("Idade")),
                    DataColumn(Text("Altura")),
                    DataColumn(Text("Email")),
                ],
                rows=[
                    DataRow(
                        cells=[
                            DataCell(Text(resposta['nome'])),
                            DataCell(Text(resposta['idade'])),
                            DataCell(Text(resposta['altura'])),
                            DataCell(Text(resposta['email']))
                        ]
                    )
                ]
            )
            self.container_informacoes.content.controls.append(tabela)
            self.page.update()
            self.limpar_campos(self.container_adicionar_pessoa)

        def buscar_todas_pessoas(event):
            self.verifica_conteudo_tela()
            resposta = self.requisicoes.requisitar_todas_pessoas()
            tabela = DataTable(
                columns=[
                    DataColumn(Text("Nome")),
                    DataColumn(Text("Idade")),
                    DataColumn(Text("Altura")),
                    DataColumn(Text("Email")),
                ]
            )

            for pessoa in resposta:
                data = DataRow(
                            cells=[
                                DataCell(Text(pessoa['nome'])),
                                DataCell(Text(pessoa['idade'])),
                                DataCell(Text(pessoa['altura'])),
                                DataCell(Text(pessoa['email']))
                            ]
                        )
                tabela.rows.append(data)
            
            self.container_informacoes.content.controls.append(tabela)
            self.page.update()

        def buscar_pessoa_por_email(event):
            self.verifica_conteudo_tela()
            email_value: List = self.container_buscar_pessoa_por_email.content.controls.copy()
            email_value.pop(0)
            email_value.pop()
            email: str = email_value[0].value
            resposta = self.requisicoes.requisitar_pessoa_por_email(email)
            
            if resposta['status']:
                tabela = DataTable(
                    columns=[
                        DataColumn(Text("Nome")),
                        DataColumn(Text("Idade")),
                        DataColumn(Text("Altura")),
                        DataColumn(Text("Email")),
                    ],
                    rows=[
                        DataRow(
                            cells=[
                                DataCell(Text(resposta['dados']['nome'])),
                                DataCell(Text(resposta['dados']['idade'])),
                                DataCell(Text(resposta['dados']['altura'])),
                                DataCell(Text(resposta['dados']['email']))
                            ]
                        )
                    ]
                )
                self.container_informacoes.content.controls.append(tabela)
            else:
                self.container_informacoes.content.controls.append(Text(resposta['mensagem'], text_align=TextAlign.CENTER, size=30, weight=FontWeight.BOLD))
            
            self.page.update()
            self.limpar_campos(self.container_buscar_pessoa_por_email)
        
        def alterar_dados(event):
            self.verifica_conteudo_tela()
            lista_valores: List = self.container_alterar_dados.content.controls.copy()
            lista_valores.pop(0)
            lista_valores.pop(1)
            lista_valores.pop()
            email: str = lista_valores.pop(0).value
            dados_formatados = self.formatar_dados(lista_valores)
            resposta = self.requisicoes.requisitar_alterar_dados(email, dados_formatados)
            
            if resposta['status']:
                tabela = DataTable(
                    columns=[
                        DataColumn(Text("Nome")),
                        DataColumn(Text("Idade")),
                        DataColumn(Text("Altura")),
                        DataColumn(Text("Email")),
                    ],
                    rows=[
                        DataRow(
                            cells=[
                                DataCell(Text(resposta['dados']['nome'])),
                                DataCell(Text(resposta['dados']['idade'])),
                                DataCell(Text(resposta['dados']['altura'])),
                                DataCell(Text(resposta['dados']['email']))
                            ]
                        )
                    ]
                )
                self.container_informacoes.content.controls.append(tabela)
            else:
                self.container_informacoes.content.controls.append(Text(resposta['mensagem'], text_align=TextAlign.CENTER, size=30, weight=FontWeight.BOLD))
            
            self.page.update()
            self.limpar_campos(self.container_alterar_dados)
        
        def excluir_pessoa(event):
            self.verifica_conteudo_tela()
            email_value: List = self.container_excluir_pessoa.content.controls.copy()
            email_value.pop(0)
            email_value.pop()
            email = email_value[0].value
            resposta = self.requisicoes.requisitar_deletar_pessoa(email)

            if resposta['status']:
                self.container_informacoes.content.controls.append(Text(resposta['mensagem'], text_align=TextAlign.CENTER, size=30, weight=FontWeight.BOLD))
            else:
                self.container_informacoes.content.controls.append(Text(resposta['mensagem'], text_align=TextAlign.CENTER, size=30, weight=FontWeight.BOLD))
            
            self.page.update()
            self.limpar_campos(self.container_excluir_pessoa)

        def montar_tela(event):
            destino = event.data
            destino = int(destino)

            if destino == 0:
                self.verifica_conteudo_tela()
                self.container_informacoes.content.controls.append(self.container_adicionar_pessoa)
                self.page.update()
            elif destino == 1:
                self.verifica_conteudo_tela()
                self.container_informacoes.content.controls.append(self.container_buscar_todas_pessoas)
                self.page.update()
            elif destino == 2:
                self.verifica_conteudo_tela()
                self.container_informacoes.content.controls.append(self.container_buscar_pessoa_por_email)
                self.page.update()
            elif destino == 3:
                self.verifica_conteudo_tela()
                self.container_informacoes.content.controls.append(self.container_alterar_dados)
                self.page.update()
            else:
                self.verifica_conteudo_tela()
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
                    TextField(label="Nome", hint_text="Entre com seu Nome aqui!", value=None),
                    TextField(label="Idade", hint_text="Entre com sua Idade aqui!", value=None),
                    TextField(label="Altura", hint_text="Entre com sua Altura aqui!", value=None),
                    TextField(label="Email", hint_text="Entre com seu Email aqui!", value=None),
                    ElevatedButton(content=Row([Text("Adicionar", size=20)], alignment=MainAxisAlignment.CENTER), width=180, height=50, on_click=adicionar_pessoa_valores)
                ], alignment=MainAxisAlignment.CENTER, horizontal_alignment=CrossAxisAlignment.CENTER
            ), width=480
        )

        self.container_buscar_todas_pessoas = Container(
            content=Column(
                controls=[
                    Text("Buscar Todas as Pessoa", text_align=TextAlign.CENTER, size=30, weight=FontWeight.BOLD),
                    ElevatedButton(content=Row([Text("Buscar", size=20)], alignment=MainAxisAlignment.CENTER), width=180, height=50, on_click=buscar_todas_pessoas)                
                ], alignment=MainAxisAlignment.CENTER, horizontal_alignment=CrossAxisAlignment.CENTER
            ), width=480
        )

        self.container_buscar_pessoa_por_email = Container(
            content=Column(
                controls=[
                    Text("Buscar Pessoa por Email", text_align=TextAlign.CENTER, size=30, weight=FontWeight.BOLD),
                    TextField(label="Email", hint_text="Digite o email aqui!"),
                    ElevatedButton(content=Row([Text("Buscar", size=20)], alignment=MainAxisAlignment.CENTER), width=180, height=50, on_click=buscar_pessoa_por_email)
                ], alignment=MainAxisAlignment.CENTER, horizontal_alignment=CrossAxisAlignment.CENTER
            ), width=480
        )

        self.container_alterar_dados = Container(
            content=Column(
                controls=[
                    Text("Alterar Dados da Pessoa", text_align=TextAlign.CENTER, size=30, weight=FontWeight.BOLD),
                    TextField(label="Email", hint_text="Digite o email aqui!"),
                    Text("Novos Dados", text_align=TextAlign.CENTER, size=30, weight=FontWeight.BOLD),
                    TextField(label="Nome", hint_text="Entre com o Nome aqui!"),
                    TextField(label="Idade", hint_text="Entre com a Idade aqui!"),
                    TextField(label="Altura", hint_text="Entre com a Altura aqui!"),
                    TextField(label="Email", hint_text="Entre com o Email aqui!"),
                    ElevatedButton(content=Row([Text("Alterar", size=20)], alignment=MainAxisAlignment.CENTER), width=180, height=50, on_click=alterar_dados)
                ], alignment=MainAxisAlignment.CENTER, horizontal_alignment=CrossAxisAlignment.CENTER
            ), width=480
        )

        self.container_excluir_pessoa = Container(
            content=Column(
                controls=[
                    Text("Excluir Pessoa", text_align=TextAlign.CENTER, size=30, weight=FontWeight.BOLD),
                    TextField(label="Email", hint_text="Digite o email aqui!"),
                    ElevatedButton(content=Row([Text("Excluir", size=20)], alignment=MainAxisAlignment.CENTER), width=180, height=50, on_click=excluir_pessoa)
                ], alignment=MainAxisAlignment.CENTER, horizontal_alignment=CrossAxisAlignment.CENTER
            ), width=480
        )

        self.container_inicial = Container(
            content=Column(
                controls=[
                   Text("Bem Vindo!", text_align=TextAlign.CENTER, size=30, weight=FontWeight.BOLD)
                ], alignment=CrossAxisAlignment.CENTER
            )
        )

        self.container_informacoes = Container(
            content=Column(
                controls=[
                    self.container_inicial
                ], alignment=CrossAxisAlignment.CENTER
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
