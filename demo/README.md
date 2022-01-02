Ở tab Storage khi ấn vào 1 dòng trong listbox sẽ đợi khoảng 1 -> 2s để ảnh tải từ firebase mới hiện ra. Ảnh được hiện thỉ lấy từ ảnh output.jpg ngay tại source code.

Mỗi lần upload ảnh ở tab upload thì qua Storage có nút refresh ấn vào nó sẽ cập nhập ảnh vừa up vào lsitbox.

Còn phần mã hóa ảnh thì trong source này chưa có. Nhưng t đã demo ở ngoài với cách làm là lấy 3 channels RBG của ảnh để mã hóa từng phần tử trong matrix. Thì mã hóa được rồi nhưng có 2 vấn đề:
    1)Nếu khóa lớn thì mã hóa sẽ rất chậm. Mất tầm 10 phút cho ảnh 1800x1800 với khóa 256 bit
    2)Vì cách t mã hóa trên 3 channels RBG của ảnh. Mà mỗi phần tử trong matrix có giá trị trong [0,255] nên muốn giải mã phải có 1 biến giữ giá trị gốc sau khi mã hóa.

có thể đổi file json thành firebase khác để chạy. Nhớ đổi phần auth trong app.py
