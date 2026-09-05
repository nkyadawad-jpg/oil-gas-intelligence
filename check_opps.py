import re

with open('index.html', encoding='utf-8') as f:
    text = f.read()

# Check client and EPC names
clients = re.findall(r'client:\s*"([^"]+)"', text)
epcs = re.findall(r'epc:\s*"([^"]+)"', text)
projects = re.findall(r'project:\s*"([^"]+)"', text)
stages = re.findall(r'stageBadge:\s*"([^"]+)"', text)
values = re.findall(r'value:\s*([0-9]+)', text)

print(f"Count of opportunities: {len(clients)}")
for i in range(len(clients)):
    print(f"{i+1}. [{clients[i]}] ({epcs[i]}) {projects[i][:40]}... Stage: {stages[i]} Val: QAR {int(values[i]):,}")
