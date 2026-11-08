ĐỀ CƯƠNG BTL
1. Tên đề tài: Mô hình Logistic dự báo sự bùng nổ số lượng thiết bị kết nối IoT trong một hệ thống Smart Home.
2. Nhóm AC
Thành viên: 
	Đinh Anh Tuấn - 2413767
	Nguyễn Lê Quang Minh  - 2613244
	Nguyễn Thanh Tú - 2612458
	Nguyễn Thảo Vi - 2610353
	Trần Anh Tuấn - 2413808 
3. Bối cảnh và vấn đề
Sự phát triển của xu hướng Smart Home dẫn đến sự gia tăng mạnh mẽ các thiết bị kết nối vạn vật (IoT) trong các hộ gia đình. Vấn đề đặt ra cho các kỹ sư viễn thông là cần dự báo số lượng thiết bị kết nối IoT tối đa vào một hệ thống mạng trung tâm ở tương lai dựa trên tốc độ tăng trưởng hiện tại. Từ đó, đưa ra các tính toán quy hoạch và nâng cấp băng thông mạng kịp thời để tránh tình trạng quá tải hệ thống.
4. Mục tiêu
Xây dựng mô hình toán học (Logistic) mô phỏng quỹ đạo tăng trưởng số lượng thiết bị IoT kết nối vào hệ thống Smart Home.
Xác định thời điểm "bùng phát" (thời điểm tốc độ kết nối thiết bị mới tăng cao nhất) để lên kế hoạch nâng cấp hạ tầng vật lý.
Tính toán số lượng thiết bị kết nối tối đa (ngưỡng bão hòa) nhằm định cỡ và cấp phát đủ tài nguyên mạng dài hạn.
5. Nội dung chính
Thu thập và nội suy dữ liệu giả định về số lượng thiết bị kết nối.
Thiết lập phương trình cân bằng sự gia tăng lượng người dùng theo thời gian. (Công cụ 1: Phương trình vi phân Logistic P'(t)=kP(t)(1-(P(t))/K)).
Khảo sát hàm tốc độ $P'(t)$ để xác định điểm bùng phát gây áp lực lớn nhất lên băng thông. (Công cụ 2: Đạo hàm cấp 1 và cấp 2).
Tính toán sức chịu tải tối đa của hệ thống trước khi bão hòa. (Công cụ 3: Giới hạn (lim)┬(t→∞) P(t)=K).
6. Phương pháp / Dữ liệu / Code
Mô hình sử dụng: Mô hình tăng trưởng Logistic.
Dữ liệu: Dữ liệu giả định được nội suy dựa trên các báo cáo thực tế về hạ tầng kết nối viễn thông và thiết bị IoT.
Công cụ code: Sử dụng thư viện scipy và matplotlib của Python để hồi quy (curve fitting) khớp mô hình toán học với dữ liệu và vẽ đồ thị hàm số.
7. Kết quả dự kiến & Tài liệu tham khảo
Sản phẩm dự kiến: Một báo cáo phân tích bằng toán học về quỹ đạo kết nối, kèm đồ thị code Python mô phỏng đường cong Logistic xác định trực quan thời điểm cảnh báo quá tải mạng.
Tài liệu tham khảo:
[1] S.T. Tan, Single Variable Calculus, Cengage Learning, 2011 (Mục 7.3: Phương trình logistic).
[2] J. Stewart, D. Clegg, S. Watson, Calculus, 9th ed, Cengage Learning, 2021.

