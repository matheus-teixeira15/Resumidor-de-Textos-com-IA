
import os
from dotenv import load_dotenv
from google import genai

# Carrega as variáveis do arquivo .env
load_dotenv()

# Armazena a chave da API em uma variável
api_key = os.getenv("GEMINI_API_KEY")

# Armazena o comando base para se comunicar com a IA
client = genai.Client(api_key=api_key)


def resumir_texto(texto, tamanho):
    """
    Recebe um texto e retorna um resumo gerado pelo Gemini.
    """

    prompt = f"""
    Você é um assistente especializado em resumir textos.

    Sua tarefa é resumir o texto abaixo.

    O resumo deve ter o seguinte tamanho: {tamanho}.

    Preserve as informações mais importantes,
    utilize uma linguagem clara e não invente informações.

    Texto para resumir:
    {texto}
    """

    # Envia o prompt com o texto a ser resumido para a IA e armazena o resumo
    response = client.models.generate_content(
        model="gemini-3.8-flash",
        contents=prompt
    )

    # Retorna o texto produzido pela IA
    return response.text
