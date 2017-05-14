#-*-coding:utf-8-*-

# Description:
# Dans ce programme, un automate est une classe qui consiste 4 membres:
# "stats" est une liste de tous les états dans l'automate.
# "vocabulaire" est un string qui représente le vocabulaire,
#     par exemple, "ab" veut dire que l'automate peut recevoir soit 'a', soit 'b'
# "currentStat" indique que l'automate est actuellement dans quel état.
# "initStat" indique l'état initial de cet automate.


# Un état est une classe qui a 3 membres:
# "name" est le nom de cet état, doit être unique!
# "transition" est l'ensemble des règles de transition pour l'état courant,
#    est sous forme de dicionnaire, par exemple:
#
#    # transition = {
#    #     "a": "B",
#    #     "b": "C",
#    # }
#
#    C'est à dire losqu'on reçoit 'a', l'automate va se déplacer vers l'état "B", et si on
#    reçoit 'B', l'automate va se déplacer vers l'état "C".
# "isFinal" indique si l'état est un état final.


from exceptions import *
import sys

# La classe de NFA est très similaire que la classe dee DFA.
# Sauf pour le membre "transition" de son état, c'est une liste en remplaçant le dictionnaire.
# C'est parce que le dictionnaire ne permet pas avoir les clés avec les mêmes valeurs.

class NFA:
    class stat:
        def __init__(self):
            self.name = ""
            self.transition = []
            # e.g. transition = [('a', 'A'), ('a', 'B')]
            self.isFinal = False

    def __init__(self):
        self.stats = []
        self.vocabulaire = ""
        self.currentStat = None
        self.initStat = None

    def getPosition(self, stat_name):
        for each in self.stats:
            if each.name == stat_name:
                return each

    def input_check(self, input_char):
        if input_char not in self.vocabulaire:
            raise TypeError("Invalid Input, not found in current vocabulary.")

    def stat_name_check(self, name):
        if not isinstance(name, str):
            raise TypeError("The name of a stat must be a string!")
        if name == "":
            raise Exception("The name of a stat must not be void!")
        for each in self.stats:
            if each.name == name:
                raise Exception("The stat name already exists, please choose another name.")

    def update_vocabulaire(self, vocabulaire):
        if isinstance(vocabulaire, str):
            self.vocabulaire = vocabulaire
        else:
            raise TypeError("Invalid Input.")

    def addStat(self, name, transition = dict(), isFinal = False):
        self.stat_name_check(name)

        newstat = self.stat()
        newstat.name = name
        newstat.transition = transition
        newstat.isFinal = isFinal
        self.stats.append(newstat)
        del newstat


class Automate:
    class stat:
        def __init__(self):
            self.name = ""
            self.transition = dict()
            self.isFinal = False

    def __init__(self):
        self.stats = []
        self.vocabulaire = ""
        self.currentStat = None
        self.initStat = None

    def getPosition(self, stat_name):
        for each in self.stats:
            if each.name == stat_name:
                return each
        raise Exception("Stat name not found.")

    def input_check(self, input_char):
        if input_char not in self.vocabulaire:
            raise TypeError("Invalid Input, not found in current vocabulary.")

    def stat_name_check(self, name):
        if not isinstance(name, str):
            raise TypeError("The name of a stat must be a string!")
        if name == "":
            raise Exception("The name of a stat must not be void!")
        for each in self.stats:
            if each.name == name:
                raise Exception("The stat name already exists, please choose another name.")

    def update_vocabulaire(self, vocabulaire):
        if isinstance(vocabulaire, str):
            self.vocabulaire = vocabulaire
        else:
            raise TypeError("Invalid Input.")

    def move(self, char):
        sys.stdout.write("Receive \'" + char + "\'. ")
        sys.stdout.write("Move from current stat: " + self.currentStat.name)
        self.currentStat = self.getPosition(self.currentStat.transition[char])
        sys.stdout.write(" to next stat: " + self.currentStat.name + "\n")
        if self.currentStat.isFinal:
            print "Reach Final Stat."

    def recognize(self, receive = ""):
        print "The initial stat is: " + self.currentStat.name
        for each in receive:
            self.input_check(each)
            self.move(each)

    def addStat(self, name, transition = dict(), isFinal = False):
        self.stat_name_check(name)

        newstat = self.stat()
        newstat.name = name
        newstat.transition = transition
        newstat.isFinal = isFinal
        self.stats.append(newstat)
        del newstat

    @staticmethod
    def determiniser(nfa):
        dfa = Automate()
        dfa.vocabulaire = nfa.vocabulaire

        stats_name_set = []
        stats_name_set.append(nfa.initStat.name)

        index = 0
        while True:
            if index < stats_name_set.__len__():
                current_stat_name = stats_name_set[index]
                current_stat_transition = dict()
                for each_char in dfa.vocabulaire:
                    name_composantes = []
                    name = ""
                    for each_stat_name in current_stat_name:
                        each_stat = nfa.getPosition(each_stat_name)
                        for each_tran in each_stat.transition:
                            if each_tran[0] == each_char:
                                name_composantes.append(each_tran[1])
                        for each in name_composantes:
                            if each not in name:
                                name += each
                    name = ''.join(sorted(name))
                    if name not in stats_name_set:
                        stats_name_set.append(name)
                    current_stat_transition.update({each_char : name})

                current_stat_isFinal = False
                for each in current_stat_name:
                    if nfa.getPosition(each).isFinal == True:
                        current_stat_isFinal = True
                        break
                dfa.addStat(current_stat_name, current_stat_transition, current_stat_isFinal)
                index = index + 1
            else:
                break

        return dfa


if __name__ == '__main__':
    # Les codes suivantes permettent de construire un automate fini déterministe
    # qui reconnait le mot "baab".

    automate = Automate()
    automate.vocabulaire = "ab"
    transition_A = {"a": "A", "b": "B"}
    automate.addStat("A", transition_A, False)
    transition_B = {"a": "C", "b": "B"}
    automate.addStat("B", transition_B, False)
    transition_C = {"a": "D", "b": "B"}
    automate.addStat("C", transition_C, False)
    transition_D = {"a": "A", "b": "E"}
    automate.addStat("D", transition_D, False)
    transition_E = {"a": "E", "b": "E"}
    automate.addStat("E", transition_E, True)

    automate.initStat = automate.stats[0]
    automate.currentStat = automate.initStat

    automate.recognize("baab")
    # print automate.initStat.name

    # automate.recognize("aaaa")

    nfa = NFA()
    nfa.vocabulaire = "ab"
    ntA = [("a", "A"), ("b", "A"), ("b", "B")]
    nfa.addStat("A", ntA, False)
    ntB = [("a", "C")]
    nfa.addStat("B", ntB, False)
    ntC = [("a", "D")]
    nfa.addStat("C", ntC, False)
    ntD = [("b", "E")]
    nfa.addStat("D", ntD, False)
    ntE = [("a", "E"), ("b", "E")]
    nfa.addStat("E", ntE, True)
    nfa.initStat = nfa.stats[0]

    dfa = Automate.determiniser(nfa)
