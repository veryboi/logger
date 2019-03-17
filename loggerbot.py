# -*- coding: utf-8 -*-
import discord
import asyncio
import aiofiles
from os.path import isdir, join
from os import makedirs
from re import sub
import os

logFolder = "Userlogs"  # Folder with log files.
fileExt = ".txt"  # The extension of the userlogs, if changed after logs are created multiple files will be created.
avoidMsg = ["Image made with", "Loading...", "t!"]  # Avoids messages containing one of these substrings.
cmdPrefix = '$'  # The prefix to the commands.
muteChar = '£'  # Place this char infront of message to not store message.
tokenKey = str(os.getenv('token'))
seperationChar = '\n'  # The charactor that seperates new messages. Blank for none.

client = discord.Client()
print("Initiating logger")


@client.event
async def on_ready():
    print("Logged in as: " + client.user.name)
    print(client.user.id)
    print("Command prefix: " + repr(cmdPrefix))
    print("Seperation char: " + repr(seperationChar))
    print("Mute char: " + repr(muteChar))
    print("Log folder: {0}, log file extension: {1}".format(logFolder, fileExt))
    print("-------------")
    if not (isdir(logFolder)):
        makedirs(logFolder)
        print("Created log folder: " + logFolder)


@client.event
async def on_message(message):
    if (message.author.bot):
        return False
    try:
        i = 0;
        msgContained = False;
        Status = "[Not Logged] ";
        Nickname = "";
        while i < len(avoidMsg):
            if (avoidMsg[i] in message.content):
                print("Avoiding message: {0} | By {1}".format(message.content.replace("\n", " "), message.author.name))
                msgContained = True
            i += 1
        if not (msgContained):
            Targetfile = join(logFolder, message.author.name + fileExt)  # Combines paths with relevant variables.
            MsgText = sub("[^a-zA-Z -<>.,':]+", "",
                          message.content.replace("\n", " ")) + ' '  # Sorts out not supported-chars.
            if (len(MsgText) < 1):
                return False
            if not (message.content[0] == muteChar):
                Status = ""
                async with aiofiles.open(Targetfile, mode='a') as f:
                    await f.write(MsgText + seperationChar)
            if not (message.author.name == message.author.display_name):
                Nickname = "({0})".format(str(message.author.display_name))
            print('{1}{2} {3}said: {0}'.format(MsgText, str(message.author.name), Nickname, Status))
            if int(message.author.id) == 269881662836441088:
                await client.add_reaction(message, '⭐')
            elif int(message.author.id) == 305496297727721472:
                await client.add_reaction(message, ':joh:555844681196634114')
                await client.add_reaction(message, ':thot:556959362107703329')
                await client.add_reaction(message, ':juan:556959325256548362')
            elif int(message.author.id) == 480075856681893898:
                await client.add_reaction(message, ':justice:556668050007654409')
            elif int(message.author.id) == 198671632095510529:
                await client.add_reaction(message, ':orz:545130316067635200')
            elif int(message.author.id) == 539585349374967809:
                await client.add_reaction(message, '🏳️‍🌈')
            elif int(message.author.id) == 305517731229204481:
                await client.add_reaction(message, ':izzy:556668288998965248')
            elif int(message.author.id) == 489268166334218263:
                await client.add_reaction(message, '🆒')
            elif int(message.author.id) == 438142672893640707:
                await client.add_reaction(message, '👺')

            await client.send_message(client.get_channel('530221804069978114'),
                                      '{1}{2} {3}said: {0}'.format(MsgText, str(message.author.name), Nickname, Status))
            if int(message.channel.id) == 556912837646352395:
                await client.send_message(client.get_channel('532704877550239746'),
                                          str(message.content))
    except Exception as e:
        print("Exception: " + str(e))

    if message.content.startswith(cmdPrefix + "ping"):  # Used as a template for commands
        if (message.author.bot):
            return False
        print("Ping recieved, responding")
        counter = 0
        tmp = await client.send_message(message.channel, "Pong")
        async for log in client.logs_from(message.channel, limit=100):
            if log.author == message.author:
                counter += 1


async def list_servers():
    await client.wait_until_ready()
    while not client.is_closed:
        print("Current servers:")
        for server in client.servers:
            print(server.name)
            print(server.id)
        await asyncio.sleep(600)


client.loop.create_task(list_servers())
client.run(tokenKey)
