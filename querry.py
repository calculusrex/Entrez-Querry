from Bio import Entrez



Entrez.email = 'piton.portocaliu@gmail.com'


handle = Entrez.esearch(db='gene', term='csk-1')
record = Entrez.read(handle)
handle.close()

