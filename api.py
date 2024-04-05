from botocore.exceptions import BotoCoreError, ClientError
from contextlib import closing
from boto3 import Session
import subprocess
import datetime
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

        subprocess.call(f'{data["convert"]} -y', shell=True)
        
        voicenote = open('speech.ogg', 'rb')

        return voicenote

    else:
        print("Could not stream audio")
        sys.exit(-1)


def help(update, context):
    update.message.reply_text(
        """💻 *Comandos disponibles* 💻
• /start - _Lista comandos_
• /tts help - _Voces disponibles_
• /version - _Versión del bot y código fuente_
    """, parse_mode='Markdown')


def version(update, context):
    sourceCode = "https://github.com/CxrlosKenobi/TelegramTTS"
    kenobiUrl = 'https://github.com/CxrlosKenobi'
    albfrUrl = 'https://github.com/AlbFR'

    update.message.reply_text(
        "<b>TTS Bot v1.0\n</b>"
        f"<b>Código fuente: </b><a href='{sourceCode}'>GitHub</a>\n"
        f"<b>Colaboradores: </b><a href='{albfrUrl}'>AlbFR</a>"
    , parse_mode="HTML")

def log(update, context, voice):
    with open('logs.json', 'r') as file:
        data = json.load(file)
    data.append({
        'user': f"{update.message.from_user.first_name} {update.message.from_user.last_name}",
        'command': voice,
        'text': f"{' '.join(context.args)}"
    })
    with open('logs.json', 'w') as file:
        json.dump(data, file, indent=4)


def tts(update, context):
    try:
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

        if context.args[0] == '':
            update.message.reply_text('😟 ¡No olvides ingresar el texto!')
            return

        update.message.reply_voice(
            Pocket(
                text=' '.join(context.args),
                voice='Ricardo'
            ), 
            quote=False
        )
        log(update, context, 'Ricardo')
        subprocess.call(data["ciao"], shell=True)


    except IndexError:
        update.message.reply_text('😟 ¡No olvides ingresar el texto!')
        return    

def ttsCn(update, context):
    try:
        if context.args[0] == '':
            update.message.reply_text('😟 ¡No olvides ingresar el texto!')
            return

        update.message.reply_voice(
            Pocket(text=' '.join(context.args), voice='Zhiyu'), 
            quote=False)
        log(update, context, 'Zhiyu')
        subprocess.call(data["ciao"], shell=True)

    except IndexError:
        update.message.reply_text('😟 ¡No olvides ingresar el texto!')
        return

def ttsArb(update, context):
    try:
        if context.args[0] == '':
            update.message.reply_text('😟 ¡No olvides ingresar el texto!')
            return

        update.message.reply_voice(
            Pocket(text=' '.join(context.args), voice='Zeina'), 
            quote=False)
        log(update, context, 'Zeina')
        subprocess.call(data["ciao"], shell=True)

    except IndexError:
        update.message.reply_text('😟 ¡No olvides ingresar el texto!')
        return

def ttsFr(update, context):
    try:
        if context.args[0] == '':
            update.message.reply_text('😟 ¡No olvides ingresar el texto!')
            return

        update.message.reply_voice(
            Pocket(text=' '.join(context.args), voice='Celine'), 
            quote=False)
        log(update, context, 'Celine')
        subprocess.call(data["ciao"], shell=True)

    except IndexError:
        update.message.reply_text('😟 ¡No olvides ingresar el texto!')
        return

def ttsJp(update, context):
    try:
        if context.args[0] == '':
            update.message.reply_text('😟 ¡No olvides ingresar el texto!')
            return

        update.message.reply_voice(
            Pocket(text=' '.join(context.args), voice='Takumi'), 
            quote=False)
        log(update, context, 'Takumi')
        subprocess.call(data["ciao"], shell=True)

    except IndexError:
        update.message.reply_text('😟 ¡No olvides ingresar el texto!')
        return

def ttsMx(update, context):
    try:
        if context.args[0] == '':
            update.message.reply_text('😟 ¡No olvides ingresar el texto!')
            return

        update.message.reply_voice(
            Pocket(text=' '.join(context.args), voice='Mia'), 
            quote=False)
        log(update, context, 'Mia')
        subprocess.call(data["ciao"], shell=True)

    except IndexError:
        update.message.reply_text('😟 ¡No olvides ingresar el texto!')
        return

def ttsRu(update, context):
    try:
        if context.args[0] == '':
            update.message.reply_text('😟 ¡No olvides ingresar el texto!')
            return

        update.message.reply_voice(
            Pocket(text=' '.join(context.args), voice='Maxim'), 
            quote=False)
        log(update, context, 'Maxim')
        subprocess.call(data["ciao"], shell=True)

    except IndexError:
        update.message.reply_text('😟 ¡No olvides ingresar el texto!')
        return
