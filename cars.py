#sets: A set is an unordered collection with no duplicate elements
#membership testing and eliminating duplicate entries


showroom = {'Acura', 'BMW', 'Honda', 'Toyota'}
print(len(showroom))
print("----------Showroom Length---------------")

showroom.add('Acura')
print(showroom)
print("----------Showroom Add Acura---------------")

showroom.update(['Mercedes', 'Ford'])
print(showroom)
print("----------Showroom Updated Mercedes & Ford---------------")

showroom.discard('Mercedes')
print(showroom)
print("----------Mercedes Deleted Mercedes---------------")

junkyard = {'Acura', 'Honda', 'Cadillac', 'Volkswagon', 'Nissan', 'Kia'}
print(junkyard)
print("----------Junkyard Created---------------")


new_showroom = showroom.intersection(junkyard)
print(new_showroom)
print("--------Junkyard Intersect Showroom-----------------")

updated_showroom = showroom.symmetric_difference(junkyard)
print(updated_showroom)
print("--------difference of both showroom and junkyard-----------------")


final_showroom = updated_showroom.union(new_showroom)
print(final_showroom)
print("--------combined inventory with union without dupes-----------------")

final_showroom.discard('Kia')
print(final_showroom)
print("--------deleted inventory not needed-----------------")
