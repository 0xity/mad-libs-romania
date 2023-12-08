class MadLib:
    def __init__(self):
        self.wordlist = ["sub1", "sub2", "verb1", "sub3", "verb2", "sub4"]

    def sugi(self):
        self.wordlist[0] = input("Scrie o locație: ")
        self.wordlist[1] = input("Scrie un obiect: ")
        self.wordlist[2] = input("Scrie un verb: ")
        self.wordlist[3] = input("Scrie o jucărie / persoană: ")
        self.wordlist[4] = input("Scrie un verb: ")
        self.wordlist[5] = input("Scrie o locație / stare: ")
        sentence = (f"Ana a mers la {self.wordlist[0]} "
                    f"si a luat {self.wordlist[1]} "
                    f"apoi a {self.wordlist[2]} "
                    f"și s-a jucat cu {self.wordlist[3]} "
                    f"apoi a {self.wordlist[4]} "
                    f"pana la {self.wordlist[5]} ")
        return sentence


if __name__ == "__main__":
    Madlib = MadLib()
    print(MadLib.sugi(Madlib))
