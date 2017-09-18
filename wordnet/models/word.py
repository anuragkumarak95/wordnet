'''Author Anurag Kumar 13 Sept, 2017

This module is a Word entity.
--
'''

class Word():
    ''' Word-Entity

    Attributes
    --
    w :             word itself
    bkwrd_links :   words which have this word as their relational word.
    frwrd_links :   words which are realtional to this word.

    '''
    def __init__(self,w,b_links=None,f_links=None):
        self.w = w
        self.bkwrd_links = b_links if b_links else set([]) # not being used for now.
        self.frwrd_links = f_links if f_links else set([])
    
    # getters and setters
    def getw(self):
        return self.w

    def setw(self,w):
        self.w = w

    def getbkwrd_links(self):
        return self.bkwrd_links

    def setbkwrd_links(self,b_links):
        self.bkwrd_links = b_links

    def getfrwrd_links(self):
        return self.frwrd_links

    def setfrwrd_links(self,f_links):
        self.frwrd_links = f_links

    # helper methods
    def addtobkwrd_links(self, links):
        self.bkwrd_links.update(links)

    def addtofrwrd_links(self, links):
        self.frwrd_links.update(links)
