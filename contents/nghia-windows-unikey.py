import os










Downloads = os.path.expanduser(r"~\Downloads")
print(f"🚀 {Downloads}")


VietNam = os.path.join(Downloads, r"Nghia\Programs\VietNam")
print(f"🚀 {VietNam}")

keymap_txt_link = os.path.join(VietNam, "keymap.txt")
print(f"🚀 {keymap_txt_link}")


nghia_windows_unikey_txt = os.path.join(os.getcwd(), "nghia-windows-unikey.txt")
print(f"🚀 {nghia_windows_unikey_txt}")



try:
    if os.path.exists(keymap_txt_link):
        os.remove(keymap_txt_link)
        print(f"Đã xóa symlink: {keymap_txt_link}")
    os.symlink(os.path.abspath(nghia_windows_unikey_txt), keymap_txt_link)
    print(f"Tạo link: {keymap_txt_link}")
except OSError as e:
    print(f"Lỗi: {e}")
