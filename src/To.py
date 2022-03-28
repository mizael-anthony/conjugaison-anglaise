import sys
sys.path.append("../")
import src.Get as Get # (pour la fonction principale)
# import Get # (test du module)

# s: subject_pronouns, res: result of, is_present_simple = est-ce present simple?
# aff: Affirmative(Form), to_not_contracted = ne pas contracté?

def conjugate(s,v,is_present_simple = False):
    for i in range(len(s)):
        if i == 2 and is_present_simple:
            continue
        else:
            s[i] += " " + v
    return s

def aff(s,v):
    res = Get.data(v)
    for i in range(len(s)):
        s[i] += res[i]
    return s

def neg(s,to_not_contracted):
    neg = str()
    if to_not_contracted:
        neg = " not"
    else:
        neg = "n't" 
    for i in range(len(s)):
        s[i] += neg
    return s

def interro(s,v):
    res = Get.capitalize_case(Get.strip_case(Get.data(v)))
    s = Get.lower_case(s)
    for i in range(len(s)):
        res[i] += " " + s[i]
    return res 

def interro_neg(s,v,to_not_contracted):
    res = neg(Get.capitalize_case(Get.strip_case(Get.data(v))),to_not_contracted)
    s = Get.lower_case(s)
    for i in range(len(s)):
        res[i] += " " + s[i]
    return res  

def show(s):
    for i in range(len(s)):
        print(s[i])
