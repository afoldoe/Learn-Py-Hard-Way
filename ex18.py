def print_two(*args):
  arg1, arg2 = args
  print "arg1: %r, arg2: %r" % (arg1, arg2)

def print_two_again(args1, args2):
  print "arg1: %r, arg2: %r" % (args1, args2)

def print_uno(args1):
  print "you are the ONE: %r" % (args1)

def nada():
  print "Winter is coming."

print_two("First", "Second")
print_two_again("FirstAgain", "SecondAgain")
print_uno("Me?")
nada()

