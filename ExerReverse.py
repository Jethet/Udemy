#Given a sentence, return a new sentence with the words reversed

def rev_sent(sent):
    sent_rev = sent.split()
    sent_rev.reverse()
    sent_rev = ' '.join(sent_rev)
    return sent_rev

print(rev_sent("Whatever you want"))
