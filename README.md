STT: 41

1712858 - Nguyễn Ngọc Tú

1712495 - Nguyễn Quang Huy

Demo website: [https://voz-text-classification.herokuapp.com](https://voz-text-classification.herokuapp.com/)

Giải thích model Bidirectional LSTM dùng dự đoán thể loại tin tức :

Sử dụng embeđing Word2Vec (link tải trong code)

Sử dụng tách từ của thư viện ViTokenizer

Text sẽ được chuyển thành dạng số bởi thư iện Tokenizer()

Và được chuẩn hóa về kích thước vector 300 trước khi đưa vào mô hình

Tiếp theo sẽ qua lớp Embedding (Word2Vec)

Tiếp theo qua lớp Bidirectional LSTM

Tiếp theo qua lớp Linear với hàm kích hoạt là softmax => Đầu ra là xác suất cho từng class
