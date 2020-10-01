from kcu import kjson
import unidecode

# with open('/Users/kristofk/github/gender-detection/genders/female.js', 'r') as f:
#     female = f.read().strip().strip('}').strip()
#     female_lines = female.split('\n')

# with open('/Users/kristofk/github/gender-detection/genders/male.js', 'r') as f:
#     male = f.read().strip().strip('}').strip()
#     male_lines = male.split('\n')

for path in ['/Users/kristofk/github/gender-detection/genders/female.js', '/Users/kristofk/github/gender-detection/genders/male.js']:
    with open(path, 'r') as f:
        names = [l.lstrip('"').split('"')[0].strip() for l in f.read().split('\n') if l.startswith('"')]

    s = ''
    
    for name in names:
        s += '\n    "' + name + '": { en: 1 },'

        decoded_name = unidecode.unidecode(name)

        if name != decoded_name and decoded_name not in names:
            # print(name, decoded_name)
            s += '\n"' + decoded_name + '": { en: 1 },'
    
    with open(path, 'w') as f:
        f.write('module.exports = {' + s.rstrip(',') + '\n}')

        






# for name, gender in kjson.load('/Users/kristofk/github/npmtest/names3.json').items():
#     proposed_line = '"'+name+'": { en: 1 },'

#     if proposed_line not in female_lines and (gender == 'f' or gender == 'u'):
#         female += '\n' + proposed_line

#     if proposed_line not in male_lines and (gender == 'm' or gender == 'u'):
#         male += '\n' + proposed_line

# with open('/Users/kristofk/github/gender-detection/genders/female.js', 'w') as f:
#     f.write(female.rstrip(',') + '\n}\n')

# with open('/Users/kristofk/github/gender-detection/genders/male.js', 'w') as f:
#     f.write(male.rstrip(',') + '\n}\n')


