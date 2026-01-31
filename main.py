import torch
from dotenv import load_dotenv

from backend.ai_vituber import ai_assistant
from backend.service.llm import OllamaClient
from backend.service.stt import AudioStreamSTT
from backend.service.tts import AudioStreamTTS

load_dotenv()


def main():
    tts_engine = AudioStreamTTS("tts_models/multilingual/multi-dataset/xtts_v2", "cuda")
    stt_engine = AudioStreamSTT("large-v2", "cpu", type="int8")
    llm_engine = OllamaClient("gemini-3-flash-preview", "https://ollama.com")

    ai_assistant(
        stt=stt_engine,
        tts=tts_engine,
        llm=llm_engine,
        rate_size=16000,
        chunk_size=1024,
        language="ru",
        username="PEZDABOLIUS"
    )

if __name__ == "__main__":
    main()
