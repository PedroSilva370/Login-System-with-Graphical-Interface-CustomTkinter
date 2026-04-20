import customtkinter as ctk

# Configuração aparência
ctk.set_appearance_mode('dark')

# Criação das funções
def validar_login():
    usuario = campo_usuario.get()
    senha = campo_senha.get()

    # verificar se o  usuario é pedro e a senha 12345678
    if usuario == "pedro" and senha == '12345678':
        resultado_login.configure(text='Login feito com sucesso!', text_color='green')
    else:
        resultado_login.configure(text='Login incorreto', text_color='red')

# Criação da janela principal
app = ctk.CTk()
app.title('Sistema de Login')
app.geometry('300x300')

# Criação dos campos
# Label
label_usuario = ctk.CTkLabel(app, text='Usuário:')
label_usuario.pack(pady=7)
# Entry
campo_usuario = ctk.CTkEntry(app, placeholder_text='Digite seu Usuário')
campo_usuario.pack(pady=5)
# Label
label_senha = ctk.CTkLabel(app, text='Senha:')
label_senha.pack(pady=7)
# Entry
campo_senha = ctk.CTkEntry(app, placeholder_text='Digite sua Senha')
campo_senha.pack(pady=5)
# Button
botao_login = ctk.CTkButton(app, text='Login', command=validar_login)
botao_login.pack(pady=7)
# campo feedback de login
resultado_login = ctk.CTkLabel(app, text='')
resultado_login.pack(pady=7)

# Iniciar a aplicação
app.mainloop()