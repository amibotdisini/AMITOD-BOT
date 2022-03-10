from time import sleep
from userbot import CMD_HELP
from userbot.events import register


@register(outgoing=True, pattern='^.sadboy(?: |$)(.*)')
async def typewriter(typew):
    typew.pattern_match.group(1)
    sleep(2)
    await typew.edit("`Pertama-tama kamu cantik`")
    sleep(2)
    await typew.edit("`Kedua kamu manis`")
    sleep(1)
    await typew.edit("`Dan yang terakhir adalah kamu bukan jodohku`")
# Create by myself @localheart


@register(outgoing=True, pattern='^.punten(?: |$)(.*)')
async def typewriter(typew):
    typew.pattern_match.group(1)
    await typew.edit("`\n┻┳|―-∩`"
                     "`\n┳┻|     ヽ`"
                     "`\n┻┳|    ● |`"
                     "`\n┳┻|▼) _ノ`"
                     "`\n┻┳|￣  )`"
                     "`\n┳ﾐ(￣ ／`"
                     "`\n┻┳T￣|`"
                     "\n**Njir Ngeri Abis Suhu🛐Tapi Sayang Lu Sombong..**")


@register(outgoing=True, pattern='^.lancau(?: |$)(.*)')
async def typewriter(typew):
    typew.pattern_match.group(1)
    await typew.edit("**Yus Si Paling Sombong☑️**")
    await typew.edit("**Yus Si Paling Sombong✅**")
    sleep(1)
    await typew.edit("**AmNi Si Paling Private☑️**")
    await typew.edit("**AmNi Si Paling Private✅**")
    sleep(2)
    await typew.edit("**Meki Ni Baik Tapi Kek Tolol☑️**")
    await typew.edit("**Meki Ni Baik Tapi Kek Tolol✅**")
    sleep(2)
    await typew.edit("**Mal Ni Si Paling Desah☑️**")
    await typew.edit("**Mal Ni Si Paling Desah✅**")
    sleep(2)
    await typew.edit("**Wan Ngentod Si Paling Admin!☑️**")
    await typew.edit("**Wan Ni Kang Mute + Kang Ban!✅**")
    sleep(2)
    await typew.edit("**Milo Kabur Si GakJelas!☑️**")
    await typew.edit("**Milo Kabur Si GakJelas!✅**")
    sleep(2)
    await typew.edit("**Asta Kuat Main Jubo☑️**")
    await typew.edit("**Asta Kuat Main Jubo✅**")
    sleep(2)
    await typew.edit("**Keen Si Ngeri☑️**")
    await typew.edit("**Keen Si Ngeri✅**")
    sleep(3)
    await typew.edit("**CUMA AMI SI PALING MURNI🗿!**")


@register(outgoing=True, pattern='^.lahk(?: |$)(.*)')
async def typewriter(typew):
    typew.pattern_match.group(1)
    await typew.edit("`Lahk, Lo tolol?`")
    sleep(1)
    await typew.edit("`Apa dongok?`")
    sleep(1)
    await typew.edit("`Gausah sok keras`")
    sleep(1)
    await typew.edit("`Gua ga ketrigger sama bocah baru nyemplung!`")


@register(outgoing=True, pattern='^.wah(?: |$)(.*)')
async def typewriter(typew):
    typew.pattern_match.group(1)
    await typew.edit("`Wahh, War nya keren bang`")
    sleep(2)
    await typew.edit("`Tapi, Yang gua liat, kok Kaya lawakan`")
    sleep(2)
    await typew.edit("`Oh iya, Kan lo badut 🤡`")
    sleep(2)
    await typew.edit("`Kosa kata pas ngelawak, Jangan di pake war bang`")
    sleep(2)
    await typew.edit("`Kesannya lo ngasih kita hiburan.`")
    sleep(2)
    await typew.edit("`Kasian badut🤡, Ga di hargain pengunjung, Eh lampiaskan nya ke Tele, Wkwkwk`")
    sleep(3)
    await typew.edit("`Dah sana cabut, Makasih hiburannya, Udah bikin Gua tawa ngakak`")

CMD_HELP.update({
    "rambot":
    "`.rambot`\
    \nUsage: menampilkan alive bot.\
    \n\n`.sadboy`\
    \nUsage: hiks\
    \n\n`.punten` ; `.geez`\
    \nUsage: misi."
})
