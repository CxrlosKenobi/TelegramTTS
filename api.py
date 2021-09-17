from botocore.exceptions import BotoCoreError, ClientError
from contextlib import closing
from boto3 import Session
import subprocess
import json
import sys

session = Session(profile_name="default")
go = session.client("polly")

with open('data.json', 'r') as file:
    data = json.load(file)

def Pocket(text, voice) -> str:
    try:
        response = go.synthesize_speech(
            Text=text,
            OutputFormat="mp3",
            VoiceId=voice
        )
        
    except (BotoCoreError, ClientError) as error:
        print(error)
        sys.exit(-1)

    if "AudioStream" in response:
        with closing(response["AudioStream"]) as stream:
            try:
                with open("speech.mp3", "wb") as file:
                    file.write(stream.read())
            except IOError as error:
                print(error)
                sys.exit(-1)

        subprocess.call(data["convert"], shell=True)
        voicenote = open('speech.ogg', 'rb')

        return voicenote

    else:
        print("Could not stream audio")
        sys.exit(-1)


def help(update, context):
    update.message.reply_text(
        """💻 *Comandos disponibles* 💻
• _/start - Lista comandos
• _/tts help - Voces disponibles
• _/git - Versión del bot y código fuente_
    """, parse_mode='Markdown')


def version(update, context):
    sourceCode = "https://github.com/CxrlosKenobi/TelegramTTS"
    kenobiUrl = 'https://github.com/CxrlosKenobi'
    albfrUrl = 'https://github.com/AlbFR'
    
    update.message.reply_text(
        "<b>TTS Bot v1.0\n</b>"
        f"<b>Código fuente: </b><a href='{sourceCode}'>GitHub</a>\n"
        f"<b>Colaboradores</b>: <a href='{kenobiUrl}'>CxrlosKenobi</a>, <a href='{albfrUrl}'>AlbFR</a>"
    , parse_mode="HTML")

def tts(update, context):
    if context.args[0] == 'help':
        update.message.reply_text('''
*¡Puedes usar las siguientes voces!*

• /ttsCn - 🇨🇳 Zhiyu
• /ttsArb - 🇸🇦 Zeina
• /ttsFr - 🇫🇷 Celine
• /ttsJp - 🇯🇵 Takumi
• /ttsMx - 🇲🇽 Mia
• /ttsRu - 🇷🇺 Maxim
• /tts - 🇧🇷 Ricardo _(default)_

*Usage: /<tts> <text>*
''', parse_mode='Markdown')

        return
    
    update.message.reply_voice(
        Pocket(
            text=' '.join(context.args),
            voice='Ricardo'
        ), 
        quote=False
    )
    subprocess.call(data["ciao"], shell=True)

def ttsCn(update, context):
    if context.args[0] == '':
        update.message.reply_text('😟 ¡No olvides ingresar el texto!')
        return
    update.message.reply_voice(
        Pocket(text=' '.join(context.args), voice='Zhiyu'), 
        quote=False)
    subprocess.call(data["ciao"], shell=True)

def ttsArb(update, context):
    if context.args[0] == '':
        update.message.reply_text('😟 ¡No olvides ingresar el texto!')
        return

    update.message.reply_voice(
        Pocket(text=' '.join(context.args), voice='Zeina'), 
        quote=False)
    subprocess.call(data["ciao"], shell=True)

def ttsFr(update, context):
    if context.args[0] == '':
        update.message.reply_text('😟 ¡No olvides ingresar el texto!')
        return

    update.message.reply_voice(
        Pocket(text=' '.join(context.args), voice='Celine'), 
        quote=False)
    subprocess.call(data["ciao"], shell=True)

def ttsJp(update, context):
    if context.args[0] == '':
        update.message.reply_text('😟 ¡No olvides ingresar el texto!')
        return

    update.message.reply_voice(
        Pocket(text=' '.join(context.args), voice='Takumi'), 
        quote=False)
    subprocess.call(data["ciao"], shell=True)

def ttsMx(update, context):
    if context.args[0] == '':
        update.message.reply_text('😟 ¡No olvides ingresar el texto!')
        return

    update.message.reply_voice(
        Pocket(text=' '.join(context.args), voice='Mia'),
        quote=False)
    subprocess.call(data["ciao"], shell=True)

def ttsRu(update, context):
    if context.args[0] == '':
        update.message.reply_text('😟 ¡No olvides ingresar el texto!')
        return

    update.message.reply_voice(
        Pocket(text=' '.join(context.args), voice='Maxim'),
        quote=False)
    subprocess.call(data["ciao"], shell=True)
