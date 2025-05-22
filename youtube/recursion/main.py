# recursion

# calling fn within itself

def fn():
    print("recursion")
    fn()
    
fn()

# RecursionError: maximum recursion depth exceeded
# quiz : max recursion limit 1000
# we can set max limit 