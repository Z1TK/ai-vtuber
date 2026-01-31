# AI-Femboy
An open-source AI waifu created just for fun, but you’re free to use it for your own enjoyment.

## Links 
- [Setup](#setup)
- [Requirements](#requirements)
- [State of Development](#development)

## Setup
To set up project:
1. Clone the repository:
```
    git clone https://github.com/Z1TK/budget-AI-VTuber.git
```
2. Create environemnt:
```
    python -3.11 -m venv venv
    .\venv\Scripts\activate
```
3. Install dependencies
```
    pip install -r requirements.txt
```
4. Install CUDA 12.6 version of pytorch 2.8.0
```
    pip install torch==2.8.0 torchvision==0.23.0 torchaudio==2.8.0 --index-url https://download.pytorch.org/whl/cu126
```
5. Create a `.env` file and add your Ollama API key.
    https://ollama.com/settings/keys
```
    OLLAMA_API_KEY=6a59c6db67bdb4c83af4738cd5bb7531.soTzhjmiqntsLaHyua18uwU_
```
6. Start program
```
    python main.py
```
P.S. To use a VTube avatar, you need to install VTube Studio and VB-CABLE.

## Requirements

## State of Development
The project could be considered in an "early access state".