import xml.etree.ElementTree as ET
import matplotlib.pyplot as plt
import pandas as pd

# Parse the XML file
xml_file = 'API_SP.POP.TOTL_DS2_en_xml_v2_38418.xml'
tree = ET.parse(xml_file)
root = tree.getroot()

# Extract population data for a specific country (e.g., Aruba)
data = []
for record in root.findall('.//data/record'):
    country = record.find("./field[@name='Country or Area']").text
    year = record.find("./field[@name='Year']").text
    value = record.find("./field[@name='Value']").text
    item = record.find("./field[@name='Item']").text

    if country == 'Aruba' and item == 'Population, total':
        data.append({'Year': int(year), 'Population': int(value)})

# Convert to DataFrame
df = pd.DataFrame(data)

# Plot 1: Bar chart (Population over the years for India)
plt.figure(figsize=(14, 6))
plt.bar(df['Year'], df['Population'], color='skyblue')
plt.title('Total Population of Aruba Over the Years')
plt.xlabel('Year')
plt.ylabel('Population')
plt.grid(True, linestyle='--', alpha=0.5)
plt.xticks(rotation=45)
plt.tight_layout()
plt.show()

# Plot 2: Histogram (Distribution of population values)
plt.figure(figsize=(10, 5))
plt.hist(df['Population'], bins=15, color='orange', edgecolor='black')
plt.title('Distribution of Aruba\'s Population (1960–2024)')
plt.xlabel('Population')
plt.ylabel('Frequency')
plt.grid(True, linestyle='--', alpha=0.5)
plt.tight_layout()
plt.show()
