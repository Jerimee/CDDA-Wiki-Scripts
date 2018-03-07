import json
from version import version
import pywikibot

#data is uploaded automatically, used for the Template:Speciestoname

with open('data/json/species.json') as data_file:
    data = json.load(data_file)

header ='''<includeonly>{{#switch:{{lc:{{{1}}}}}
  |none
  |species_none = unknown species\n'''

footer = '''  |#default={{{1|none}}}
}}</includeonly><noinclude>
Automatically generated by [https://github.com/Soyweiser/CDDA-Wiki-Scripts The speciestoname.py script]. Any edits made to this can and will be overwritten. Please contact [[User:Soyweiser|Soyweiser]] if you want make changes to this page. Especially as any changes made here probably also means there have been changes in other pages. And there are tools to update those a little bit quicker.\n\n
Template for converting species identifiers to their associated names.\n'''
footer += version+'''[[Category:Templates]]
</noinclude>'''

output = [ "" ]
output.append(header)
for it in range(0, len(data)):
    output.append("  |")
    output.append(data[it]['id'].lower())
    output.append(" = ")
    output.append(data[it]['name'])
    output.append("\n")
output.append(footer)

text = "".join(output)
text.replace("\n", "\\n")
site = pywikibot.Site('en', 'cddawiki')
page = pywikibot.Page(site, 'Template:Speciestoname')
page.text = Foodtext
page.save('Updated text automatically via the https://github.com/Soyweiser/CDDA-Wiki-Scripts speciestoname.py script')
exit()