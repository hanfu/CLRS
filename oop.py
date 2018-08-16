#static variable
class theclass:
	#variables defined at class level are static
	staticv = 10

a = theclass()
a.staticv #10
a.staticv = 9#only change instance a
theclass.staticv = 9#change at the class level

#instance property, getter, setter
class java:
	def __init__(self, n):
		self._value = n

	#traditiona getter and setter methods
	def getter(self):
		return self._value

	def setter(self, newn):
		self._value = newn

	#add the property
	value = property(fget=getter, fset=setter, doc="Property: value")

class python:
	def __init__(self,n):
		self._value = n

	#read-only getter
	@property
	def value(self):
		#possible for statements
		return self._value

	#the property setter
	@value.setter
	def value(self, n):
		#possible for validation
		self._value = n

#static, class, instance method
class theclass:
	def insm(self):
		pass
		#modify instance, called only at instance level

	@classmethod
	def clsm(cls):
		pass
		#modify cls, callable to both instance and cls level
		#useful for class' utility func, 

	@staticmethod
	def staticm():
		pass
		#access only input args, callable at both levels

#function-oriented decorators
def decor_func(innerfunc):
    def wrapper(*a, **kw):
        print("entering")
        innerfunc(*a, **kw)
        print("exited")
    #wrapper.__name__ = innerfunc.__name__
    #if name matters
    return wrapper

def func1(*a, **kw):
    print("Wheee!")

func1_d = decor_func(func1)

@decor_func
def newfunc1(*a, **kw):
	print("whoooa")

print(newfunc1.__str__)
#returns function decor_func.<locals>.wrapper


#class-oriented decorator equavalent to previous
class decor_obj:
    def __init__(self, f):
        self.f = f

    def __call__(self):
        print("Entering", self.f.__name__)
        self.f()
        print("Exited", self.f.__name__)

@decor_obj
def func2():
    print("whaiii")



#even change the function call
class myDecorator:
    def __init__(self, f):
        print("inside myDecorator.__init__()")
        f() # Prove that function definition has completed
    def __call__(self):
        print("inside myDecorator.__call__()")

@myDecorator
def aFunction():
    print("inside aFunction()")
#decorator declared with __init__now:
#as soon as func defined, it prompts
#__init__
#inside func()

#aFunction is a myDecorator object
aFunction()
#print 
#now prints myDecorator.__call__()
#NOT inside func because class attr overwrite

def decorator(func):
	pass

@decorator
def foo(*args, **kwargs):
    pass
#translates to
foo = decorator(foo)

#So if the decorator had arguments,
def decorator_arg(arg):
	return decorator
	#return a decorator func

arg = 'someblah'
@decorator_arg(arg)
def foo(*args, **kwargs):
    pass
#translates to
foo = decorator_arg(arg)(foo)


#talking about super()
#1. pass subclass' args to superclass
class Superclass(object):
    def __init__(self, arg1, arg2, arg3):
        #Initialise some variables
        #Call some methods
        pass

class Subclass(Superclass):
    def __init__(self, subclass_arg1, *args, **kwargs):
        super().__init__(*args, **kwargs)
		#same as Superclass.__init__(*a, **kw)
		#if python2, super(ClassName, self).__init__()
        pass


#2. shortcut for parent class in more subtle inherentence
class A():
    def __init__(self):
        print("A")
        self.a = 'a'

class B(A):
    def __init__(self):
        print("B")
        self.b = 'b'
        #class A not init at all. 
        #no 'first' printed, nor attr a.

class C(B):
    def __init__(self):
        super().__init__()
        print("C")
        #super calls class B
        #prints second and third, and have attr b = 'b'


#override: subclass replace the method/attr
#overload: same method act differently on different input(mostly data type)



#try except testing
arr = [1,2,3]
def tryindex(arr):
	try:
		maximum = 1
		maximum = max(arr[2],  arr[3], 2)
		maximum = 10
	except IndexError:
		pass
        maximum = 100
	else:
    #optional if you only want it execute when no exception
        return maximum
	#conclusion: run till error line
	#conclusion: python will abort entire line 

#__getattr__三连
getattr
setattr
hasattr#only return AttributeError