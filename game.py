from random import *

import db


class Game:
    winning = None

    @staticmethod
    def getWinningNumber():
        Game.winning = randint(0, 36)

    @staticmethod
    def play(var):
        Game.getWinningNumber()
        arr=var.split("&")
        number=(arr[0].split("="))[1]
        cred = (arr[1].split("="))[1]
        user=(arr[2].split("="))[1]
        isInt=True


        try:
            n=int(number)
        except:
            isInt=False


        if isInt:
            if n==Game.winning:
                s = f'credits={str(int(int(cred) / 1))}&username={user}'
                db.Db.addCredits(s)
                return int(int(cred)/1)
            else:
                s = f'credits=-{cred}&username={user}'
                db.Db.addCredits(s)
                return -1

        else:
            if number == "1rw":
                win=False
                i=1
                while i<=34:
                    if Game.winning==i:
                        win=True
                        break
                    i+=3
                if win:
                    s = f'credits={str(int(int(cred) / 4))}&username={user}'
                    db.Db.addCredits(s)
                    return int(int(cred)/4)
                else:
                    s = f'credits=-{cred}&username={user}'
                    db.Db.addCredits(s)
                    return -1

            elif number == "2rw":
                win = False
                i = 2
                while i <= 35:
                    if Game.winning == i:
                        win = True
                        break
                    i += 3
                if win:
                    s = f'credits={str(int(int(cred) / 4))}&username={user}'
                    db.Db.addCredits(s)
                    return int(int(cred)/4)
                else:
                    s = f'credits=-{cred}&username={user}'
                    db.Db.addCredits(s)
                    return -1


            elif number == "3rw":
                win = False
                i = 3
                while i <= 36:
                    if Game.winning == i:
                        win = True
                        break
                    i += 3
                if win:
                    s = 'credits=' + str(int(int(cred) / 4)) + '&username=' + user
                    db.Db.addCredits(s)
                    return int(int(cred)/4)
                else:
                    s = f'credits=-{cred}&username={user}'
                    db.Db.addCredits(s)
                    return -1

            elif number=="1to12":
                if 1<=Game.winning and Game.winning<=12:
                    s = 'credits=' + str(int(int(cred) / 4)) + '&username=' + user
                    db.Db.addCredits(s)
                    return int(int(cred)/4)
                else:
                    s = f'credits=-{cred}&username={user}'
                    db.Db.addCredits(s)
                    return -1
            elif number == "1to18":
                if 1 <= Game.winning and Game.winning <= 18:
                    s = 'credits=' + str(int(int(cred) / 8)) + '&username=' + user
                    db.Db.addCredits(s)
                    return int(int(cred)/8)
                else:
                    s = f'credits=-{cred}&username={user}'
                    db.Db.addCredits(s)
                    return -1
            elif number == "even":
                if Game.winning%2==0:
                    s = 'credits=' + str(int(int(cred) / 8)) + '&username=' + user
                    db.Db.addCredits(s)
                    return int(int(cred)/8)
                else:
                    s = f'credits=-{cred}&username={user}'
                    db.Db.addCredits(s)
                    return -1
            elif number == "red":
                if Game.winning in {1,3,5,7,9,12,14,16,18,19,21,23,25,27,30,32,34,36}:
                    s = 'credits=' + str(int(int(cred) / 8)) + '&username=' + user
                    db.Db.addCredits(s)
                    return int(int(cred)/8)
                else:
                    s = f'credits=-{cred}&username={user}'
                    db.Db.addCredits(s)
                    return -1
            elif number == "blk":
                if Game.winning not in {1,3,5,7,9,12,14,16,18,19,21,23,25,27,30,32,34,36}:
                    s = 'credits=' + str(int(int(cred) / 8)) + '&username=' + user
                    db.Db.addCredits(s)
                    return int(int(cred)/8)
                else:
                    s = f'credits=-{cred}&username={user}'
                    db.Db.addCredits(s)
                    return -1
            elif number == "13to24":
                if 13<=Game.winning and Game.winning<=24:
                    s = f'credits={str(int(int(cred) / 4))}&username={user}'
                    db.Db.addCredits(s)
                    return int(int(cred)/4)
                else:
                    s = f'credits=-{cred}&username={user}'
                    db.Db.addCredits(s)
                    return -1
            elif number == "odd":
                if Game.winning % 2 != 0:
                    s = 'credits=' + str(int(int(cred) / 8)) + '&username=' + user
                    db.Db.addCredits(s)
                    return int(int(cred)/8)
                else:
                    s = f'credits=-{cred}&username={user}'
                    db.Db.addCredits(s)
                    return -1
            elif number == "19to36":
                if 19 <= Game.winning and Game.winning <= 36:
                    s = 'credits=' + str(int(int(cred) / 8)) + '&username=' + user
                    db.Db.addCredits(s)
                    return int(int(cred)/8)
                else:
                    s = f'credits=-{cred}&username={user}'
                    db.Db.addCredits(s)
                    return -1
            elif number == "25to36":
                if 25 <= Game.winning and Game.winning <= 36:
                    s = 'credits=' + str(int(int(cred) / 4)) + '&username=' + user
                    db.Db.addCredits(s)
                    return int(int(cred)/4)
                else:
                    s = f'credits=-{cred}&username={user}'
                    db.Db.addCredits(s)
                    return -1
