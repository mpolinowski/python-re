import re

# extract emails from text

text = "Spicy jalapeno_bacon@ipsum.com dolor amet turducken biltong frankfurter shankle porchetta. Tail buffalo anim, capicola eiusmod cupim beef ribs tenderloin shank@beef.br biltong. Laboris meatloaf swine, esse cillum est sausage t-bone dolor adipisicing ex-corned@beef.co.uk aliqua porchetta. Boudin fatback chuck meatball laborum meatloaf ground round, filet mignon.prosciutto@shankle.nz pig."

# emails that don't use special characters
# [a-z] = match 1 letter between a-z
# [a-z]+ = match n letter between a-z
email_pattern = re.compile("[a-z]+@[a-z]+.[a-z]+")
email_matches = email_pattern.findall(text)
print(email_matches)
# => ['bacon@ipsum.com', 'shank@beef.br', 'corned@beef.co', 'prosciutto@shankle.nz']

# [^ ] = match everything but white space
# \. = match a "dot" (escaping the . meta character)
# {2,} = TLD has 2 or more characters
email2_pattern = re.compile("[^ ]+@[^ ]+\.[a-z]{2,}")
email2_matches = email2_pattern.findall(text)
# => ['jalapeno_bacon@ipsum.com ', 'shank@beef.br ', 'ex-corned@beef.co.uk ', 'mignon.prosciutto@shankle.nz ']
print(email2_matches)

# (?:com|co.uk) = Match only co.uk and com addresses
email3_pattern = re.compile("[^ ]+@[^ ]+\.(?:com|co.uk)")
email3_matches = email3_pattern.findall(text)
# => ['jalapeno_bacon@ipsum.com', 'ex-corned@beef.co.uk']
print(email3_matches) 
