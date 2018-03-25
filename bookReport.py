import re
import wikipedia as wiki

math = wiki.summary('math')
mathematicians = re.findall(r'[A-Z]\w+\s[A-Z]\w+',math)

errors = list()
for i in range(0,len(mathematicians)):
    try:
        guru = wiki.summary(mathematicians[i])
        birthday = re.search(r'\w+\s\w+\s\d\d\d\d',guru).group()
        print()
        print(mathematicians[i] + ' born on ' + birthday)
        print()
    except:
        errors.append(mathematicians[i])

print(errors)
