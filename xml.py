import xml.etree.ElementTree as ET
tree = ET.parse('country_data.xml')
root = tree.getroot()

for at in root.iter():
	name = at.get('Name')
	print(at.tag)
