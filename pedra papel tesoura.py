import random
import customtkinter as ctk

# Função do jogo de Pedra, Papel e Tesoura
def jogar_pedra_papel_tesoura(escolha_jogador):
    opcoes = ['PEDRA', 'PAPEL', 'TESOURA']
    escolha_computador = random.choice(opcoes)
    
    # Exibe as escolhas
    resultado_jogador.set(f'Você escolheu: {escolha_jogador}')
    resultado_computador.set(f'O computador escolheu: {escolha_computador}')
    
    # Determina o resultado do jogo
    if escolha_jogador == escolha_computador:
        resultado_jogo.set('EMPATOU')
    elif (escolha_jogador == 'PEDRA' and escolha_computador == 'TESOURA') or \
         (escolha_jogador == 'PAPEL' and escolha_computador == 'PEDRA') or \
         (escolha_jogador == 'TESOURA' and escolha_computador == 'PAPEL'):
        resultado_jogo.set('VOCÊ GANHOU!')
    else:
        resultado_jogo.set('VOCÊ PERDEU!')

# Cria a janela principal
janela = ctk.CTk()
janela.title('Jogo de Pedra, Papel e Tesoura')

# Variáveis para armazenar os resultados
resultado_jogador = ctk.StringVar()
resultado_computador = ctk.StringVar()
resultado_jogo = ctk.StringVar()

# Label inicial
label_titulo = ctk.CTkLabel(janela, text='ESSE É UM JOGO DE PEDRA, PAPEL E TESOURA!!!!!!', font=('Arial', 16))
label_titulo.pack(pady=10)
label_titulo = ctk.CTkLabel(janela, text='ESCOLHA O SEU', font=('Arial', 16))
label_titulo.pack(padx=10)

# Botões para escolha do jogador
frame_botoes = ctk.CTkFrame(janela)
frame_botoes.pack(pady=10)

botao_pedra = ctk.CTkButton(frame_botoes, text='PEDRA', command=lambda: jogar_pedra_papel_tesoura('PEDRA'))
botao_pedra.grid(row=0, column=0, padx=10)

botao_papel = ctk.CTkButton(frame_botoes, text='PAPEL', command=lambda: jogar_pedra_papel_tesoura('PAPEL'))
botao_papel.grid(row=0, column=1, padx=10)

botao_tesoura = ctk.CTkButton(frame_botoes, text='TESOURA', command=lambda: jogar_pedra_papel_tesoura('TESOURA'))
botao_tesoura.grid(row=0, column=2, padx=10)

# Labels para exibir os resultados
label_resultado_jogador = ctk.CTkLabel(janela, textvariable=resultado_jogador, font=('Arial', 14))
label_resultado_jogador.pack(pady=5)

label_resultado_computador = ctk.CTkLabel(janela, textvariable=resultado_computador, font=('Arial', 14))
label_resultado_computador.pack(pady=5)

label_resultado_jogo = ctk.CTkLabel(janela, textvariable=resultado_jogo, font=('Arial', 16, 'bold'))
label_resultado_jogo.pack(pady=10)

def reiniciar_jogo():
    resultado_jogador.set('')
    resultado_computador.set('')
    resultado_jogo.set('')

botao_reset = ctk.CTkButton(janela, text='Jogar Novamente', command=reiniciar_jogo)
botao_reset.pack(pady=10)

# Executa a interface
janela.mainloop()
