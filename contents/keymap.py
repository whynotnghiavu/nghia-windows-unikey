import os
import subprocess
import sys
import ctypes


def is_admin():
    try:
        return ctypes.windll.shell32.IsUserAnAdmin()
    except:
        return False


if is_admin():

    Downloads = os.path.expanduser(r"~\Downloads")
    print(f"🚀 {Downloads}")

    # Đường dẫn đến thư mục VietNam
    VietNam = os.path.join(Downloads, r"Nghia\Programs\VietNam")
    print(f"🚀 {VietNam}")

    keymap_txt_link = os.path.join(VietNam, "keymap.txt")
    print(f"🚀 {keymap_txt_link}")

    # Đường dẫn đến file keymap.txt
    keymap_txt = os.path.join(os.getcwd(), "keymap.txt")
    print(f"🚀 {keymap_txt}")

    # Xóa liên kết
    if os.path.exists(keymap_txt_link):
        os.remove(keymap_txt_link)
        print(f"Đã xóa file: {keymap_txt_link}")
    else:
        print(f"File không tồn tại: {keymap_txt_link}")

    # Tạo liên kết
    try:
        # subprocess.run(['mklink', keymap_txt_link, keymap_txt], shell=True, check=True)
        subprocess.run(['mklink', keymap_txt_link, keymap_txt], shell=True, check=True)
        print(f"Tạo liên kết thành công: {keymap_txt_link}")
    except subprocess.CalledProcessError as e:
        print(f"Lỗi khi tạo liên kết: {e}")
    except FileExistsError:
        print("Liên kết đã tồn tại")
    except OSError as e:
        print(f"Lỗi hệ thống khi tạo liên kết: {e}")


else:
    ctypes.windll.shell32.ShellExecuteW(
        None, "runas", sys.executable, " ".join(sys.argv), None, 1)
