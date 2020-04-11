import aiofiles,json

def SetItem(self,Item):
    self.id = Item["id"]
    self.type = Item["type"]
    self.backendType = Item["backendType"]
    self.rarity = Item["rarity"]
    self.backendRarity = Item["backendRarity"]
    self.Names = Item["Names"]
    self.variants = Item["variants"]
    self.path = Item["path"]

async def getCosmetic(NameorId,Lang,Type):
    Cosmetics = json.loads(await (await aiofiles.open('Items.json', mode='r')).read())

    for Cosmetic in Cosmetics:
        if Cosmetic["id"].lower() == NameorId.lower() and Type.lower() == Cosmetic["backendType"].lower():
            return Cosmetic
        elif Cosmetic["Names"][Lang].lower() == NameorId.lower() and Type.lower() == Cosmetic["backendType"].lower():
            return Cosmetic

    for Cosmetic in Cosmetics:
        if Cosmetic["id"].lower().startswith(NameorId.lower()) and Type.lower() == Cosmetic["backendType"].lower():
            return Cosmetic
        elif Cosmetic["Names"][Lang].lower().startswith(NameorId.lower()) and Type.lower() == Cosmetic["backendType"].lower():
            return Cosmetic

    return None

async def GetSkin(NameorId,Lang="en"):
    return (await getCosmetic(NameorId,Lang,"AthenaCharacter"))

async def GetBackpack(NameorId,Lang="en"):
    return (await getCosmetic(NameorId,Lang,"AthenaBackpack"))

async def GetPickaxe(NameorId,Lang="en"):
    return (await getCosmetic(NameorId,Lang,"AthenaPickaxe"))

async def GetEmote(NameorId,Lang="en"):
    return (await getCosmetic(NameorId,Lang,"AthenaDance"))

async def GetEmoji(NameorId,Lang="en"):
    return (await getCosmetic(NameorId,Lang,"AthenaEmoji"))

async def GetPet(NameorId,Lang="en"):
    return (await getCosmetic(NameorId,Lang,"AthenaPetCarrier"))