from typing import Set,Tuple,Type,Optional,Callable
from albion_data import get_price
import operator

class Expr:

    a = None
    b = None
    value = None
    func = None
    reqs: Set[Tuple[str]]

    def __init__(self, a, b, func):
        self.a = a
        self.b = b
        self.func = func
        self.get_req()
        if getattr(self.a,"value",True)!=None and getattr(self.b,"value",True)!=None:
            self.eval()

    def get_req(self):
        self.reqs = set()
        if isinstance(self.a,Expr):
            self.reqs.update(self.a.reqs)
        if isinstance(self.b,Expr):
            self.reqs.update(self.b.reqs)

    def get_params(self):
        items = set()
        locations = set()
        qualities = set()
        for entry in self.reqs:
            items.update([entry[0]])
            locations.update([entry[1]])
            qualities.update([entry[2]])
        return items,locations,qualities
    
    def get_data(self):
        items,locations,qualities = self.get_params()
        return get_price(items,locations,qualities)

    def get(self,data):
        arg1 = self.a.eval(data) if isinstance(self.a,Expr) else self.a
        arg2 = self.b.eval(data) if isinstance(self.b,Expr) else self.b
        if arg2:
            return self.func(arg1,arg2)
        elif arg1:
            return self.func(arg1)
        else:
            return 0

    def eval(self, data=None,forced=False):
        if data == None:
            if self.value:
                return self.value
            #not forced,a.value and b.value not None and self not a Var
            if (not forced) and \
                getattr(self.a,"value",True)!=None and \
                getattr(self.b,"value",True)!=None and \
                (not isinstance(self,Var)):
                    data = None
            else:
                data = self.get_data()
        self.value = self.get(data)
        return self.value
    
    def refresh(self):
        self.value = None
        return self.eval(forced=True)

    def __add__(self,other):
        return Expr(self,other,operator.add)

    def __radd__(self,other):
        return Expr(other,self,operator.add)

    def __sub__(self,other):
        return Expr(self,other,operator.sub)

    def __rsub__(self,other):
        return Expr(other,self,operator.sub)

    def __mul__(self,other):
        return Expr(self,other,operator.mul)

    def __rmul__(self,other):
        return Expr(other,self,operator.mul)

    def __truediv__(self,other):
        return Expr(self,other,operator.truediv)

    def __rtruediv__(self,other):
        return Expr(other,self,operator.truediv)

    def __floordiv__(self, other):
        return Expr(self,other,operator.floordiv)

    def __rfloordiv__(self, other):
        return Expr(other,self,operator.floordiv)

    def __mod__(self, other):
        return Expr(self,other,operator.mod)
    
    def __rmod__(self, other):
        return Expr(other,self,operator.mod)

    def __neg__(self):
        return Expr(self,None,operator.neg)
    
    def __abs__(self):
        return Expr(self,None,operator.abs)
    
    def __lt__(self,other):
        return Expr(self,other,operator.lt)

    def __le__(self,other):
        return Expr(self,other,operator.le)

    def __ne__(self,other):
        return Expr(self,other,operator.ne)

    def __eq__(self,other):
        return Expr(self,other,operator.eq)

    def __gt__(self,other):
        return Expr(self,other,operator.gt)

    def __ge__(self,other):
        return Expr(self,other,operator.ge)

    def __and__(self,other):
        return Expr(self,other,lambda x,y:x and y)

    def __rand__(self,other):
        return Expr(other,self,lambda x,y:x and y)

    def __or__(self,other):
        return Expr(self,other,lambda x,y:x or y)

    def __ror__(self,other):
        return Expr(other,self,lambda x,y:x or y)

    def __invert__(self):
        return Expr(self,None,lambda x: not x)

    def __pos__(self):
        return self

    def __repr__(self):
        return str(self.eval())

    def __str__(self):
        return str(self.eval())

    def __int__(self):
        return self.eval()

    def __bool__(self): #to ensure evaluation in if,while etc
        return bool(self.eval())

    def __float__(self):
        return float(self.eval())

class Var(Expr):
    def __init__(self,item:str,location:str,key:str,quality:Optional[int]=1):
        self.item = item
        self.location = location
        self.quality = quality
        self.key = key
        self.reqs = [(item,location,quality)]
    
    def get(self,data):
        try:
            return data[self.item][self.location][self.quality][self.key]
        except:
            raise InvalidVarError(self)


class InvalidVarError(Exception):
    def __init__(self,var: Var):
        self.var = var
        self.message = "invalid params in %s,%s,%d,%s"%(var.item,var.location,var.quality,var.key)

    def __str__(self):
        return self.message