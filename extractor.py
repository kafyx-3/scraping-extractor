import requests
from bs4 import BeautifulSoup


def extract_data(url, tag="div", class_name=None, show_content=True, save_to_file=False, filename="hasil_ekstraksi.txt"):
    """
    Alat ekstraksi data dari website
    
    Parameters:
    - url: URL website yang mau di-scrape
    - tag: HTML tag yang dicari (default: "div")
    - class_name: Nama class dari tag (default: None untuk semua)
    - show_content: Tampilkan hasil di console (default: True)
    - save_to_file: Simpan hasil ke file (default: False)
    - filename: Nama file output (default: "hasil_ekstraksi.txt")
    """
    
    try:
        # Request ke website
        print(f"Mengakses: {url}")
        response = requests.get(url, timeout=10)
        response.raise_for_status()
        
        # Parse HTML
        soup = BeautifulSoup(response.text, 'html.parser')
        
        # Cari data sesuai parameter
        if class_name:
            results = soup.find_all(tag, class_=class_name)
            print(f"\nMencari <{tag} class='{class_name}'>")
        else:
            results = soup.find_all(tag)
            print(f"\nMencari semua <{tag}>")
        
        print(f"Ditemukan: {len(results)} data\n")
        print("=" * 80)
        
        # Output hasil
        output_lines = []
        
        for i, data in enumerate(results, 1):
            line = f"\n[{i}]\n{data}\n{'-' * 80}"
            output_lines.append(line)
            
            if show_content:
                print(line)
        
        # Simpan ke file jika diminta
        if save_to_file:
            with open(filename, 'w', encoding='utf-8') as f:
                f.write(f"URL: {url}\n")
                f.write(f"Tag: <{tag}> Class: {class_name if class_name else 'semua'}\n")
                f.write(f"Total: {len(results)} data\n")
                f.write("=" * 80 + "\n")
                f.writelines(output_lines)
            print(f"\n✓ Hasil disimpan ke: {filename}")
        
        return results
        
    except requests.exceptions.RequestException as e:
        print(f"✗ Error saat mengakses website: {e}")
        return None
    except Exception as e:
        print(f"✗ Error: {e}")
        return None


# ======================== MENU INTERAKTIF ========================

if __name__ == "__main__":
    print("=" * 80)
    print("ALAT EKSTRAKSI DATA WEBSITE".center(80))
    print("=" * 80)
    
    # Input URL
    url = input("\nMasukkan URL website: ").strip()
    if not url:
        print("✗ URL tidak boleh kosong!")
        exit()
    
    # Input tag HTML
    print("\nContoh tag: div, article, section, span, p, h1, etc.")
    tag = input("Masukkan tag HTML (default: div): ").strip()
    if not tag:
        tag = "div"
    
    # Input class name
    print("\nContoh class: quote, post, product, card, item, etc.")
    print("(Kosongkan jika mau ambil semua tag tersebut)")
    class_name = input(f"Masukkan nama class dari <{tag}>: ").strip()
    if not class_name:
        class_name = None
    
    # Opsi simpan file
    save = input("\nSimpan hasil ke file? (y/n, default: n): ").strip().lower()
    save_to_file = save == 'y' or save == 'yes'
    
    filename = "hasil_ekstraksi.txt"
    if save_to_file:
        custom_filename = input("Nama file (default: hasil_ekstraksi.txt): ").strip()
        if custom_filename:
            if not custom_filename.endswith('.txt'):
                custom_filename += '.txt'
            filename = custom_filename
    
    # Mulai ekstraksi
    print("\n" + "=" * 80)
    results = extract_data(
        url=url,
        tag=tag,
        class_name=class_name,
        show_content=True,
        save_to_file=save_to_file,
        filename=filename
    )
    
    if results:
        print("\n" + "=" * 80)
        print(f"✓ Selesai! Total data: {len(results)}")
        print("=" * 80)
