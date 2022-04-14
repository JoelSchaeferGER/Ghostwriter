import random
counter = 0 # count how many iterations are necessary
# original = 'Hello, World!'
original = 'Hello, World!'

txt = original
txt = [c for c in txt]
random.shuffle(txt)
print(txt)

generated = ''

# Do until original and generated are the same
while generated != original:
    counter += 1
    random.shuffle(txt)
    generated = ''.join(txt)
    
print(f'generated {generated} after {counter} iterations')

