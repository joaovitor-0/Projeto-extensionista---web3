import mysql.connector
import tkinter as tk
from tkinter import messagebox

conexao = mysql.connector.connect(
    host="localhost",
    user="root",
    password="",
)
cursor = conexao.cursor()
cursor.execute('USE Gavime')

cursor.execute("""
    CREATE TABLE IF NOT EXISTS participacoes (
        id_participacao INT PRIMARY KEY AUTO_INCREMENT,
        id_atividade INT,
        id_voluntario INT,
        data_cadastro TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
        FOREIGN KEY (id_atividade) REFERENCES atividades(id_atividade) ON DELETE CASCADE,
        FOREIGN KEY (id_voluntario) REFERENCES INSCRITOS(ID_VOLUNTARIO) ON DELETE CASCADE,
        UNIQUE KEY uq_participacao (id_atividade, id_voluntario)
    )
""")

class Participacao:
    def __init__(self):
        self.__id_participacao = ''
        self.__id_atividade = ''
        self.__id_voluntario = ''

    def get_id_participacao(self): return self.__id_participacao
    def set_id_participacao(self, id_participacao): self.__id_participacao = id_participacao

    def get_id_atividade(self): return self.__id_atividade
    def set_id_atividade(self, id_atividade): self.__id_atividade = id_atividade

    def get_id_voluntario(self): return self.__id_voluntario
    def set_id_voluntario(self, id_voluntario): self.__id_voluntario = id_voluntario

class AppParticipacoes:
    def __init__(self):
        self.participacao = Participacao()

        self.janela = tk.Tk()
        self.janela.title('Gavime - Vincular Voluntário à Atividade')
        self.janela.geometry('600x450')

        self.label = tk.Label(self.janela, text='Código do Vínculo')
        self.label.place(x=20, y=20)
        self.e_id_vinculo = tk.Entry(self.janela, width=40)
        self.e_id_vinculo.place(x=180, y=20)

        self.label = tk.Label(self.janela, text='Use apenas para consultas ou exclusão', fg='gray')
        self.label.place(x=180, y=40)

        self.label = tk.Label(self.janela, text='Código da Atividade')
        self.label.place(x=20, y=70)
        self.e_id_atividade = tk.Entry(self.janela, width=40)
        self.e_id_atividade.place(x=180, y=70)

        self.label = tk.Label(self.janela, text='Código do Voluntário')
        self.label.place(x=20, y=110)
        self.e_id_voluntario = tk.Entry(self.janela, width=40)
        self.e_id_voluntario.place(x=180, y=110)

        self.label_info = tk.Label(self.janela, text='Informações do Vínculo:', font=('Arial', 10, 'bold'))
        self.label_info.place(x=20, y=160)
        
        self.txt_info = tk.Text(self.janela, width=65, height=8, bg='#f0f0f0')
        self.txt_info.place(x=20, y=190)

        self.btnVincular = tk.Button(self.janela, text='Vincular', width=12, command=self.vincular)
        self.btnVincular.place(x=20, y=360)

        self.btnConsultar = tk.Button(self.janela, text='Consultar', width=12, command=self.consultar)
        self.btnConsultar.place(x=130, y=360)

        self.btnExcluir = tk.Button(self.janela, text='Remover Vínculo', width=15, command=self.excluir)
        self.btnExcluir.place(x=240, y=360)

        self.btnLimpar = tk.Button(self.janela, text='Limpar', width=12, command=self.limpar)
        self.btnLimpar.place(x=470, y=360)

        self.janela.mainloop()

    def preencher(self):
        id_atv = self.e_id_atividade.get()
        id_vol = self.e_id_voluntario.get()

        if id_atv == '' or id_vol == '':
            messagebox.showerror('Erro', 'Informe o Código da Atividade e do Voluntário')
            return False

        try:
            self.participacao.set_id_atividade(int(id_atv))
            self.participacao.set_id_voluntario(int(id_vol))
            return True
        except ValueError:
            messagebox.showerror('Erro', 'Os códigos devem ser números inteiros')
            return False

    def vincular(self):
        if not self.preencher():
            return

        try:
            cursor.execute("SELECT id_atividade FROM atividades WHERE id_atividade = %s", (self.participacao.get_id_atividade(),))
            if not cursor.fetchone():
                messagebox.showerror('Erro', 'Atividade não encontrada no sistema!')
                return

            cursor.execute("SELECT ID_VOLUNTARIO FROM INSCRITOS WHERE ID_VOLUNTARIO = %s", (self.participacao.get_id_voluntario(),))
            if not cursor.fetchone():
                messagebox.showerror('Erro', 'Voluntário não encontrado no sistema!')
                return

            sql = "INSERT INTO participacoes (id_atividade, id_voluntario) VALUES (%s, %s)"
            cursor.execute(sql, (self.participacao.get_id_atividade(), self.participacao.get_id_voluntario()))
            conexao.commit()
            
            messagebox.showinfo('Sucesso', 'Voluntário vinculado à atividade com sucesso!')
            self.limpar()

        except mysql.connector.Error as err:
            if err.errno == 1062: # Código de erro para entrada duplicada (Unique Key)
                messagebox.showwarning('Aviso', 'Este voluntário já está vinculado a esta atividade!')
            else:
                messagebox.showerror('Erro', f'Falha ao vincular: {err}')

    def consultar(self):
        id_vinculo = self.e_id_vinculo.get()

        if id_vinculo == '':
            messagebox.showerror('Erro', 'Informe o código do vínculo para consultar')
            return

        sql = """
            SELECT p.id_participacao, a.nome_atividade, a.local_atividade, v.NOME, v.EMAIL 
            FROM participacoes p
            INNER JOIN atividades a ON p.id_atividade = a.id_atividade
            INNER JOIN INSCRITOS v ON p.id_voluntario = v.ID_VOLUNTARIO
            WHERE p.id_participacao = %s
        """
        cursor.execute(sql, (id_vinculo,))
        dados = cursor.fetchone()

        if dados:
            self.limpar()
            self.e_id_vinculo.insert(0, dados)
            
            self.txt_info.insert('1.0', f"Vínculo ID: {dados}\n")
            self.txt_info.insert('end', f"----------------------------------------\n")
            self.txt_info.insert('end', f"ATIVIDADE: {dados} | Local: {dados}\n")
            self.txt_info.insert('end', f"VOLUNTÁRIO: {dados} | E-mail: {dados}\n")
        else:
            messagebox.showinfo('Consulta', 'Vínculo não encontrado')

    def excluir(self):
        id_vinculo = self.e_id_vinculo.get()

        if id_vinculo == '':
            messagebox.showerror('Erro', 'Informe o código do vínculo para remover')
            return

        cursor.execute('DELETE FROM participacoes WHERE id_participacao = %s', (id_vinculo,))
        conexao.commit()
        
        messagebox.showinfo('Sucesso', 'Vínculo removido com sucesso!')
        self.limpar()

    def limpar(self):
        self.e_id_vinculo.delete(0, 'end')
        self.e_id_atividade.delete(0, 'end')
        self.e_id_voluntario.delete(0, 'end')
        self.txt_info.delete('1.0', 'end')


if __name__ == "__main__":
    AppParticipacoes()