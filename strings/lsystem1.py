def ApplyLSystem(string, rule1, rule2, n):
    if (n <= 0):
        return string
    else:
        for i in range(n):
            string = string.replace(rule1, rule2)
        return string

axiom = "A"
rule1 = "A"
rule2 = "ABBA"
# Rule: A -> ABBA because I'm a dancing queen
newstring = ApplyLSystem(axiom, rule1, rule2, 2)
print(newstring)