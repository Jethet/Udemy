#Given a sentence, return a sentence with the words reversed

def rev_sent(sent):
    sent_rev = sent.split()
    sent_rev.reverse()
    return sent_rev

print(rev_sent("Whatever you want"))
