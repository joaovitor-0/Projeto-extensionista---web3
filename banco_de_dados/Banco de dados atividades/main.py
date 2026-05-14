from tkinter import *
import mysql.connector
import tkinter.messagebox as MessageBox
from datetime import datetime

conexao = mysql.connector.connect(
    host="localhost",
    user="root",
    password="",
)

cursor = conexao.cursor()

cursor.execute('create database if not exists Gavime')
cursor.execute('use Gavime')

cursor.execute('create table if not exists atividades(id_atividade int primary key auto_increment,'
               'nome_atividade varchar(100) not null,'
               'descricao varchar(100),'
               'data_atividade date,'
               'local_atividade varchar(100),'
               'quantidade_vagas int,'
               'status_atividade varchar(100) not null)')

class Atividade:
    def __init__(self):
        self.__id_atividade = ''
        self.__nome_atividade = ''
        self.__descricao = ''
        self.__data_atividade = ''
        self.__local_atividade = ''
        self.__quantidade_vagas = ''
        self.__status_atividade = ''

    def get_id_atividade(self):
        return self.__id_atividade

    def set_id_atividade(self, id_atividade):
        self.__id_atividade = id_atividade


    def get_nome_atividade(self):
        return self.__nome_atividade

    def set_nome_atividade(self, nome_atividade):
        if len(nome_atividade) > 0:
            self.__nome_atividade = nome_atividade
        else:
            print('Nome invalido. Nome deve ser maior que zero')


    def get_descricao(self):
        return self.__descricao

    def set_descricao(self, descricao):
        self.__descricao = descricao


    def get_data_atividade(self):
        return self.__data_atividade

    def set_data_atividade(self, data_atividade):
        self.__data_atividade = data_atividade


    def get_local_atividade(self):
        return self.__local_atividade

    def set_local_atividade(self, local_atividade):
        self.__local_atividade = local_atividade


    def get_quantidade_vagas(self):
        return self.__quantidade_vagas

    def set_quantidade_vagas(self, quantidade_vagas):
        self.__quantidade_vagas = quantidade_vagas


    def get_status_atividade(self):
        return self.__status_atividade

    def set_status_atividade(self, status_atividade):
        if len(status_atividade) > 0:
            self.__status_atividade = status_atividade
        else:
            print('Status invalido. Status deve ser maior que zero')


class App:
    def __init__(self):
        self.atividade = Atividade()

        self.janela = Tk()
        self.janela.title('Cadastro de atividades')
        self.janela.geometry('600x550')

        self.label = Label(self.janela, text = 'Código da atividade')
        self.label.place(x = 20, y = 20)

        self.e_id = Entry(self.janela, width = 40)
        self.e_id.place(x = 180, y = 20)

        self.label = Label(self.janela, text = 'Código gerado automaticamente. Use apenas para consultas', fg = 'gray')
        self.label.place(x = 180, y = 40)

        self.label = Label(self.janela, text = 'Nome da atividade')
        self.label.place(x = 20, y = 60)

        self.e_nome = Entry(self.janela, width = 40)
        self.e_nome.place(x = 180, y = 60)

        self.label = Label(self.janela, text = 'Descrição')
        self.label.place(x = 20, y = 100)

        self.e_descricao = Entry(self.janela, width = 40)
        self.e_descricao.place(x = 180, y = 100)

        self.label = Label(self.janela, text = 'Data de atividade')
        self.label.place(x = 20, y = 140)

        self.e_data_atividade = Entry(self.janela, width = 40)
        self.e_data_atividade.place(x = 180, y = 140)

        self.label = Label(self.janela, text = 'Local da atividade')
        self.label.place(x = 20, y = 180)

        self.e_local = Entry(self.janela, width = 40)
        self.e_local.place(x = 180, y = 180)

        self.label = Label(self.janela, text = 'Quantidade de vagas')
        self.label.place(x = 20, y = 220)

        self.e_vagas = Entry(self.janela, width = 40)
        self.e_vagas.place(x = 180, y = 220)

        self.label = Label(self.janela, text = 'Status da atividade')
        self.label.place(x = 20, y = 260)

        self.status_var = StringVar()

        self.aberta = Radiobutton(self.janela, text = 'Aberta', variable = self.status_var, value = 'Aberta')
        self.aberta.place(x = 180, y = 260)

        self.andamento = Radiobutton(self.janela, text = 'Em andamento', variable = self.status_var, value = 'Em andamento')
        self.andamento.place(x = 260, y = 260)

        self.encerrada = Radiobutton(self.janela, text = 'Encerrada', variable = self.status_var, value = 'Encerrada')
        self.encerrada.place(x = 390, y = 260)


        self.btnInserir = Button(self.janela, text = 'Inserir', width = 12,command = self.inserir)
        self.btnInserir.place(x = 20, y = 340)

        self.btnConsultar = Button(self.janela, text = 'Consultar', width = 12,command = self.consultar)
        self.btnConsultar.place(x = 130, y = 340)

        self.btnAtualizar = Button(self.janela, text = 'Atualizar', width = 12,command = self.atualizar)
        self.btnAtualizar.place(x = 240, y = 340)

        self.btnExcluir = Button(self.janela, text = 'Excluir', width = 12,command = self.excluir)
        self.btnExcluir.place(x = 460, y = 340)

        self.btnLimpar = Button(self.janela, text = 'Limpar', width = 12,command = self.limpar)
        self.btnLimpar.place(x = 350, y = 340)

        self.janela.mainloop()

    def preencher(self):
        self.atividade.set_nome_atividade(self.e_nome.get())
        self.atividade.set_descricao(self.e_descricao.get())
        self.atividade.set_local_atividade(self.e_local.get())
        self.atividade.set_status_atividade(self.status_var.get())

        if(self.atividade.get_nome_atividade() == '' or self.atividade.get_status_atividade() == ''):
            MessageBox.showerror('Erro', 'Informe o nome e status da atividade')
            return False

        vagas_digitadas = self.e_vagas.get()

        if(vagas_digitadas != ''):
            try:
                vagas = int(vagas_digitadas)

                if(vagas < 0):
                    MessageBox.showerror('Erro', 'Quantidade de vagas não pode ser menor que zero.')
                    return False

                self.atividade.set_quantidade_vagas(vagas)

            except ValueError:
                MessageBox.showerror('Erro', 'Digite apenas números inteiros.')
                return False

        else:
            self.atividade.set_quantidade_vagas(None)

        data_digitada = self.e_data_atividade.get()

        if(data_digitada != ''):
            try:
                data_mysql = datetime.strptime(data_digitada, '%d/%m/%Y').strftime('%Y-%m-%d')

                self.atividade.set_data_atividade(data_mysql)

            except ValueError:
                MessageBox.showerror('Erro','Coloque a data dia/mes/ano')
                return False

        else:
            self.atividade.set_data_atividade(None)

        return True


    def inserir(self):
        if(self.preencher() == False):
            return
        else:
            cursor.execute('insert into atividades(nome_atividade,descricao,data_atividade,local_atividade,quantidade_vagas,status_atividade) '
                           'values (%s,%s,%s,%s,%s,%s)', (self.atividade.get_nome_atividade(),self.atividade.get_descricao(),
                                                          self.atividade.get_data_atividade(),self.atividade.get_local_atividade(),
                                                          self.atividade.get_quantidade_vagas(),self.atividade.get_status_atividade()))

            conexao.commit()

            MessageBox.showinfo('Sucesso','Atividade inserida!')

            self.limpar()


    def consultar(self):
        id_atividade = self.e_id.get()

        if(id_atividade == ''):
            MessageBox.showerror('Erro', 'Informe o código da atividade')
            return
        else:
            cursor.execute('select * from atividades where id_atividade = %s', (id_atividade,))
            dados = cursor.fetchone()

            if(dados):
                self.limpar()

                self.e_id.insert(0, dados[0])
                self.e_nome.insert(0, dados[1])
                self.e_descricao.insert(0, dados[2])

                if(dados[3] is not None):
                    data_formatada = dados[3].strftime('%d/%m/%Y')

                    self.e_data_atividade.insert(0, data_formatada)

                self.e_local.insert(0, dados[4])

                if(dados[5] is not None):
                    self.e_vagas.insert(0, dados[5])

                self.status_var.set(dados[6])

            else:
                MessageBox.showinfo('Consulta', 'Atividade não encontrada')


    def atualizar(self):
        id_atividade = self.e_id.get()

        if(id_atividade == ''):
            MessageBox.showerror('Erro','Informe o código da atividade')
            return

        if(self.preencher() == False):
            return

        cursor.execute('update atividades set nome_atividade = %s, descricao = %s, data_atividade = %s, '
                       'local_atividade = %s,quantidade_vagas = %s, status_atividade = %s where id_atividade = %s',
                       (self.atividade.get_nome_atividade(),self.atividade.get_descricao(),
                        self.atividade.get_data_atividade(), self.atividade.get_local_atividade(),
                        self.atividade.get_quantidade_vagas(),self.atividade.get_status_atividade(),id_atividade))

        conexao.commit()

        MessageBox.showinfo('Sucesso','Atividade atualizada!')
        self.limpar()


    def excluir(self):
        id_atividade = self.e_id.get()

        if(id_atividade == ''):
            MessageBox.showerror('Erro', 'Informe o código da atividade')
            return

        cursor.execute('delete from atividades where id_atividade = %s', (id_atividade,))

        conexao.commit()

        MessageBox.showinfo('Sucesso', 'Atividade excluída!')

        self.limpar()


    def limpar(self):
        self.e_id.delete(0, 'end')
        self.e_nome.delete(0, 'end')
        self.e_descricao.delete(0, 'end')
        self.e_data_atividade.delete(0, 'end')
        self.e_local.delete(0, 'end')
        self.e_vagas.delete(0, 'end')

        self.status_var.set('')

App()