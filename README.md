# Thông tin nhóm
STT: 41

1712858 - Nguyễn Ngọc Tú

1712495 - Nguyễn Quang Huy

# Giới thiệu đồ án

Phân loại bài viết trên [voz.vn](voz.vn) vào forum có chủ đề phù hợp dựa trên nội dung.

Dựa trên nội dung, các bài viết sẽ được tự động phân loại vào một trong 4 forum: [Phim/Nhạc Sách](https://voz.vn/f/phim-nhac-sach.65/), [Điện thoại di động](https://voz.vn/f/dien-thoai-di-dong.76/), [4 bánh](https://voz.vn/f/4-banh.38/), [Đồ điện tử & Thiết bị gia dụng](https://voz.vn/f/do-dien-tu-thiet-bi-gia-dung.10/)

# Quy trình thực hiện
1. Crawl dữ liệu từ [voz.vn](voz.vn) bằng thư viện [Scrapy](scrapy.org)  
2. Sau khi crawl xong, thu được các dữ liệu:
	- postTitle: tiêu đề bài viết
	- postContent: nội dung bài viết
	- postLink: URL của bài viết
	- forumName: tên forum mà bài viết thuộc về

Tuy nhiên, khi huấn luyện mô hình thì chỉ dùng tới postContent và forumName

3. Sử dụng Deep Learning để huấn luyện mô hình dự đoán forumName dựa vào postContent

Giải thích model : https://github.com/qhuy4119/1712858-1712495-nmkhdl/blob/main/Description%20model.pdf

# Các thông tin khác
Phân chia công việc: https://github.com/qhuy4119/1712858-1712495-nmkhdl/blob/main/Teamwork.pdf
