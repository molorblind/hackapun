class Homonyms:
  def __init__(self):
    self.homs = [h.split(',') for h in
        open("data/homophones.csv").read().split('\n')]

  def homonyms(self, word):
    return [hs for hs in self.homs if any([h for h in hs if word == h])]
