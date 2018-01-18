import session
import player
import master
import user
import json


def main():

    users = []
    users.append(user.User('u1', 'u1@email.com', 1))
    users.append(user.User('u2', 'u2@email.com', 2))
    users.append(user.User('u3', 'u3@email.com', 3))

    player1 = player.Player("fulano", "pedreiro", "humano", "story", 1, 1)
    player2 = player.Player("ciclano", "cozinheiro", "humano", "story", 1, 2)
    player3 = player.Player("joao", "knight", "humano", "story", 1, 3)

    players = []
    players.append(player1)
    players.append(player2)
    players.append(player3)

    master1 = master.Master(None, None, None, None, None, None)

    newsession = session.Session(1, players, master1, users, 'teste')
    newsession.setMasterConfig()
    newsession.getMasterConfig()

    print(json.dumps(newsession.toObject()))


main()
