import shlex
import random
import string
import time
# Thêm thư viện sys để điều hướng luồng xuất
import sys

# ==============================================================================
# PHẦN CẤU HÌNH - Tọa độ và thông tin của bạn đã được cập nhật sẵn
# ==============================================================================
class Config:
    # --- (THÊM MỚI) DANH SÁCH ĐỂ TẠO TÊN NGẪU NHIÊN ---
    HO_VIETNAM = ["Nguyen", "Tran", "Le", "Pham", "Hoang", "Huynh", "Phan", "Vu", "Vo", "Dang", "Bui", "Do", "Ho", "Ngo", "Duong"]
    TEN_VIETNAM = ["Anh", "Binh", "Chau", "Dung", "Giang", "Hien", "Khanh", "Linh", "Minh", "Nam", "Phuong", "Quan", "Son", "Thang", "Trang", "Tuan", "Van", "Xuan", "Yen"]


    # --- Thông tin cho bước tải và cài đặt ---
    APK_DOWNLOAD_URL = "https://raw.githubusercontent.com/tom88901/apk_debug/main/Shelter.apk" # Chú thích: Đường link URL trực tiếp để tải về tệp Shelter.apk.
    APK_PATH_IN_VM = "/sdcard/Download/Shelter.apk" # Chú thích: Đường dẫn lưu tệp APK sau khi tải về trên máy ảo, thường là trong thư mục Download.

    # !!! THAY ĐỔI QUAN TRỌNG: Tọa độ cho các màn hình chào mừng của Chrome
    # BẠN CẦN LẤY VÀ CẬP NHẬT CÁC TỌA ĐỘ NÀY BẰNG CÔNG CỤ "VỊ TRÍ CON TRỎ"
    COORDS_CHROME_ACCEPT = (356, 1181)           # Chú thích: Tọa độ (X, Y) của nút "Accept & continue" (Trường hợp 1).
    COORDS_CHROME_USE_WITHOUT_ACCOUNT = (350, 1064) # Chú thích: Tọa độ (X, Y) của nút "Use without an account" (Trường hợp 2).
    COORDS_CHROME_SYNC_NO = (101, 1200)           # Chú thích: Tọa độ (X, Y) của nút "No, thanks" trên màn hình "Turn on sync?".
    COORDS_CHROME_NOTIF_CONTINUE = (337, 1051)    # Chú thích: Tọa độ (X, Y) của nút "Continue" trên màn hình "Chrome notifications".
    COORDS_CHROME_DOWNLOAD_ANYWAY = (533, 784)   # Chú thích: Tọa độ (X, Y) của nút "Download anyway" khi Chrome hiện cảnh báo.

    # --- Tọa độ cho các bước còn lại của kịch bản ---
    COORDS_ICON_SHELTER_HOME = (274, 294)         # Chú thích: Tọa độ của biểu tượng ứng dụng Shelter trên màn hình chính.
    COORDS_NEXT_BUTTON = (578, 1222)              # Chú thích: Tọa độ chung cho các nút "Next" hoặc "Continue" trong quá trình cài đặt Shelter.
    COORDS_ACCEPT_CONTINUE = (528, 1204)          # Chú thích: Tọa độ của nút "Accept and continue" để đồng ý điều khoản của Shelter.

    # --- TÁCH RIÊNG NÚT NEXT SAU KHI CÀI ĐẶT PROFILE ---
    COORDS_NEXT_AFTER_SETUP = (588, 1202)         # Chú thích: Tọa độ của nút "Next" xuất hiện sau khi Shelter đã thiết lập xong.

    COORDS_ALLOW = (368, 706)                     # Chú thích: Tọa độ của nút "ALLOW" để cấp quyền quản trị thiết bị cho Shelter.
    COORDS_3_DOTS_MENU = (674, 98)                # Chú thích: Tọa độ của menu 3 chấm trong ứng dụng Shelter.
    COORDS_SHOW_ALL_APPS = (646, 488)             # Chú thích: Tọa độ của mục "Show All Apps" trong menu của Shelter.
    COORDS_CONTINUE = (566, 854)                  # Chú thích: Tọa độ của nút "CONTINUE" khi vào danh sách ứng dụng hệ thống.
    COORDS_SEARCH_ICON = (472, 96)                # Chú thích: Tọa độ của biểu tượng kính lúp để tìm kiếm ứng dụng.
    COORDS_GOOGLE_PLAY_STORE_ITEM = (222, 228)    # Chú thích: Tọa độ của ứng dụng "Google Play Store" trong danh sách kết quả tìm kiếm.
    COORDS_CLONE_TO_SHELTER = (262, 732)          # Chú thích: Tọa độ của nút "Clone to Shelter" để nhân bản ứng dụng.
    COORDS_GOOGLE_PLAY_SERVICES_ITEM = (262, 386) # Chú thích: Tọa độ của "Google Play services" trong danh sách ứng dụng.
    COORDS_PLAY_STORE_ICON_HOME = (434, 278)      # Chú thích: Tọa độ của biểu tượng Play Store đã được nhân bản (có hình cặp sách).
    COORDS_SIGN_IN = (354, 950)                   # Chú thích: Tọa độ của nút "Sign in" trong Google Play Store.
    COORDS_CREATE_ACCOUNT = (134, 896)            # Chú thích: Tọa độ của nút "Create account" để bắt đầu tạo tài khoản Google.
    COORDS_FOR_MY_PERSONAL_USE = (158, 604)       # Chú thích: Tọa độ của tùy chọn "For my personal use" (Đã thêm để sửa lỗi).
    COORDS_FIRST_NAME_INPUT = (152, 486)          # Chú thích: Tọa độ của ô nhập "First name" (Tên).
    COORDS_SURNAME_INPUT = (168, 640)             # Chú thích: Tọa độ của ô nhập "Surname" (Họ).
    COORDS_NEXT_AFTER_NAME = (586, 708)           # Chú thích: Tọa độ của nút "Next" sau khi đã nhập tên.
    COORDS_DAY_INPUT = (102, 488)                 # Chú thích: Tọa độ của ô nhập "Day" (Ngày sinh).
    COORDS_MONTH_DROPDOWN = (362, 488)            # Chú thích: Tọa độ của ô chọn "Month" (Tháng sinh).
    COORDS_MONTH_FEBRUARY = (358, 708)            # Chú thích: Tọa độ của lựa chọn "February" (Tháng hai) trong danh sách tháng.
    COORDS_YEAR_INPUT = (544, 488)                # Chú thích: Tọa độ của ô nhập "Year" (Năm sinh).
    COORDS_GENDER_DROPDOWN = (160, 628)           # Chú thích: Tọa độ của ô chọn "Gender" (Giới tính).
    COORDS_GENDER_MALE_OR_FEMALE = (202, 310)     # Chú thích: Tọa độ của một lựa chọn giới tính (ví dụ: Male/Female).
    COORDS_NEXT_AFTER_DOB = (592, 1210)           # Chú thích: Tọa độ của nút "Next" sau khi nhập xong ngày tháng năm sinh.
    COORDS_CREATE_OWN_GMAIL = (162, 690)          # Chú thích: Tọa độ của tùy chọn "Create your own Gmail address".
    COORDS_NEXT_AFTER_GMAIL = (592, 1210)          # Chú thích: Tọa độ của nút "Next" sau khi nhập Gmail.
    COORDS_PASSWORD_INPUT = (106, 540)            # Chú thích: Tọa độ của ô nhập "Password" (Mật khẩu).
    COORDS_NEXT_AFTER_PASSWORD = (592, 710)       # Chú thích: Tọa độ của nút "Next" sau khi nhập mật khẩu.
    COORDS_SKIP_OR_NEXT_FINAL = (590, 1198)       # Chú thích: Tọa độ của nút "Next" hoặc "Skip" ở các bước cuối cùng của việc tạo tài khoản.

    # !!! (CHÈN THÊM) TỌA ĐỘ CHO 2 HÀNH ĐỘNG NHẤN MỚI - BẠN HÃY CẬP NHẬT LẠI 2 TỌA ĐỘ NÀY !!!
    COORDS_TAP_AFTER_FIRST_NAME = (657, 1224)          # Chú thích: Tọa độ nhấn bất kỳ sau khi nhập First name.
    COORDS_TAP_AFTER_GMAIL = (690, 216)               # Chú thích: Tọa độ nhấn bất kỳ sau khi nhập Gmail.


    # --- Thông tin người dùng (sẽ được tạo tự động) ---
    INPUT_FIRST_NAME = ""
    INPUT_SURNAME = ""
    INPUT_DAY_OF_BIRTH = ""
    INPUT_YEAR_OF_BIRTH = ""
    INPUT_GMAIL_USERNAME = ""
    INPUT_PASSWORD = ""

# ==============================================================================
# PHẦN LOGIC - Các hàm để tạo ra các câu lệnh con
# ==============================================================================
def cmd_tap(x, y):
    # Hàm này tạo ra lệnh 'input tap' để mô phỏng một cú nhấn vào tọa độ (X, Y) trên màn hình.
    return f"input tap {x} {y}"

def cmd_type_text(text):
    # Hàm này tạo ra lệnh 'input text' để gõ một chuỗi văn bản vào ô đang được chọn (focus).
    # shlex.quote giúp xử lý các ký tự đặc biệt trong văn bản một cách an toàn.
    safe_text = shlex.quote(text)
    return f"input text {safe_text}"

def cmd_wait(seconds_str):
    # Hàm này tạo ra lệnh 'sleep' để tạm dừng kịch bản trong một khoảng thời gian (giây) nhất định.
    # ĐÃ SỬA: Chấp nhận chuỗi để tương thích với random.uniform
    return f"sleep {seconds_str}"

def cmd_keyevent(keycode):
    # Hàm này tạo ra lệnh 'input keyevent' để mô phỏng việc nhấn một phím cứng trên thiết bị (ví dụ: phím Home, Back, Enter).
    return f"input keyevent {keycode}"

def cmd_install_apk(path):
    # Hàm này tạo ra lệnh 'pm install' để cài đặt một tệp APK từ một đường dẫn cho trước trên thiết bị.
    # Cờ '-g' sẽ tự động cấp tất cả các quyền mà ứng dụng yêu cầu khi cài đặt.
    return f"pm install -g {path}"

def cmd_start_chrome(url):
    # Hàm này tạo ra lệnh 'am start' để khởi động ứng dụng Chrome và mở một URL cụ thể.
    return f'am start -n com.android.chrome/com.google.android.apps.chrome.Main -d "{url}"'

# ==============================================================================
# PHẦN CHÍNH - Nơi kịch bản được tạo ra
# ==============================================================================
def generate_script():
    commands = []
    cfg = Config()

    # --- TẠO THÔNG TIN NGƯỜI DÙNG NGẪU NHIÊN ---
    cfg.INPUT_SURNAME = random.choice(cfg.HO_VIETNAM)
    cfg.INPUT_FIRST_NAME = random.choice(cfg.TEN_VIETNAM)
    cfg.INPUT_DAY_OF_BIRTH = str(random.randint(1, 28))
    cfg.INPUT_YEAR_OF_BIRTH = str(random.randint(1990, 2004))
    
   # --- TẠO USERNAME HỢP LỆ VÀ DUY NHẤT ---
    first_name_lower = cfg.INPUT_FIRST_NAME.lower()
    surname_lower = cfg.INPUT_SURNAME.lower()
    year_short = cfg.INPUT_YEAR_OF_BIRTH[2:]
    
    # Tăng số lượng chữ số ngẫu nhiên lên 5 để đảm bảo tính duy nhất cao hơn
    random_numbers = ''.join(random.choices(string.digits, k=5))

    # Cập nhật lại các cấu trúc, loại bỏ dấu '_' không hợp lệ
    username_patterns = [
        f"{first_name_lower}{surname_lower}{random_numbers}",         # Ví dụ: trangvo12345
        f"{surname_lower}.{first_name_lower}{random_numbers}",       # Ví dụ: vo.trang12345
        f"{first_name_lower}.{year_short}{random_numbers}",          # SỬA LỖI: Đã thay thế dấu '_' bằng dấu '.'
        f"{surname_lower}{first_name_lower}{random_numbers}"        # Ví dụ: votrang12345
    ]

    # Chọn ngẫu nhiên một cấu trúc từ danh sách trên
    cfg.INPUT_GMAIL_USERNAME = random.choice(username_patterns)
    
    # --- TẠO MẬT KHẨU "GIỐNG NGƯỜI" HƠN ---
    words = ["xanh", "do", "tim", "vang", "buon", "vui", "nho", "yeu", "mua", "nang", "sky", "sun", "moon", "happy"]
    random_word1 = random.choice(words)
    random_word2 = random.choice(words)
    random_nums_pass = ''.join(random.choices(string.digits, k=3))
    special_char = random.choice("!@#$")
    cfg.INPUT_PASSWORD = f"{random_word1.capitalize()}{random_word2}{random_nums_pass}{special_char}"
    
    # In thông tin đã tạo ra để theo dõi (in ra stderr)
    print("--- ĐÃ TẠO THÔNG TIN NGƯỜI DÙNG NGẪU NHIÊN ---", file=sys.stderr)
    print(f"Ho: {cfg.INPUT_SURNAME}", file=sys.stderr)
    print(f"Ten: {cfg.INPUT_FIRST_NAME}", file=sys.stderr)
    print(f"Ngay sinh: {cfg.INPUT_DAY_OF_BIRTH}", file=sys.stderr)
    print(f"Nam sinh: {cfg.INPUT_YEAR_OF_BIRTH}", file=sys.stderr)
    print(f"Gmail: {cfg.INPUT_GMAIL_USERNAME}", file=sys.stderr)
    print(f"Mat khau: {cfg.INPUT_PASSWORD}", file=sys.stderr)
    print("------------------------------------------", file=sys.stderr)

    # --- SỬ DỤNG THỜI GIAN CHỜ NGẪU NHIÊN ---
    def rand_wait(base, variance=0.5):
        # Hàm trợ giúp để tạo thời gian chờ ngẫu nhiên
        # Ví dụ: rand_wait(3) sẽ cho ra số ngẫu nhiên từ 2.5 đến 3.5
        return f"{random.uniform(base - variance, base + variance):.2f}"

    # --- BƯỚC 0: TẢI VÀ CÀI ĐẶT SHELTER (DÙNG TỌA ĐỘ TUYỆT ĐỐI) ---
    commands.append("pm clear com.android.chrome") # Chú thích: Xóa sạch dữ liệu của Chrome để đưa về trạng thái gốc, đảm bảo kịch bản luôn bắt đầu từ điểm xuất phát giống nhau.
    commands.append(cmd_wait(rand_wait(3)))                   # Chú thích: Chờ 3 giây để hệ thống hoàn tất việc dọn dẹp.

    commands.append(cmd_start_chrome(cfg.APK_DOWNLOAD_URL)) # Chú thích: Mở ứng dụng Chrome với đường link tải tệp APK.
    commands.append(cmd_wait(rand_wait(5, 1)))                   # Chú thích: Chờ 5 giây để Chrome có thời gian khởi động và hiển thị màn hình đầu tiên.

    # --- Xử lý 2 trường hợp màn hình chào mừng của Chrome ---
    conditional_tap_command = (
        'uiautomator dump && '
        'if (grep -q "Accept &amp; continue" /sdcard/window_dump.xml); '
        f'then input tap {cfg.COORDS_CHROME_ACCEPT[0]} {cfg.COORDS_CHROME_ACCEPT[1]}; '
        f'else input tap {cfg.COORDS_CHROME_USE_WITHOUT_ACCOUNT[0]} {cfg.COORDS_CHROME_USE_WITHOUT_ACCOUNT[1]}; '
        'fi'
    )
    commands.append(conditional_tap_command)
    commands.append(cmd_wait(rand_wait(3)))                   # Chú thích: Chờ 3 giây để màn hình tiếp theo xuất hiện.

    # --- Chuỗi lệnh xử lý các màn hình cài đặt của Chrome theo thứ tự ---
    commands.append(cmd_tap(cfg.COORDS_CHROME_SYNC_NO[0], cfg.COORDS_CHROME_SYNC_NO[1])) # Chú thích: Nhấn vào tọa độ của nút "No, thanks" để bỏ qua việc đồng bộ.
    commands.append(cmd_wait(rand_wait(3)))                   # Chú thích: Chờ 3 giây để màn hình tiếp theo ("Chrome notifications") xuất hiện.

    commands.append(cmd_tap(cfg.COORDS_CHROME_NOTIF_CONTINUE[0], cfg.COORDS_CHROME_NOTIF_CONTINUE[1])) # Chú thích: Nhấn vào tọa độ của nút "Continue" để xử lý màn hình thông báo.
    commands.append(cmd_wait(rand_wait(5, 1)))                   # Chú thích: Chờ 5 giây để trang web tải file và hộp thoại cảnh báo có thể xuất hiện.

    # --- Sau khi đã qua các màn hình cài đặt, tiến hành tải file ---
    commands.append(cmd_tap(cfg.COORDS_CHROME_DOWNLOAD_ANYWAY[0], cfg.COORDS_CHROME_DOWNLOAD_ANYWAY[1])) # Chú thích: Nhấn vào nút "Download anyway" để xác nhận tải file.
    commands.append(cmd_wait(rand_wait(10, 2)))                  # Chú thích: Chờ 10 giây để đảm bảo tệp APK có đủ thời gian để tải về hoàn tất.

    commands.append(cmd_install_apk(cfg.APK_PATH_IN_VM)) # Chú thích: Cài đặt tệp APK vừa tải về từ thư mục Download.
    commands.append(cmd_wait(rand_wait(10, 2)))                  # Chú thích: Chờ 10 giây để quá trình cài đặt ứng dụng Shelter hoàn tất.

    commands.append(cmd_keyevent(3))               # Chú thích: Nhấn phím HOME để quay về màn hình chính của thiết bị.
    commands.append(cmd_wait(rand_wait(3)))                   # Chú thích: Chờ 3 giây để màn hình chính ổn định.

    # --- BƯỚC 1-9: CÀI ĐẶT SHELTER ---
    commands.append(cmd_tap(cfg.COORDS_ICON_SHELTER_HOME[0], cfg.COORDS_ICON_SHELTER_HOME[1])) # Chú thích: Nhấn vào biểu tượng ứng dụng Shelter trên màn hình chính.
    commands.append(cmd_wait(rand_wait(4)))                   # Chú thích: Chờ 4 giây để ứng dụng khởi động.

    # Chú thích: Vòng lặp để nhấn nút "Next" hoặc "Continue" 4 lần liên tiếp.
    for _ in range(4):
        commands.append(cmd_tap(cfg.COORDS_NEXT_BUTTON[0], cfg.COORDS_NEXT_BUTTON[1])) # Chú thích: Nhấn vào nút "Next".
        commands.append(cmd_wait(rand_wait(2)))               # Chú thích: Chờ 2 giây giữa mỗi lần nhấn.

    commands.append(cmd_tap(cfg.COORDS_ACCEPT_CONTINUE[0], cfg.COORDS_ACCEPT_CONTINUE[1])) # Chú thích: Nhấn vào nút "Accept and continue" để đồng ý với điều khoản.
    commands.append(cmd_wait(rand_wait(17, 3)))                  # Chú thích: Chờ 17 giây để Shelter thiết lập môi trường làm việc.

    commands.append(cmd_tap(cfg.COORDS_NEXT_AFTER_SETUP[0], cfg.COORDS_NEXT_AFTER_SETUP[1])) # Chú thích: Nhấn nút "Next" sau khi thiết lập xong.
    commands.append(cmd_wait(rand_wait(10, 2)))                  # Chú thích: Chờ 10 giây để màn hình yêu cầu quyền xuất hiện.

    commands.append(cmd_tap(cfg.COORDS_ALLOW[0], cfg.COORDS_ALLOW[1])) # Chú thích: Nhấn "ALLOW" để cấp quyền quản trị thiết bị cho Shelter.
    commands.append(cmd_wait(rand_wait(5, 1)))                   # Chú thích: Chờ 5 giây để vào màn hình chính của Shelter.

    # --- (ĐOẠN CHÈN THÊM) NHẤN HOME VÀ QUAY LẠI APP ---
    commands.append(cmd_keyevent(3))               # Chú thích: Nhấn phím HOME để quay về màn hình chính.
    commands.append(cmd_wait(rand_wait(3)))                   # Chú thích: Chờ 3 giây.
    commands.append(cmd_tap(cfg.COORDS_ICON_SHELTER_HOME[0], cfg.COORDS_ICON_SHELTER_HOME[1])) # Chú thích: Nhấn vào icon Shelter để mở lại app.
    commands.append(cmd_wait(rand_wait(3)))                   # Chú thích: Chờ 3 giây để app mở lại.

    # --- BƯỚC 10-17: CLONE ỨNG DỤNG ---
    commands.append(cmd_tap(cfg.COORDS_3_DOTS_MENU[0], cfg.COORDS_3_DOTS_MENU[1])) # Chú thích: Nhấn vào menu 3 chấm ở góc trên bên phải.
    commands.append(cmd_wait(rand_wait(2)))                   # Chú thích: Chờ 2 giây để menu xổ xuống.

    commands.append(cmd_tap(cfg.COORDS_SHOW_ALL_APPS[0], cfg.COORDS_SHOW_ALL_APPS[1])) # Chú thích: Nhấn vào mục "Show All Apps" để hiển thị tất cả ứng dụng.
    commands.append(cmd_wait(rand_wait(3)))                   # Chú thích: Chờ 3 giây để danh sách ứng dụng tải.

    commands.append(cmd_tap(cfg.COORDS_CONTINUE[0], cfg.COORDS_CONTINUE[1])) # Chú thích: Nhấn "CONTINUE" nếu có hộp thoại thông báo.
    commands.append(cmd_wait(rand_wait(5, 1)))                   # Chú thích: Chờ 5 giây để vào danh sách ứng dụng hệ thống.

    commands.append(cmd_tap(cfg.COORDS_SEARCH_ICON[0], cfg.COORDS_SEARCH_ICON[1])) # Chú thích: Nhấn vào biểu tượng kính lúp để tìm kiếm.
    commands.append(cmd_wait(rand_wait(2)))                   # Chú thích: Chờ 2 giây để bàn phím hiện ra.

    commands.append(cmd_type_text('google play'))  # Chú thích: Gõ từ khóa "google play" vào ô tìm kiếm.
    commands.append(cmd_wait(rand_wait(3)))                   # Chú thích: Chờ 3 giây để kết quả tìm kiếm hiển thị.

    commands.append(cmd_tap(cfg.COORDS_GOOGLE_PLAY_STORE_ITEM[0], cfg.COORDS_GOOGLE_PLAY_STORE_ITEM[1])) # Chú thích: Nhấn vào ứng dụng "Google Play Store" trong kết quả.
    commands.append(cmd_wait(rand_wait(2)))                   # Chú thích: Chờ 2 giây.

    commands.append(cmd_tap(cfg.COORDS_CLONE_TO_SHELTER[0], cfg.COORDS_CLONE_TO_SHELTER[1])) # Chú thích: Nhấn vào nút "Clone to Shelter" để nhân bản ứng dụng.
    commands.append(cmd_wait(rand_wait(3)))                  # Chú thích: Chờ 3 giây để quá trình nhân bản hoàn tất.

    commands.append(cmd_tap(cfg.COORDS_GOOGLE_PLAY_SERVICES_ITEM[0], cfg.COORDS_GOOGLE_PLAY_SERVICES_ITEM[1])) # Chú thích: Nhấn vào ứng dụng "Google Play services".
    commands.append(cmd_wait(rand_wait(2)))                   # Chú thích: Chờ 2 giây.

    commands.append(cmd_tap(cfg.COORDS_CLONE_TO_SHELTER[0], cfg.COORDS_CLONE_TO_SHELTER[1])) # Chú thích: Nhấn "Clone to Shelter" để nhân bản dịch vụ Google Play.
    commands.append(cmd_wait(rand_wait(3)))                  # Chú thích: Chờ 3 giây để quá trình nhân bản hoàn tất.

    # --- BƯỚC 18-31: TẠO TÀI KHOẢN GOOGLE ---
    commands.append(cmd_keyevent(3))               # Chú thích: Nhấn phím HOME để quay về màn hình chính.
    commands.append(cmd_wait(rand_wait(3)))                   # Chú thích: Chờ 3 giây.

    commands.append(cmd_tap(cfg.COORDS_PLAY_STORE_ICON_HOME[0], cfg.COORDS_PLAY_STORE_ICON_HOME[1])) # Chú thích: Nhấn vào biểu tượng Play Store đã được nhân bản (có cặp sách).
    commands.append(cmd_wait(rand_wait(5, 1)))                  # Chú thích: Chờ 5 giây để Play Store khởi động.

    commands.append(cmd_tap(cfg.COORDS_SIGN_IN[0], cfg.COORDS_SIGN_IN[1])) # Chú thích: Nhấn vào nút "Sign in".
    commands.append(cmd_wait(rand_wait(7, 1)))                   # Chú thích: Chờ 7 giây để màn hình đăng nhập tải.

    commands.append(cmd_tap(cfg.COORDS_CREATE_ACCOUNT[0], cfg.COORDS_CREATE_ACCOUNT[1])) # Chú thích: Nhấn vào nút "Create account" để bắt đầu tạo tài khoản.
    commands.append(cmd_wait(rand_wait(3)))                   # Chú thích: Chờ 3 giây.

    commands.append(cmd_tap(cfg.COORDS_FOR_MY_PERSONAL_USE[0], cfg.COORDS_FOR_MY_PERSONAL_USE[1])) # Chú thích: Nhấn vào tùy chọn "For my personal use".
    commands.append(cmd_wait(rand_wait(3)))                   # Chú thích: Chờ 3 giây.

    commands.append(cmd_tap(cfg.COORDS_FIRST_NAME_INPUT[0], cfg.COORDS_FIRST_NAME_INPUT[1])) # Chú thích: Nhấn vào ô nhập "First name".
    commands.append(cmd_wait(rand_wait(2)))                   # Chú thích: Chờ 2 giây.

    commands.append(cmd_type_text(cfg.INPUT_FIRST_NAME)) # Chú thích: Gõ Tên vào ô.
    commands.append(cmd_wait(rand_wait(2)))                   # Chú thích: Chờ 2 giây.

    commands.append(cmd_tap(cfg.COORDS_TAP_AFTER_FIRST_NAME[0], cfg.COORDS_TAP_AFTER_FIRST_NAME[1])) # Chú thích: Nhấn vào vị trí bất kỳ sau khi nhập First name.
    commands.append(cmd_wait(rand_wait(2)))                   # Chú thích: Chờ 2 giây.

    commands.append(cmd_tap(cfg.COORDS_SURNAME_INPUT[0], cfg.COORDS_SURNAME_INPUT[1])) # Chú thích: Nhấn vào ô nhập "Surname".
    commands.append(cmd_wait(rand_wait(2)))                   # Chú thích: Chờ 2 giây.

    commands.append(cmd_type_text(cfg.INPUT_SURNAME)) # Chú thích: Gõ Họ vào ô.
    commands.append(cmd_wait(rand_wait(2)))                   # Chú thích: Chờ 2 giây.

    commands.append(cmd_tap(cfg.COORDS_NEXT_AFTER_NAME[0], cfg.COORDS_NEXT_AFTER_NAME[1])) # Chú thích: Nhấn "Next" sau khi đã nhập tên.
    commands.append(cmd_wait(rand_wait(3)))                   # Chú thích: Chờ 3 giây để chuyển sang màn hình nhập ngày sinh.

    commands.append(cmd_tap(cfg.COORDS_DAY_INPUT[0], cfg.COORDS_DAY_INPUT[1])) # Chú thích: Nhấn vào ô nhập "Day" (Ngày).
    commands.append(cmd_wait(rand_wait(2)))                   # Chú thích: Chờ 2 giây.

    commands.append(cmd_type_text(cfg.INPUT_DAY_OF_BIRTH)) # Chú thích: Gõ ngày sinh.
    commands.append(cmd_tap(cfg.COORDS_MONTH_DROPDOWN[0], cfg.COORDS_MONTH_DROPDOWN[1])) # Chú thích: Nhấn vào ô chọn "Month" (Tháng).
    commands.append(cmd_wait(rand_wait(2)))                   # Chú thích: Chờ 2 giây.

    commands.append(cmd_tap(cfg.COORDS_MONTH_FEBRUARY[0], cfg.COORDS_MONTH_FEBRUARY[1])) # Chú thích: Chọn tháng Hai trong danh sách.
    commands.append(cmd_wait(rand_wait(2)))                   # Chú thích: Chờ 2 giây.

    commands.append(cmd_tap(cfg.COORDS_YEAR_INPUT[0], cfg.COORDS_YEAR_INPUT[1])) # Chú thích: Nhấn vào ô nhập "Year" (Năm).
    commands.append(cmd_wait(rand_wait(2)))                   # Chú thích: Chờ 2 giây.

    commands.append(cmd_type_text(cfg.INPUT_YEAR_OF_BIRTH)) # Chú thích: Gõ năm sinh.
    commands.append(cmd_wait(rand_wait(2)))                   # Chú thích: Chờ 2 giây.

    commands.append(cmd_tap(cfg.COORDS_GENDER_DROPDOWN[0], cfg.COORDS_GENDER_DROPDOWN[1])) # Chú thích: Nhấn vào ô chọn "Gender" (Giới tính).
    commands.append(cmd_wait(rand_wait(2)))                   # Chú thích: Chờ 2 giây.

    commands.append(cmd_tap(cfg.COORDS_GENDER_MALE_OR_FEMALE[0], cfg.COORDS_GENDER_MALE_OR_FEMALE[1])) # Chú thích: Chọn một giới tính trong danh sách.
    commands.append(cmd_wait(rand_wait(2)))                   # Chú thích: Chờ 2 giây.

    commands.append(cmd_tap(cfg.COORDS_NEXT_AFTER_DOB[0], cfg.COORDS_NEXT_AFTER_DOB[1])) # Chú thích: Nhấn "Next" sau khi nhập xong ngày sinh.
    commands.append(cmd_wait(rand_wait(5, 1)))                   # Chú thích: Chờ 5 giây để chuyển màn hình.

    commands.append(cmd_tap(cfg.COORDS_CREATE_OWN_GMAIL[0], cfg.COORDS_CREATE_OWN_GMAIL[1])) # Chú thích: Nhấn vào tùy chọn "Create your own Gmail address".
    commands.append(cmd_wait(rand_wait(3)))                   # Chú thích: Chờ 3 giây.

    commands.append(cmd_type_text(cfg.INPUT_GMAIL_USERNAME)) # Chú thích: Gõ tên người dùng Gmail mong muốn.
    commands.append(cmd_wait(rand_wait(2)))                   # Chú thích: Chờ 2 giây.

    commands.append(cmd_tap(cfg.COORDS_TAP_AFTER_GMAIL[0], cfg.COORDS_TAP_AFTER_GMAIL[1])) # Chú thích: Nhấn vào vị trí bất kỳ sau khi nhập Gmail.
    commands.append(cmd_wait(rand_wait(2)))                   # Chú thích: Chờ 2 giây.

    commands.append(cmd_tap(cfg.COORDS_NEXT_AFTER_GMAIL[0], cfg.COORDS_NEXT_AFTER_GMAIL[1])) # Chú thích: Nhấn "Next" sau khi nhập Gmail.
    commands.append(cmd_wait(rand_wait(5, 1)))                   # Chú thích: Chờ 5 giây.

    commands.append(cmd_tap(cfg.COORDS_PASSWORD_INPUT[0], cfg.COORDS_PASSWORD_INPUT[1])) # Chú thích: Nhấn vào ô nhập "Password".
    commands.append(cmd_wait(rand_wait(2)))                   # Chú thích: Chờ 2 giây.

    commands.append(cmd_type_text(cfg.INPUT_PASSWORD)) # Chú thích: Gõ mật khẩu.
    commands.append(cmd_wait(rand_wait(2)))                   # Chú thích: Chờ 2 giây.

    commands.append(cmd_tap(cfg.COORDS_NEXT_AFTER_PASSWORD[0], cfg.COORDS_NEXT_AFTER_PASSWORD[1])) # Chú thích: Nhấn "Next" sau khi nhập mật khẩu.
    commands.append(cmd_wait(rand_wait(5, 1)))                   # Chú thích: Chờ 5 giây.

    commands.append(cmd_tap(cfg.COORDS_SKIP_OR_NEXT_FINAL[0], cfg.COORDS_SKIP_OR_NEXT_FINAL[1])) # Chú thích: Nhấn "Next" hoặc "Skip" ở các bước cuối cùng.
    
    # --- HIỂN THỊ THÔNG TIN TÀI KHOẢN TRÊN CONSOLE ---
    display_credentials_command = (
        f"echo '========== TAI KHOAN DA TAO =========='; "
        f"echo 'Gmail: {cfg.INPUT_GMAIL_USERNAME}@gmail.com'; "
        f"echo 'Mat khau: {cfg.INPUT_PASSWORD}'; "
        f"echo '======================================='"
    )
    commands.append(display_credentials_command)

    full_script = " && ".join(commands)
    return full_script

# ==============================================================================
# ĐIỂM BẮT ĐẦU CHẠY SCRIPT
# ==============================================================================
if __name__ == "__main__":
    final_script = generate_script()
    
    # Chỉ in ra thông báo cho người dùng trên màn hình console (in ra stderr)
    print("========= SAO CHÉP TOÀN BỘ LỆNH BÊN DƯỚI =========", file=sys.stderr)
    
    # Chỉ in chuỗi lệnh cuối cùng ra stdout (để chuyển hướng vào file)
    print(final_script)
    
    # Chỉ in ra thông báo cho người dùng trên màn hình console (in ra stderr)
    print("===================================================", file=sys.stderr)