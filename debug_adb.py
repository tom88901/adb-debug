import shlex

# ==============================================================================
# PHẦN CẤU HÌNH - Tọa độ và thông tin của bạn đã được cập nhật sẵn
# ==============================================================================
class Config:
    # --- Thông tin cho bước tải và cài đặt ---
    APK_DOWNLOAD_URL = "https://raw.githubusercontent.com/tom88901/apk_debug/main/Shelter.apk"
    APK_PATH_IN_VM = "/sdcard/Download/Shelter.apk"

    # --- Tọa độ các nút bấm (X, Y) ---
    COORDS_ICON_SHELTER_HOME = (274, 294)      # Bước 1: Icon app Shelter ngoài màn hình chính
    COORDS_NEXT_BUTTON = (578, 1222)          # Bước 2, 3, 4, 5, 7: Nút "Next"
    COORDS_ACCEPT_CONTINUE = (528, 1204)      # Bước 6: Nút "Accept and continue"
    COORDS_ALLOW = (368, 706)                 # Bước 8: Nút "ALLOW"
    COORDS_3_DOTS_MENU = (674, 98)            # Bước 10: Dấu 3 chấm
    COORDS_SHOW_ALL_APPS = (646, 488)         # Bước 11: Nút "Show All Apps"
    COORDS_CONTINUE = (566, 854)              # Bước 12: Nút "CONTINUE"
    COORDS_SEARCH_ICON = (472, 96)            # Bước 13, 14: Kính lúp / Ô tìm kiếm
    COORDS_GOOGLE_PLAY_STORE_ITEM = (222, 228) # Bước 16: Dòng "Google Play Store" trong danh sách
    COORDS_CLONE_TO_SHELTER = (262, 732)      # Bước 16, 17: Nút "Clone to Shelter"
    COORDS_GOOGLE_PLAY_SERVICES_ITEM = (262, 386) # Bước 17: Dòng "Google Play services"
    COORDS_PLAY_STORE_ICON_HOME = (434, 278)  # Bước 18: Icon Play Store (có cặp sách)
    COORDS_SIGN_IN = (354, 950)               # Bước 19: Nút "Sign in"
    COORDS_CREATE_ACCOUNT = (134, 896)        # Bước 20: Nút "Create account"
    COORDS_FIRST_NAME_INPUT = (152, 486)      # Bước 22: Ô nhập "First name"
    COORDS_SURNAME_INPUT = (168, 640)         # Bước 22: Ô nhập "Surname"
    COORDS_NEXT_AFTER_NAME = (586, 708)       # Bước 22: Nút "Next" sau khi nhập tên
    COORDS_DAY_INPUT = (102, 488)             # Bước 24: Ô nhập "Day"
    COORDS_MONTH_DROPDOWN = (362, 488)        # Bước 25: Ô chọn "Month"
    COORDS_MONTH_FEBRUARY = (358, 708)        # Bước 25: Chọn "February"
    COORDS_YEAR_INPUT = (544, 488)            # Bước 26: Ô nhập "Year"
    COORDS_GENDER_DROPDOWN = (160, 628)       # Bước 27: Ô chọn "Gender"
    COORDS_GENDER_MALE_OR_FEMALE = (202, 310) # Bước 27: Tùy chọn Male/Female
    COORDS_NEXT_AFTER_DOB = (592, 1210)       # Bước 28: Nút "Next" sau khi nhập ngày sinh
    COORDS_CREATE_OWN_GMAIL = (162, 690)      # Bước 29: Dòng "Create your own Gmail address"
    COORDS_CUSTOM_GMAIL_INPUT = (126, 840)    # Bước 29: Ô nhập gmail tùy chỉnh
    COORDS_NEXT_AFTER_GMAIL = (594, 708)      # Bước 29: Nút "Next" sau khi nhập gmail
    COORDS_PASSWORD_INPUT = (106, 540)        # Bước 30: Ô nhập password
    COORDS_NEXT_AFTER_PASSWORD = (592, 710)   # Bước 30: Nút "Next" sau khi nhập pass
    COORDS_SKIP_OR_NEXT_FINAL = (590, 1198)   # Bước 31: Nút "Next" hoặc "Skip" ở màn hình cuối

    # --- Thông tin người dùng ---
    INPUT_FIRST_NAME = "Van A"
    INPUT_SURNAME = "Nguyen"
    INPUT_DAY_OF_BIRTH = "15"
    INPUT_YEAR_OF_BIRTH = "1995"
    INPUT_GMAIL_USERNAME = "nguyenvan.a95.test"
    INPUT_PASSWORD = "Password_cua_ban_123"

# ==============================================================================
# PHẦN LOGIC - Các hàm để tạo ra các câu lệnh con
# ==============================================================================

def cmd_tap(x, y):
    return f"input tap {x} {y}"

def cmd_type_text(text):
    safe_text = shlex.quote(text)
    return f"input text {safe_text}"

def cmd_wait(seconds):
    return f"sleep {seconds}"

def cmd_keyevent(keycode):
    return f"input keyevent {keycode}"

def cmd_install_apk(path):
    return f"pm install -g {path}" # Thêm cờ -g để tự động cấp quyền

def cmd_start_chrome_no_setup(url):
    return f'am start -n com.android.chrome/com.google.android.apps.chrome.Main -d "{url}" --ez com.android.chrome.EXTRA_DISABLE_FRE true'

def cmd_tap_on_text(text_to_find):
    get_coords_cmd = f"uiautomator dump >/dev/null && grep -o 'text=\"{text_to_find}\"' /sdcard/window_dump.xml | sed -n 's/.*bounds=\"\\[\\([0-9]*\\),\\([0-9]*\\)\\]\\[\\([0-9]*\\),\\([0-9]*\\)\\].*/\\1 \\2 \\3 \\4/p' | head -n 1"
    full_command = f"coords=$({get_coords_cmd}); if [ ! -z \"$coords\" ]; then set -- $coords; x=$((($1+$3)/2)); y=$((($2+$4)/2)); input tap $x $y; fi"
    return full_command

def cmd_tap_on_resource_id(id_to_find):
    # !!! HÀM MỚI: Tìm và nhấn vào một phần tử dựa trên resource-id duy nhất của nó.
    get_coords_cmd = f"uiautomator dump >/dev/null && grep -o 'resource-id=\"{id_to_find}\"' /sdcard/window_dump.xml | sed -n 's/.*bounds=\"\\[\\([0-9]*\\),\\([0-9]*\\)\\]\\[\\([0-9]*\\),\\([0-9]*\\)\\].*/\\1 \\2 \\3 \\4/p' | head -n 1"
    full_command = f"coords=$({get_coords_cmd}); if [ ! -z \"$coords\" ]; then set -- $coords; x=$((($1+$3)/2)); y=$((($2+$4)/2)); input tap $x $y; fi"
    return full_command

def cmd_wait_for_text(text_to_wait_for, timeout=30):
    loop_command = f"count=0; while ! (uiautomator dump >/dev/null && grep -q '{text_to_wait_for}' /sdcard/window_dump.xml); do sleep 1; count=$((count+1)); if [ $count -ge {timeout} ]; then echo 'Timeout waiting for {text_to_wait_for}'; break; fi; done"
    return loop_command

# ==============================================================================
# PHẦN CHÍNH - Nơi kịch bản được tạo ra
# ==============================================================================

def generate_script():
    commands = []
    cfg = Config()

    # --- BƯỚC 0: TẢI VÀ CÀI ĐẶT SHELTER ---
    
    # 1. DỌN DẸP TRIỆT ĐỂ: Reset Chrome về trạng thái gốc để đảm bảo môi trường luôn sạch.
    commands.append("pm clear com.android.chrome")
    commands.append(cmd_wait(3)) # Chờ 3 giây để hệ thống hoàn tất việc dọn dẹp

    # 2. Mở Chrome. Bây giờ nó sẽ luôn khởi động như lần đầu tiên.
    commands.append(cmd_start_chrome_no_setup(cfg.APK_DOWNLOAD_URL))
    commands.append(cmd_wait(5)) 

    # 3. HỦY DIỆT: Xử lý màn hình cài đặt bằng cách thử nhấn vào TẤT CẢ các ID đã biết.
    
    # Bỏ chọn ô gửi dữ liệu (nếu nó xuất hiện)
    commands.append(cmd_tap_on_resource_id("com.android.chrome:id/send_report_checkbox"))
    commands.append(cmd_wait(1))

    # Nút "Accept" có thể có 3 ID khác nhau. Ta sẽ thử nhấn cả ba.
    # Phương pháp này đảm bảo thành công dù Chrome hiển thị phiên bản giao diện nào.
    commands.append(cmd_tap_on_resource_id("com.android.chrome:id/terms_accept"))   # ID phiên bản 1
    commands.append(cmd_tap_on_resource_id("com.android.chrome:id/next_button"))     # ID phiên bản 2
    commands.append(cmd_tap_on_resource_id("com.android.chrome:id/positive_button")) # ID phiên bản 3 (mới nhất)
    commands.append(cmd_wait(2))

    # Tiếp tục xử lý các màn hình sau (nếu có)
    commands.append(cmd_tap_on_text("No, thanks"))
    commands.append(cmd_wait(2))
    commands.append(cmd_tap_on_text("Done"))
    commands.append(cmd_wait(2))

    # 4. Sau khi đã dọn dẹp, tiến hành tải file
    commands.append(cmd_wait_for_text("Download", timeout=20))
    commands.append(cmd_tap_on_text("Download"))
    commands.append(cmd_wait(20))
    commands.append(cmd_install_apk(cfg.APK_PATH_IN_VM))
    commands.append(cmd_wait(15))
    commands.append(cmd_keyevent(3))
    commands.append(cmd_wait(3))

    
    # Bước 1-9: Cài đặt Shelter
    commands.append(cmd_tap(cfg.COORDS_ICON_SHELTER_HOME[0], cfg.COORDS_ICON_SHELTER_HOME[1]))
    commands.append(cmd_wait_for_text("CONTINUE", timeout=10))
    commands.append(cmd_tap_on_text("CONTINUE"))
    commands.append(cmd_wait_for_text("Next", timeout=5))
    commands.append(cmd_tap_on_text("Next"))
    commands.append(cmd_wait_for_text("Accept & continue", timeout=18))
    commands.append(cmd_tap_on_text("Accept & continue"))
    commands.append(cmd_wait_for_text("Next", timeout=20))
    commands.append(cmd_tap_on_text("Next"))
    commands.append(cmd_wait(10)) 
    commands.append(cmd_wait_for_text("ALLOW", timeout=10))
    commands.append(cmd_tap_on_text("ALLOW"))
    commands.append(cmd_wait_for_text("Main", timeout=10))

    # Bước 10-17: Clone ứng dụng
    commands.append(cmd_tap(cfg.COORDS_3_DOTS_MENU[0], cfg.COORDS_3_DOTS_MENU[1]))
    commands.append(cmd_wait(1))
    commands.append(cmd_tap_on_text("Show All Apps"))
    commands.append(cmd_wait_for_text("System Apps", timeout=10))
    commands.append(cmd_tap(cfg.COORDS_SEARCH_ICON[0], cfg.COORDS_SEARCH_ICON[1]))
    commands.append(cmd_wait(1))
    commands.append(cmd_type_text('google play'))
    commands.append(cmd_wait(2))
    commands.append(cmd_tap_on_text("Google Play Store"))
    commands.append(cmd_wait(1))
    commands.append(cmd_tap_on_text("Clone to Shelter"))
    commands.append(cmd_wait_for_text("Google Play services", timeout=15))
    commands.append(cmd_tap_on_text("Google Play services"))
    commands.append(cmd_wait(1))
    commands.append(cmd_tap_on_text("Clone to Shelter"))
    commands.append(cmd_wait(10))

    # Bước 18-31: Tạo tài khoản Google
    commands.append(cmd_keyevent(3))
    commands.append(cmd_wait(3))
    commands.append(cmd_tap(cfg.COORDS_PLAY_STORE_ICON_HOME[0], cfg.COORDS_PLAY_STORE_ICON_HOME[1]))
    commands.append(cmd_wait_for_text("Sign in", timeout=15))
    commands.append(cmd_tap_on_text("Sign in"))
    commands.append(cmd_wait_for_text("Create account", timeout=10))
    commands.append(cmd_tap_on_text("Create account"))
    commands.append(cmd_wait_for_text("For my personal use", timeout=5))
    commands.append(cmd_tap_on_text("For my personal use"))
    commands.append(cmd_wait_for_text("First name", timeout=5))
    commands.append(cmd_type_text(cfg.INPUT_FIRST_NAME))
    commands.append(cmd_keyevent(61)) # Phím TAB để chuyển sang ô Surname
    commands.append(cmd_type_text(cfg.INPUT_SURNAME))
    commands.append(cmd_tap_on_text("Next"))
    commands.append(cmd_wait_for_text("Day", timeout=5))
    commands.append(cmd_type_text(cfg.INPUT_DAY_OF_BIRTH))
    commands.append(cmd_tap(cfg.COORDS_MONTH_DROPDOWN[0], cfg.COORDS_MONTH_DROPDOWN[1]))
    commands.append(cmd_wait(1))
    commands.append(cmd_tap(cfg.COORDS_MONTH_FEBRUARY[0], cfg.COORDS_MONTH_FEBRUARY[1]))
    commands.append(cmd_wait(1))
    commands.append(cmd_type_text(cfg.INPUT_YEAR_OF_BIRTH))
    commands.append(cmd_tap(cfg.COORDS_GENDER_DROPDOWN[0], cfg.COORDS_GENDER_DROPDOWN[1]))
    commands.append(cmd_wait(1))
    commands.append(cmd_tap(cfg.COORDS_GENDER_MALE_OR_FEMALE[0], cfg.COORDS_GENDER_MALE_OR_FEMALE[1]))
    commands.append(cmd_wait(1))
    commands.append(cmd_tap_on_text("Next"))
    commands.append(cmd_wait_for_text("Create your own Gmail address", timeout=5))
    commands.append(cmd_tap_on_text("Create your own Gmail address"))
    commands.append(cmd_wait(2))
    commands.append(cmd_type_text(cfg.INPUT_GMAIL_USERNAME))
    commands.append(cmd_tap_on_text("Next"))
    commands.append(cmd_wait_for_text("Password", timeout=5))
    commands.append(cmd_type_text(cfg.INPUT_PASSWORD))
    commands.append(cmd_tap_on_text("Next"))
    commands.append(cmd_wait_for_text("Yes, I’m in", timeout=10))
    commands.append(cmd_tap_on_text("Yes, I’m in"))
    commands.append(cmd_wait_for_text("Next", timeout=5))
    commands.append(cmd_tap_on_text("Next"))
    commands.append(cmd_wait_for_text("I agree", timeout=10))
    commands.append(cmd_tap_on_text("I agree"))

    full_script = " && ".join(commands)
    return full_script

if __name__ == "__main__":
    final_script = generate_script()
    print("========= SAO CHÉP TOÀN BỘ LỆNH BÊN DƯỚI =========")
    print(final_script)
    print("===================================================")
