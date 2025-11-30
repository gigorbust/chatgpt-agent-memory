import xml.etree.ElementTree as ET
from urllib.parse import urlparse
import sys

def parse_sitemap(xml_file):
    try:
        tree = ET.parse(xml_file)
        root = tree.getroot()
        
        # Namespace handling
        ns = {'ns0': 'http://www.sitemaps.org/schemas/sitemap/0.9'}
        
        urls = []
        for url in root.findall('ns0:url', ns):
            loc = url.find('ns0:loc', ns).text
            urls.append(loc)
            
        return urls
    except Exception as e:
        print(f"Error parsing XML: {e}")
        return []

def build_tree(urls):
    tree = {}
    for url in urls:
        parsed = urlparse(url)
        path = parsed.path.strip('/')
        parts = path.split('/')
        if parts == ['']:
            parts = []
            
        current = tree
        for part in parts:
            if part not in current:
                current[part] = {}
            current = current[part]
    return tree

def print_tree(tree, indent=0):
    output = ""
    keys = sorted(tree.keys())
    for i, key in enumerate(keys):
        is_last = (i == len(keys) - 1)
        prefix = "└── " if is_last else "├── "
        
        # For root level, just print the key if indent is 0, but here we are printing children
        # Actually, let's format it nicely
        output += "  " * indent + prefix + key + "\n"
        output += print_tree(tree[key], indent + 1)
    return output

def print_markdown_tree(tree, level=0):
    output = ""
    keys = sorted(tree.keys())
    for key in keys:
        indent = "    " * level
        output += f"{indent}- {key}\n"
        output += print_markdown_tree(tree[key], level + 1)
    return output

if __name__ == "__main__":
    sitemap_path = "/Users/georgegayl/Library/CloudStorage/Dropbox (9-1-25 10:19 PM)/Silent Storm RF (1)/Meztal/Google Antigravity/chatgpt-agent-memory/meztal_sitemap_final.xml"
    urls = parse_sitemap(sitemap_path)
    
    if not urls:
        print("No URLs found.")
        sys.exit(1)
        
    url_tree = build_tree(urls)
    
    print("# MezTal.com Site Hierarchy\n")
    print(f"**Total Pages:** {len(urls)}\n")
    
    # Root
    print("- / (Home)")
    print(print_markdown_tree(url_tree))
