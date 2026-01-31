import time

import keyboard

from backend.service.stt import AudioStreamSTT
from backend.service.tts import AudioStreamTTS


def listen_commands(
    stt_engine: AudioStreamSTT, rate: int, chunk: int, lang: str, username: str
) -> str:
    print("Press and hold ALT to start talking")
    keyboard.wait("alt")
    print("Recording...")
    command = []
    try:
        while keyboard.is_pressed("alt"):
            command.append(stt_engine.record())
            time.sleep(chunk / rate)
        print("Recording stopped")

        record = stt_engine.bytes_to_array(command)
        audio = stt_engine.transcribe(record, lang)
    except (OSError, IOError) as e:
        print(f"Audio device error: {e}")
    except (ValueError, RuntimeError) as e:
        print(f"Speach recognition error: {e}")
    except Exception as e:
        print(f"TTS error: {e}")

    print(f"{username}: {audio}")
    return audio


def speak_assistant(
    tts_engine: AudioStreamTTS, audio: str, lang: str, wav: list[str]
) -> None:
    try:
        reply_array = tts_engine.synthesizing(
            text=audio,
            lang=lang,
            temperature=0.7,
            speed=1.0,
            wav=wav,
        )
        reply = tts_engine.array_to_bytes(reply_array)
        tts_engine.voice(reply)
    except (OSError, IOError) as e:
        print(f"Audio output error: {e}")
    except (ValueError, RuntimeError) as e:
        print(f"Speech synthesis error: {e}")
    except Exception as e:
        print(f"TTS error: {e}")
