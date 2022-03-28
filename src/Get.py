import sys
sys.path.append("../")
# f: fichier, s: subject_pronouns, v: verb, chk = self.check
# p: past or pp, end: self.ending, res: result of
"""
    Pour mieux cibler qu'un seul caractère à remplacer:
        inverser la chaine
        utiliser str.replace('old str','new inversed str',1) 
        inverser la chaine
"""

def data(f):
    res = None
    try:
        with open(f,"r") as fic:
            res = fic.read()
            res = res.splitlines()
    except:
        res = [f,] * 6 
    finally:
        return res
    
def check_progressive(v):
    if v[len(v) - 1] == 'e' and v[len(v) - 2] == 'i':
        v = v[::-1]
        v = v.replace('i','y',1)
        v = v.replace('e',"gni",1)
        return v[::-1]
    elif v[len(v) - 1] == 'e' and v[len(v) - 2] not in "be": # à ajouter si nécessaire
        v = v[::-1] 
        v = v.replace('e',"gni",1) 
        return v[::-1] 
    elif v[len(v) - 1] == 't' and v[len(v) - 2] in "aeiouy": # To start
        return v + "ting"
    elif v[len(v) - 1] == 'p' and v[len(v) - 2] not in "aeiouy": # To sleep
        return v + "ping"
    else:
        return v + "ing"

def check_perfect(p,v,chk):
    if p != v:
        return p
    elif chk: # To read
        return v
    elif v[len(v) - 1] == 'y' and v[len(v) - 2] not in "aeiouy": # To study
        v = v[::-1]
        v = v.replace('y',"dei",1)
        return v[::-1]
    elif v[len(v) - 1] == 'e':
        v = v[::-1]
        v = v.replace('e',"de",1)
        return v[::-1]
    elif v[len(v) - 1] == 'p':
        return v + "ped"
    elif v[len(v) - 1] == 'l':# cancelled
        return v + "led"
    else:
        return v + "ed"

def check_simple(v,end):
    if v[len(v) - 2:] in end or v[len(v) - 1] in end:
        return " " + v + "es"
    elif v[len(v) - 1] == 'y' and v[len(v) - 2] not in "aeiouy":
        v = v[::-1]
        v = v.replace('y',"sei",1)
        return " " + v[::-1]
    else:
        return " " + v + 's'

def lower_case(s):
    for  i in range(1,len(s)): # I reste tjrs en MAJ
        s[i] = s[i].replace(s[i],s[i].lower())   
    return s

def capitalize_case(s):
    for  i in range(len(s)):
        s[i] = s[i].replace(s[i],s[i].capitalize())   
    return s

def strip_case(s):
    for  i in range(len(s)):
        s[i] = s[i].replace(s[i],s[i].strip())
    return s
