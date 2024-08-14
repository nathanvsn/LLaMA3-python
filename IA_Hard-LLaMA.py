import torch
from transformers import AutoModelForCausalLM, AutoTokenizer, pipeline

model_id = "Meta-Llama-3.1-8B"

model = AutoModelForCausalLM.from_pretrained(
    model_id,
    torch_dtype=torch.float16,
    device_map="auto"                 # Garante que o modelo será carregado na GPU
)

tokenizer = AutoTokenizer.from_pretrained(model_id)

text_gen_pipeline = pipeline(
    "text-generation",
    model=model,
    tokenizer=tokenizer,
)

def chat_with_model(prompt, max_length=300):
    # Gerar resposta
    response = text_gen_pipeline(prompt, max_new_tokens=max_length)[0]['generated_text']
    
    # Limpar o prompt da resposta
    return response[len(prompt):].strip()

# Conversa constante
context = ""
while True:
    user_input = input("\033[32mVocê: \033[0m")  # Verde
    print(f"User input: {user_input}")
    context += f"Você: {user_input}\n"
    print("Contexto:", context)
    prompt = context + "Assistente:"
    print("Prompt:", prompt)
    response = chat_with_model(prompt)
    print("Response:", response)
    context += f"Assistente: {response}\n"
    print(f"\033[33mAssistente: {response}\033[0m")  # Amarelo

    # Condição para encerrar a conversa
    if user_input.lower() in ["exit", "sair", "encerrar"]:
        break