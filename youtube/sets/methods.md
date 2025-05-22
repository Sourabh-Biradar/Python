# set methods 

1) `s1.union(s2)` : s1 = s1 + s2 ; no change to original s1

2) `s1.update(s2)` :  s1 updates ; new s1 = s1 + s2

3) `s1.intersection(s2)` : s1 = common item from s1 & s2

4) `s1.intersection_update(s2)` : s1 updates ; new s1 = common item from s1 & s2

5) `symmetric_difference()` : s6 = (s6 + s5) - common items

6) `symmetric_difference_update()` : new s6 = (s6 + s5) - common items

7) `isdisjoint()` : if common items present , returns FALSE

8) `issuperset()` & `issubset()` : if all items of s1 are present in s2 , thn s1 is superset
True if s2 is sub set of s1

9) `add()` : adds item to set

10) `remove()` : removes/deletes specified item ; if item is not present = KeyError

11) `discard()` : removes item if present , no KeyError 

12) `pop()` : pops last item , to see wt item was popped assign var to pop()

13) `del` : not a method but a KEYWORD ; deletes whole set

14) `clear()` : deletes all ITEMS from set ; prints `set()`