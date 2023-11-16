class GrammarStats:
    def __init__(self):
        self.checks_undertaken = 0
        self.checks_passed = 0
  
    def check(self, text):
        if text == "":
            raise Exception("No text has been inputted to check grammar")
        self.checks_undertaken += 1
        result = text[0] == text[0].upper() and text[-1] in ".!?"
        if result:
            self.checks_passed += 1
        return result
  
    def percentage_good(self):
        if self.checks_undertaken == 0:
            raise Exception("No texts have been checked")
        return round(self.checks_passed / self.checks_undertaken * 100)
