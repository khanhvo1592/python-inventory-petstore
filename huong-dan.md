# Hướng dẫn cài đặt và chạy dự án Inventory Management System

## Cấu trúc dự án
/
├── inventory/                    # App chính quản lý kho hàng
│   ├── migrations/              # Các file migration của database
│   │   └── __init__.py
│   ├── templates/               # Các template HTML
│   │   └── inventory/
│   │       ├── base.html       # Template cơ sở
│   │       ├── supply_list.html # Danh sách sản phẩm
│   │       ├── supply_form.html # Form thêm/sửa sản phẩm
│   │       ├── location_list.html # Danh sách vị trí
│   │       ├── location_form.html # Form thêm/sửa vị trí
│   │       ├── user_list.html  # Danh sách người dùng
│   │       ├── user_form.html  # Form thêm/sửa người dùng
│   │       └── alert_list.html # Danh sách cảnh báo
│   ├── static/                  # Các file tĩnh
│   │   ├── css/                # CSS files
│   │   ├── js/                 # JavaScript files
│   │   └── images/             # Image files
│   ├── models.py               # Các model của ứng dụng
│   ├── views.py                # Các view xử lý logic
│   ├── urls.py                 # Các URL pattern
│   ├── admin.py                # Cấu hình admin site
│   ├── forms.py                # Các form class
│   ├── tests.py                # Unit tests
│   └── __init__.py             # Đánh dấu thư mục là package
├── inventory_management/        # Project settings
│   ├── settings.py             # Cài đặt dự án
│   ├── urls.py                 # URL chính
│   ├── wsgi.py                 # WSGI config
│   ├── asgi.py                 # ASGI config
│   └── __init__.py             # Đánh dấu thư mục là package
├── manage.py                   # Django management script
├── requirements.txt            # Các package cần thiết
├── README.md                   # Tài liệu dự án
├── .gitignore                  # Git ignore file
└── db.sqlite3                  # Database file

## Mô tả chi tiết các thành phần

### 1. Thư mục inventory/
- **migrations/**: Chứa các file migration để quản lý thay đổi database
- **templates/**: Chứa các template HTML
  - `base.html`: Template cơ sở với layout chung
  - `supply_list.html`: Hiển thị danh sách sản phẩm
  - `supply_form.html`: Form thêm/sửa sản phẩm
  - `location_list.html`: Hiển thị danh sách vị trí
  - `location_form.html`: Form thêm/sửa vị trí
  - `user_list.html`: Hiển thị danh sách người dùng
  - `user_form.html`: Form thêm/sửa người dùng
  - `alert_list.html`: Hiển thị danh sách cảnh báo

- **static/**: Chứa các file tĩnh
  - `css/`: Các file CSS
  - `js/`: Các file JavaScript
  - `images/`: Các file hình ảnh

- **models.py**: Định nghĩa các model
  - Supply: Model sản phẩm
  - Location: Model vị trí
  - User: Model người dùng
  - Alert: Model cảnh báo

- **views.py**: Xử lý logic
  - CRUD operations cho các model
  - Xử lý form
  - Kiểm tra quyền truy cập
  - Xử lý cảnh báo

- **urls.py**: Định nghĩa URL patterns
  - URL cho các view
  - URL cho API endpoints

- **admin.py**: Cấu hình admin interface
  - Đăng ký models
  - Tùy chỉnh hiển thị

- **forms.py**: Định nghĩa các form
  - SupplyForm
  - LocationForm
  - UserForm

- **tests.py**: Unit tests
  - Test models
  - Test views
  - Test forms

### 2. Thư mục inventory_management/
- **settings.py**: Cài đặt dự án
  - Database configuration
  - Installed apps
  - Middleware
  - Templates
  - Static files
  - Security settings

- **urls.py**: URL patterns chính
  - Include app URLs
  - Admin URLs
  - API URLs

- **wsgi.py**: WSGI configuration
- **asgi.py**: ASGI configuration

### 3. Các file khác
- **manage.py**: Django management script
- **requirements.txt**: Danh sách dependencies
- **README.md**: Tài liệu dự án
- **.gitignore**: Git ignore rules
- **db.sqlite3**: SQLite database file

## Yêu cầu hệ thống
- Python 3.8 trở lên
- pip (Python package manager)
- Virtual environment (khuyến khích)

## Các bước cài đặt

1. **Cài đặt môi trường ảo (Virtual Environment)**
   ```bash
   # Tạo môi trường ảo
   python -m venv venv

   # Kích hoạt môi trường ảo
   # Trên Windows:
   venv\Scripts\activate
   # Trên macOS/Linux:
   source venv/bin/activate
   ```

2. **Cài đặt các package cần thiết**
   ```bash
   pip install -r requirements.txt
   ```

3. **Cấu hình database**
   ```bash
   # Tạo các bảng trong database
   python manage.py makemigrations
   python manage.py migrate
   ```

4. **Tạo superuser (quản trị viên)**
   ```bash
   python manage.py createsuperuser
   ```

5. **Chạy server**
   ```bash
   python manage.py runserver
   ```

## Hướng dẫn sử dụng

1. **Đăng nhập**
   - Truy cập http://localhost:8000/admin/
   - Đăng nhập bằng tài khoản superuser đã tạo

2. **Quản lý sản phẩm (Supplies)**
   - Xem danh sách sản phẩm: http://localhost:8000/inventory/supplies/
   - Thêm sản phẩm mới: Click "Add New Supply"
   - Sửa thông tin sản phẩm: Click biểu tượng edit
   - Xóa sản phẩm: Click biểu tượng delete
   - Lọc sản phẩm low stock: Sử dụng checkbox "Show Low Stock Only"
   - Tìm kiếm sản phẩm: Sử dụng ô tìm kiếm

3. **Quản lý vị trí (Locations)**
   - Xem danh sách vị trí: http://localhost:8000/inventory/locations/
   - Thêm vị trí mới: Click "Add New Location"
   - Sửa thông tin vị trí: Click biểu tượng edit
   - Xóa vị trí: Click biểu tượng delete

4. **Quản lý người dùng (User Management)**
   - Xem danh sách người dùng: http://localhost:8000/inventory/users/
   - Thêm người dùng mới: Click "Add New User"
   - Sửa thông tin người dùng: Click biểu tượng edit
   - Xóa người dùng: Click biểu tượng delete

5. **Quản lý cảnh báo (Alerts)**
   - Xem danh sách cảnh báo: http://localhost:8000/inventory/alerts/
   - Đánh dấu đã đọc: Click "Mark as Read"
   - Xóa cảnh báo: Click biểu tượng delete

## Tính năng chính
- Quản lý sản phẩm với thông tin chi tiết
- Quản lý vị trí kho hàng
- Quản lý người dùng và phân quyền
- Cảnh báo tự động khi sản phẩm sắp hết hàng
- Tìm kiếm và lọc sản phẩm nhanh chóng

