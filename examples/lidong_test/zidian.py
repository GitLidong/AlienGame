print "Hello world"
favorite_languages = {
    'jen':['python','ruby'],
    'sarash':['c'],
    'edward':['ruby','go'],
    }
for name,languages in favorite_languages.items():
    print("\n"+name.title()+"'s favorite languages are:")
    for language in languages:
        print("\t"+language.title())
