from backend.service.llm import OllamaClient
from backend.service.stt import AudioStreamSTT
from backend.service.tts import AudioStreamTTS
from backend.utils.request import chat
from backend.utils.search import open_site, request_to_youtube
from backend.utils.speak import listen_commands, speak_assistant

exit_commands = {"выход", "exit", "quit"}


def ai_assistant(
    stt: AudioStreamSTT,
    tts: AudioStreamTTS,
    llm: OllamaClient,
    rate_size: int,
    chunk_size: int,
    language: str,
    username: str,
) -> None:
    stt.start(rate_size, chunk_size)
    tts.start(chunk_size)

    try:
        while True:
            text = listen_commands(
                stt_engine=stt,
                rate=rate_size,
                chunk=chunk_size,
                lang=language,
                username=username,
            )
            command = text.strip(" .,!?\n").lower()

            if command == "":
                print("The user didn't say anything")
                continue
            if command in exit_commands:
                break
            if open_site(command):
                continue
            if request_to_youtube(command):
                continue

            # thinking = ask_assistent(llm_engine=llm, prompt=text)
            thoughts = chat(
                llm_engine=llm, content=text, system_content="character.txt"
            )

            print(f"Friend: {thoughts}")
            speak_assistant(
                tts_engine=tts,
                audio=thoughts,
                lang=language,
                wav=[
                    "samples/sample.wav",
                ],
            )
    finally:
        tts.close()
        stt.close()
