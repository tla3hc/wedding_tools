name = 'Lợi'
gental = 'em'

dai_tu_nhan_xung = ''
if gental == 'anh':
    dai_tu_nhan_xung = 'em'
elif gental == 'chị':
    dai_tu_nhan_xung = 'em'
elif gental == 'cô':
    dai_tu_nhan_xung = 'cháu'
elif gental == 'chú':
    dai_tu_nhan_xung = 'cháu'
elif gental == 'bạn':
    dai_tu_nhan_xung = 'mình'
elif gental == 'em':
    dai_tu_nhan_xung = 'anh'
else:
    dai_tu_nhan_xung = 'mình'

template = '''Thân gửi {gental} {name},
Trước hết {dai_tu_nhan_xung} thành thật xin lỗi và lấy làm tiếc khi không thể gặp trực tiếp gửi thiệp mời đám cưới. Mong {gental} {name} sắp xếp chút thời gian đến tiệc mừng và dự lễ thành hôn của {dai_tu_nhan_xung}.
Tiệc mừng được tổ chức vào lúc 9 giờ, sáng chủ nhật, ngày 22/09/2024, tại nhà trai, Thôn Giai Lệ, Lệ Xá, Tiên Lữ, Hưng Yên. 
Lễ thành hôn được tổ chức vào lúc 8 giờ, sáng chủ nhật, ngày 22/09/2024.  
{dai_tu_nhan_xung} nhắn tin này chân thành mời {gental} {name} đến tham dự chung vui cùng {dai_tu_nhan_xung}. Sự hiện diện của {gental} {name} là niềm vinh dự của {dai_tu_nhan_xung} và gia đình. Cảm ơn {gental} {name} rất nhiều!'''

print(template.format(gental=gental, name=name, dai_tu_nhan_xung=dai_tu_nhan_xung))