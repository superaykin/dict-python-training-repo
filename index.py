def applyAntigen(bloodSample, antigen) :
    return bloodSample | antigen


x = '100'
a = '100'

res = applyAntigen(x, a)

print(F"{res}")