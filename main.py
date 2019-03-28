#!/venv/bin/env python
from mem import Process
from offset import Offset
from time import sleep
import unit


if __name__ == '__main__':
    process = Process()
    offset = Offset()
    base = process.readuint4(offset.ObjectManager.ManagerBase)
    playerAddress = None

    curObj = process.readuint4(base + offset.ObjectManager.FirstObj)
    nextObj = curObj
    player_guid = process.readlong(base + offset.ObjectManager.PlayerGuid)
    while curObj != 0 and curObj % 2 == 0:
        guid = process.readlong(curObj + offset.ObjectManager.CurObjGuid)
        type = process.readuint4(curObj + offset.ObjectManager.ObjType)
        descriptor = process.readuint4(curObj + offset.ObjectManager.DescriptorOffset)
        if playerAddress is not None:
            distance = unit.distance_ato_b(playerAddress, curObj, process)
            player = unit.is_player(curObj, process)
            unit_ = unit.is_unit(curObj, process)
            if unit:
                name = unit.name(curObj, process)
            if player or unit_:
                print("Distance of " + str(curObj) + " from Player is " + str(distance))
        if guid == player_guid:
            print("Player : " + str(curObj) + " GUID : " + str(guid) + "\nDescriptor : " + str(descriptor))
            health = process.readuint4(curObj + offset.GameObject.PosX)
            print("CorpseX : " + str(health))
            playerAddress = curObj
        nextObj = process.readuint4(curObj + offset.ObjectManager.NextObj)
        curObj = nextObj
    process.cont()
