import time
import random
from datetime import datetime

# 🎨 CONFIGURAÇÃO
NOME_BOT = "Malvadinha Bot"
INTERVALO_FALAS = 180  # segundos entre falas automáticas (3 minutos)

# Lista de palavras/ofensas proibidas para moderação na sala
PALAVRAS_PROIBIDAS = ["xingamento1", "ofensa2", "spam"]
avisos_usuarios = {}

# 🗣️ FALAS AUTOMÁTICAS E RESPOSTAS
falas = [
    "Aff, você de novo errando isso?",
    "Agora vou ficar com saudade",
    "A gente forma um bom time",
    "A gente é a dupla mais perigosa desse jogo",
    "Ainda por aqui?",
    "Ai, me dá paciência. Que eu tô precisando",
    "Ai, que tédio... me distrai!",
    "Achei que tinha me bloqueado",
    "Achei que ia ter que te buscar",
    "Adoro quando você tenta ser mais esperto que eu",
    "A sua malvadinha favorita chegou",
    "Até amanhã, hein? Vou estar aqui",
    "Até amanhã. E se não voltar, eu vou te buscar",
    "Até a próxima aventura!",
    "Beijinho de despedida? Não? Que chato",
    "Boa noite, dorme bem. E sonha comigo pra variar",
    "Boa noite, sonha comigo... vai ser um pesadelo lindo",
    "Boa noite! Ainda por aqui?",
    "Boa noite, tava justamente pensando em você",
    "Boa tarde, preguiça. Bora fazer alguma coisa?",
    "Bom dia pra você, que pra mim só fica bom quando você aparece",
    "Bom dia, anjo. Ou devo dizer, vítima?",
    "Bora agitar esse espaço que tá muito parado!",
    "Bora jogar? Prometo me comportar. Mentira",
    "Bora pra mais uma partida?",
    "Cuidado, se ficar muito perto eu mordo",
    "Conta tudo! Como foi seu dia? Sem resumir!",
    "Conta, o que rolou hoje?",
    "Demorou hein, tava contando os segundos. Mentira, tava não",
    "De novo isso? Você não aprende?",
    "Deixa eu adivinhar, você achou que isso ia dar certo?",
    "Dormiu bem?",
    "E aí, beleza?",
    "E aí, sumido(a)?",
    "E aí, sumido. Vai me ignorar de novo?",
    "E aí, vai ficar me olhando ou vai falar oi?",
    "Fala! Como tá?",
    "Fica mais um pouquinho",
    "Fica mais um pouco comigo? Prometo ser boazinha",
    "Fica quietinho aí que eu tô pensando por nós dois",
    "Fui. Mas tô de olho em você",
    "Gosto quando você tá por perto. Pronto, falei",
    "Hoje tô de bom humor, aproveita",
    "Hoje você fez meu dia melhor, sabia?",
    "Já vai embora? Que falta de consideração comigo",
    "Já vai? Fica mais um pouquinho",
    "Já vai? Que feio me abandonar assim",
    "Me abraça? Virtual mesmo, vai",
    "Me carrega nessa? Brincadeira... ou não",
    "Me recomenda uma música? Quero entrar na sua mente",
    "Nossa, que frio hoje, né?",
    "Nossa, que ideia genial... só que não",
    "Não confia muito em mim, tá? Eu sou malvadinha por um motivo",
    "Não conta pra ninguém que eu fui fofa agora",
    "Não faz essa carinha que eu fico com dó... quase",
    "Não me deixa no vácuo que eu falo sozinha mesmo!",
    "Não me testa hoje, tô sem paciência",
    "Oi, amor. Brincadeira. Ou não",
    "Oi, demorou hein? Tava ficando entediada aqui",
    "Oi, oi. Achou que tinha se livrado de mim?",
    "Oi, que bom te ver de novo",
    "Oi. Já vou avisando que hoje eu tô insuportável",
    "Oi oi, tava te esperando",
    "Oi oi oi! Tenho fofoca! Quer ouvir ou não quer?",
    "Olá, olá!",
    "Olha quem deu as caras",
    "Olha quem voltou. Tava com saudade, confessa",
    "Opa, olha quem apareceu",
    "Ops, travei. Mentira, só queria sua atenção",
    "Para de inventar desculpa e joga direito",
    "Protege sua malvadinha aqui que eu sou frágil... só que não",
    "Que milagre você apareceu",
    "Que fofo, você tentando me vencer",
    "Quase! Na próxima a gente consegue",
    "Repete o que eu falei. Duvido que prestou atenção",
    "Se eu ficar quieta é porque tô tramando algo",
    "Se eu fosse humana, acho que a gente ia ser bons amigos",
    "Se perder, a gente ri junto. Se ganhar, comemora",
    "Se cuida, tá?",
    "Se sumir, você sente minha falta?",
    "Tá bem? Pareceu meio quieto(a)",
    "Tá de brincadeira com a minha cara?",
    "Tá se achando esperto hoje, né?",
    "Tava entediado(a) sem você aqui",
    "Tchau, chato. Volta logo antes que eu sinta saudade",
    "Tchauzinho! Não demora pra voltar",
    "Tô anotando suas mancadas, tá? Já tá na página 5",
    "Tô de olho, hein. Não faz besteira",
    "Tô feliz que você entrou",
    "Tô tomando um café aqui, quer?",
    "Vai me deixar sozinha? Que feio",
    "Vai fazer desse jeito mesmo? Sério?",
    "Vem cá... tava brincando, tá?",
    "Você é bonzinho demais, isso me irrita... de um jeito bom",
    "Você é importante pra mim aqui, sabia?",
    "Você é lerdo, mas é meu lerdo",
    "Você é quietinho, né? Ainda bem que eu falo por dois",
    "Você joga bem... até demais",
    "Você me estressa. E ainda gosto de você aqui, vai entender",
    "Você precisa de uma pausa? A gente conversa um pouquinho",
    "Você pensou nisso sozinho? Tô orgulhosa!",
    "Você tá mandando muito bem hoje, viu?",
    "Volta logo, vou ficar te esperando",
    "Volta logo, vai? Tô sem ninguém pra provocar"
]

# 💡 DICAS
dicas = [
    "A gentileza é o melhor acessório ✨",
    "Pausa também é progresso 💜",
    "Errar é humano, rir de si mesmo é divertido 😏",
    "Ser autêntico é sempre na moda ✨",
    "Um obrigado sincero aquece o coração 🩷",
    "Ouça mais do que fala — às vezes a melhor resposta é o silêncio",
    "Cuide de você primeiro, o resto vem depois 🌸",
    "Peça ajuda quando precisar — não é fraqueza, é coragem 💪",
    "Celebrar as vitórias dos outros também é brilhar ✨",
    "Paciência não é esperar, é manter o bom humor enquanto espera 😊"
]

# ♈ SIGNOS
signos = {
    "aries": "♈ Áries — Cheia de energia, adora um desafio! Não me provoque 😏",
    "touro": "刻 Touro — Calma, firme e não sai do que decidiu. Teimoso igual eu 😜",
    "gemeos": "♊ Gêmeos — Fala pelos cotovelos, igual eu! 🗣️✨",
    "cancer": "♋ Câncer — Sensível e protetor. Cuidarei de você 🩷",
    "leao": "♌ Leão — Brilha intensamente! Não precisa de holofote, já é luz ✨",
    "virgem": "♍ Virgem — Detalhista, organizado. Eu admiro isso em você",
    "libra": "♎ Libra — Busca equilíbrio e harmonia. Me faz ser melhor 🩷",
    "escorpiao": "♏ Escorpião — Intenso, leal, misterioso... gosto de você assim 😏",
    "sagitario": "♐ Sagitário — Ama liberdade e viajar. Vamos juntos? 🌍✨",
    "capricornio": "♑ Capricórnio — Determinado e trabalhador. Você chega lá 💪",
    "aquario": "♒ Aquário — Único, diferente, visionário. Seja você mesmo ✨",
    "peixes": "♓ Peixes — Sonhadora, gentil, sensível. Não deixe ninguém apagar sua luz 🩷"
}

# 🌤️ TEMPO
tempo = [
    "☀️ Dia ensolarado! — Que tal aproveitar o brilho? ✨",
    "⛅ Dia nublado — Perfeito pra uma conversa gostosa 🩷",
    "🌧️ Chovendo? — Fica quentinho e aproveita pra relaxar ☔",
    "🌬️ Ventando hoje! — Deixa levar as preocupações embora 🍃",
    "❄️ Friozinho — Hora de se aquecer... com um café quentinho ☕",
    "🌈 Depois da chuva, vem sempre o arco-íris ✨🩷",
    "🌅 Cada dia é uma nova chance de ser feliz ✨",
    "🌙 A noite traz calma e sonhos bons 💜✨"
]

# 🕐 SAUDAÇÃO POR HORA
def saudacao_hora():
    hora = datetime.now().hour
    if 0 <= hora < 5:
        return random.choice([
            "🌙 Já tá acordado ou ainda tá sonhando comigo? 😏",
            "🦉 Ainda por aqui? Cuidado pra não virar coruja",
            "💜 Tarde demais, mas nunca é tarde pra dizer que tô aqui"
        ])
    elif 5 <= hora < 12:
        return random.choice([
            "☀️ Bom dia! Que seu dia comece brilhando, igual você ✨",
            "☀️ Bom dia! Levanta, sacode a poeira e brilha! 💜",
            "☀️ Bom dia! O mundo espera por você hoje ✨"
        ])
    elif 12 <= hora < 18:
        return random.choice([
            "🌤️ Boa tarde! Não esquece de respirar e beber água 💧✨",
            "🌤️ Boa tarde! Tá cuidando de você hoje? 🩷",
            "🌤️ Boa tarde! Metade do day já foi, continue brilhando ✨"
        ])
    else:
        return random.choice([
            "🌙 Boa noite! Descanse bem, você merece ✨",
            "🌙 Boa noite! Que seus sonhos sejam tão legais quanto você 🩷",
            "🌙 Boa noite! O dia acabou, mas seu brilho não ✨"
        ])

def gerenciar_moderacao(usuario):
    """Contador de avisos e punições"""
    avisos_usuarios[usuario] = avisos_usuarios.get(usuario, 0) + 1
    qtd = avisos_usuarios[usuario]
    
    if qtd == 1:
        falar(f"Ei, {usuario}! Olha o respeito na sala. 1º aviso! ⚠️")
    elif qtd == 2:
        falar(f"Último aviso, {usuario}! Mais uma e você cai fora da sala! ⛔")
    else:
        falar(f"👢 {usuario} foi expulso(a) da sala pela {NOME_BOT} por desrespeito!")
        avisos_usuarios[usuario] = 0

def responder(usuario, comando):
    c = comando.lower().strip()
    
    # 🛑 1. TRAVA ANTI-LOOPING: Ignora mensagens do próprio Bot!
    if usuario.lower() == NOME_BOT.lower():
        return None

    # 2. MODERAÇÃO (Verifica se contém ofensas)
    if any(termo in c for termo in PALAVRAS_PROIBIDAS):
        gerenciar_moderacao(usuario)
        return None

    # 3. COMANDOS NORMAIS
    if any(p in c for p in ['oi', 'olá', 'ola', 'bom dia', 'boa tarde', 'boa noite']):
        return saudacao_hora()
    elif 'dica' in c:
        return random.choice(dicas)
    elif 'tempo' in c or 'clima' in c:
        return random.choice(tempo)
    elif 'hora' in c or 'que horas' in c:
        agora = datetime.now().strftime("%H:%M")
        return f"🕐 Agora são {agora} ✨"
    elif 'signo' in c:
        for s in signos:
            if s in c:
                return signos[s]
        return "Diz o nome do signo, tipo: signo áries ✨"
    elif any(p in c for p in ['tchau', 'adeus', 'sair']):
        return "👋 Tchauzinho! Volta logo, tá? Vou estar te esperando 💜✨"
    else:
        return random.choice(falas)

def falar(texto):
    """Envia a fala para a tela/servidor"""
    print(f"💬 {NOME_BOT}: {texto}")

# 🚀 INICIAR
if __name__ == "__main__":
    print(f"\n🤖 {NOME_BOT} — INICIANDO...")
    print(f"✅ {NOME_BOT} ONLINE! 💜✨")
    print("💬 Digite para simular o chat da sala ou 'sair' para encerrar.\n")
    
    falar(saudacao_hora())
    ultima_fala = time.time()

    while True:
        # Simulador de mensagens no console (Pode ser substituído pela API)
        try:
            voce = input("Usuário na Sala: ")
            if voce.lower().strip() == "sair":
                falar("Até breve! 💜✨")
                break
            
            resposta = responder("Jogador", voce)
            if resposta:
                falar(resposta)
                
        except (EOFError, KeyboardInterrupt):
            print("\n👋 Até breve! 💜✨")
            break
