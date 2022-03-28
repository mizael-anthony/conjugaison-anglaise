
import src.Get as Get
import src.To as To
import include.Initial as Initial


class Affirmative(Initial.Form):
    def __init__(self,verb):
        Initial.Form.__init__(self,verb)

    def present_simple(self):
        if self.verb == "be":
            return To.aff(self.subject_pronouns,self.aux[0])
        if self.verb == "have":
            return To.aff(self.subject_pronouns,self.aux[1])
        self.subject_pronouns[2] += Get.check_simple(self.verb,self.ending)
        return To.conjugate(self.subject_pronouns,self.verb,True)
        
    def present_progressive(self):
        self.verb = Get.check_progressive(self.verb)
        self.subject_pronouns = To.aff(self.subject_pronouns,self.aux[0])
        return To.conjugate(self.subject_pronouns,self.verb)
 
    def present_perfect(self):
        self.verb = Get.check_perfect(self.pp,self.verb,self.check)
        self.subject_pronouns = To.aff(self.subject_pronouns,self.aux[1])
        return To.conjugate(self.subject_pronouns,self.verb)

    def past_simple(self):
        if self.verb == "be":
            return To.aff(self.subject_pronouns,self.aux[3])
        self.verb = Get.check_perfect(self.past,self.verb,self.check)
        return To.conjugate(self.subject_pronouns,self.verb)

    def past_progressive(self):
        self.verb = Get.check_progressive(self.verb)
        self.subject_pronouns = To.aff(self.subject_pronouns,self.aux[3])
        return To.conjugate(self.subject_pronouns,self.verb)

    def past_perfect(self):
        self.verb = Get.check_perfect(self.pp,self.verb,self.check)
        self.subject_pronouns = To.aff(self.subject_pronouns,self.aux[4])
        return To.conjugate(self.subject_pronouns,self.verb)

    def future(self):
        self.subject_pronouns = To.aff(self.subject_pronouns,self.aux[6])
        return To.conjugate(self.subject_pronouns,self.verb)

    def present_conditional(self):
        self.subject_pronouns = To.aff(self.subject_pronouns,self.aux[8])
        return To.conjugate(self.subject_pronouns,self.verb)
    
    def past_conditional(self):
        self.verb = Get.check_perfect(self.pp,self.verb,self.check)
        self.subject_pronouns = To.aff(self.subject_pronouns,self.aux[10])
        return To.conjugate(self.subject_pronouns,self.verb)


class Negative(Initial.Form):
    def __init__(self,verb):
        Initial.Form.__init__(self,verb)
        
    def present_simple(self):
        if self.verb == "be":
            return To.neg(To.aff(self.subject_pronouns,self.aux[0]),True)
        if self.verb == "have":
            return To.neg(To.aff(self.subject_pronouns,self.aux[1]),True)
        if self.verb == "do":
            return To.neg(To.aff(self.subject_pronouns,self.aux[2]),True)
        self.subject_pronouns = To.neg(To.aff(self.subject_pronouns,self.aux[2]),False)
        return To.conjugate(self.subject_pronouns,self.verb)
    
    def present_progressive(self):
        self.verb = Get.check_progressive(self.verb)
        self.subject_pronouns = To.neg(To.aff(self.subject_pronouns,self.aux[0]),True)
        return To.conjugate(self.subject_pronouns,self.verb)

    def present_perfect(self):
        self.verb = Get.check_perfect(self.pp,self.verb,self.check)
        self.subject_pronouns = To.neg(To.aff(self.subject_pronouns,self.aux[1]),True)
        return To.conjugate(self.subject_pronouns,self.verb)

    def past_simple(self):
        if self.verb == "be":
            return To.neg(To.aff(self.subject_pronouns,self.aux[3]),True)
        if self.verb == "do":
            return To.neg(To.aff(self.subject_pronouns,self.aux[5]),False)
        self.subject_pronouns = To.neg(To.aff(self.subject_pronouns,self.aux[5]),False)
        return To.conjugate(self.subject_pronouns,self.verb)

    def past_progressive(self):
        self.verb = Get.check_progressive(self.verb)
        self.subject_pronouns = To.neg(To.aff(self.subject_pronouns,self.aux[3]),True)
        return To.conjugate(self.subject_pronouns,self.verb)

    def past_perfect(self):
        self.verb = Get.check_perfect(self.pp,self.verb,self.check)
        self.subject_pronouns = To.neg(To.aff(self.subject_pronouns,self.aux[4]),True)
        return To.conjugate(self.subject_pronouns,self.verb)

    def future(self):
        self.subject_pronouns = To.aff(self.subject_pronouns,self.aux[7])
        return To.conjugate(self.subject_pronouns,self.verb)       
         
    def present_conditional(self):
        self.subject_pronouns = To.aff(self.subject_pronouns,self.aux[9])
        return To.conjugate(self.subject_pronouns,self.verb)
    
    def past_conditional(self):
        self.verb = Get.check_perfect(self.pp,self.verb,self.check)
        self.subject_pronouns = To.aff(self.subject_pronouns,self.aux[11])
        return To.conjugate(self.subject_pronouns,self.verb)


class Interrogative(Initial.Form):
    def __init__(self,verb):
        Initial.Form.__init__(self,verb)
        
    def present_simple(self):
        if self.verb == "be":
            return To.interro(self.subject_pronouns,self.aux[0])
        if self.verb == "have":
            return To.interro(self.subject_pronouns,self.aux[1])
        self.subject_pronouns = To.interro(self.subject_pronouns,self.aux[2])
        return To.conjugate(self.subject_pronouns,self.verb)

    def present_progressive(self):
        self.verb = Get.check_progressive(self.verb)
        self.subject_pronouns = To.interro(self.subject_pronouns,self.aux[0])
        return To.conjugate(self.subject_pronouns,self.verb)

    def present_perfect(self):
        self.verb = Get.check_perfect(self.pp,self.verb,self.check)
        self.subject_pronouns = To.interro(self.subject_pronouns,self.aux[1])
        return To.conjugate(self.subject_pronouns,self.verb)

    def past_simple(self):
        if self.verb == "be":
            return To.interro(self.subject_pronouns,self.aux[3])
        if self.verb == "have":
            return To.interro(self.subject_pronouns,self.aux[4])
        self.subject_pronouns = To.interro(self.subject_pronouns,self.aux[5])
        return To.conjugate(self.subject_pronouns,self.verb)

    def past_progressive(self):
        self.verb = Get.check_progressive(self.verb)
        self.subject_pronouns = To.interro(self.subject_pronouns,self.aux[3])
        return To.conjugate(self.subject_pronouns,self.verb)
    
    def past_perfect(self):
        self.verb = Get.check_perfect(self.pp,self.verb,self.check)
        self.subject_pronouns = To.interro(self.subject_pronouns,self.aux[4])
        return To.conjugate(self.subject_pronouns,self.verb)
      
    def future(self):
        self.subject_pronouns = To.interro(self.subject_pronouns,self.aux[12])
        return To.conjugate(self.subject_pronouns,self.verb)

    def present_conditional(self):
        self.subject_pronouns = To.interro(self.subject_pronouns,self.aux[13])
        return To.conjugate(self.subject_pronouns,self.verb)

    def past_conditional(self):
        self.verb = Get.check_perfect(self.pp,self.verb,self.check)
        self.subject_pronouns = To.interro(self.subject_pronouns,self.aux[14])
        return To.conjugate(self.subject_pronouns,self.verb)


class InterroNegative(Initial.Form):
    def __init__(self,verb):
        Initial.Form.__init__(self,verb)
        
    def present_simple(self):
        if self.verb == "be":
            return To.neg(To.interro(self.subject_pronouns,self.aux[0]),True)
        if self.verb == "have":
            return To.neg(To.interro(self.subject_pronouns,self.aux[1]),True)
        self.subject_pronouns = To.interro_neg(self.subject_pronouns,self.aux[2],False)
        return To.conjugate(self.subject_pronouns,self.verb)

    def present_progressive(self):
        self.verb = Get.check_progressive(self.verb)
        self.subject_pronouns = To.interro_neg(self.subject_pronouns,self.aux[0],True)
        return To.conjugate(self.subject_pronouns,self.verb)

    def present_perfect(self):
        self.verb = Get.check_perfect(self.pp,self.verb,self.check)
        self.subject_pronouns = To.interro_neg(self.subject_pronouns,self.aux[1],True)
        return To.conjugate(self.subject_pronouns,self.verb)

    def past_simple(self):
        if self.verb == "be":
            return To.neg(To.interro(self.subject_pronouns,self.aux[3]),True)
        elif self.verb == "have":
            return To.neg(To.interro(self.subject_pronouns,self.aux[4]),True)
        self.subject_pronouns = To.interro_neg(self.subject_pronouns,self.aux[5],False)
        return To.conjugate(self.subject_pronouns,self.verb)

    def past_progressive(self):
        self.verb = Get.check_progressive(self.verb)
        self.subject_pronouns = To.interro_neg(self.subject_pronouns,self.aux[3],True)
        return To.conjugate(self.subject_pronouns,self.verb)

    def past_perfect(self):
        self.verb = Get.check_perfect(self.pp,self.verb,self.check)
        self.subject_pronouns = To.interro_neg(self.subject_pronouns,self.aux[4],True)
        return To.conjugate(self.subject_pronouns,self.verb)

    def future(self):
        self.subject_pronouns = To.interro(self.subject_pronouns,self.aux[7])
        return To.conjugate(self.subject_pronouns,self.verb)

    def present_conditional(self):
        self.subject_pronouns = To.interro(self.subject_pronouns,self.aux[9])
        return To.conjugate(self.subject_pronouns,self.verb)
    
    def past_conditional(self):
        self.verb  = Get.check_perfect(self.pp,self.verb,self.check)
        self.subject_pronouns = To.interro(self.subject_pronouns,self.aux[11])
        return To.conjugate(self.subject_pronouns,self.verb)