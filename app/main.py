from prompts import SYSTEM_PROMPT
from simulacoes import juros_compostos
import json

def classificar_intencao(texto):
    texto = texto.lower()
    if "juros" in texto or "simular" in texto:
        return "simulacao"
    if "cartão" in texto or "cdi" in texto or "rotativo" in texto:
        return "faq"
    return "geral"

def responder_usuario(mensagem):
    intencao = classificar_intencao(mensagem)

    if intencao == "simulacao":
        return "Para simular, me diga: valor inicial, taxa (%) e meses."

    if intencao == "faq":
        return "Posso te ajudar com isso. Pergunta registrada."

    return "Sou seu assistente financeiro. Como posso ajudar hoje?"

if __name__ == "__main__":
    print("Assistente Financeiro IA — DIO")
    while True:
        user = input("\nVocê: ")
        resposta = responder_usuario(user)
        print("Assistente:", resposta)

