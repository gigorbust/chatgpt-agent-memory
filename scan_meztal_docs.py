import os
import mimetypes

def is_text_file(filepath):
    guess, _ = mimetypes.guess_type(filepath)
    if guess and guess.startswith('text'):
        return True
    # Fallback for common extensions
    if filepath.endswith(('.md', '.txt', '.csv', '.json', '.py', '.xml', '.html', '.js', '.css')):
        return True
    return False

def scan_docs(root_dir, output_file):
    print(f"Scanning {root_dir}...")
    
    with open(output_file, 'w', encoding='utf-8') as out:
        out.write("# Meztal Documents Index\n\n")
        
        count = 0
        for root, dirs, files in os.walk(root_dir):
            # Skip specific directories
            if 'deliverables' in dirs:
                dirs.remove('deliverables')
            if 'logs' in dirs:
                dirs.remove('logs')
            if '.git' in dirs:
                dirs.remove('.git')
            if 'node_modules' in dirs:
                dirs.remove('node_modules')
                
            for file in files:
                if 'meztal' in file.lower():
                    filepath = os.path.join(root, file)
                    relpath = os.path.relpath(filepath, root_dir)
                    
                    # Skip the output file itself and the script
                    if file == os.path.basename(output_file) or file == os.path.basename(__file__):
                        continue

                    count += 1
                    out.write(f"## {count}. {relpath}\n")
                    
                    if is_text_file(filepath):
                        try:
                            with open(filepath, 'r', encoding='utf-8', errors='ignore') as f:
                                head = [next(f) for _ in range(5)]
                                content_preview = "".join(head).strip()
                                if content_preview:
                                    out.write(f"```text\n{content_preview}\n```\n")
                                else:
                                    out.write("*[Empty file]*\n")
                        except Exception as e:
                            out.write(f"*[Error reading file: {e}]*\n")
                    else:
                        out.write("*[Binary or non-text file]*\n")
                    
                    out.write("\n")
    
    print(f"Scan complete. Found {count} files. Results saved to {output_file}")

if __name__ == "__main__":
    root_directory = "/Users/georgegayl/Library/CloudStorage/Dropbox (9-1-25 10:19 PM)/Silent Storm RF (1)/Meztal/Google Antigravity/chatgpt-agent-memory"
    output_filename = "meztal_docs_index.md"
    scan_docs(root_directory, output_filename)
