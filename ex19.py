def cheese_and_crackers(cheese_count, boxes_of_crackers):
  print "You have %d cheeses!" % cheese_count
  print "You have %d boxes of crackers" % boxes_of_crackers
  print "Man that's enough for a party!" 
  print "Get a blanket.\n"


print "We can just give the funtion numbers directly:"
cheese_and_crackers(15, 30)

print "OR, we may use variables:"
amount_of_cheese = 15
amount_of_crackers = 30
cheese_and_crackers(amount_of_cheese, amount_of_crackers)

print "We can even do math inside too!"
cheese_and_crackers(7 + 8, 15 + 15)

print "Lastly, we can combine the two:"
cheese_and_crackers(amount_of_cheese + 8, amount_of_crackers + 10)


