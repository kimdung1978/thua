import PySimpleGUI as sg
import trolyao

def main():
    layout = [
        [sg.Text("Tên Đăng Nhập")],
        [sg.Input(key= 'tendangnhap')],
        [sg.Text("Mật Khẩu")],
        [sg.Input(key='matkhau')],
        [sg.Button("Đăng Nhập"), sg.Button("Exit")],
        [sg.Text("",key="tinnhan")]
    ]
    window = sg.Window("Trí tuệ nhân tạo", layout)
    while True:
        event, values = window.read()
        if event == sg.WINDOW_CLOSED or event == 'Exit':
            break
        elif event == 'Đăng Nhập':
            if values['tendangnhap'] == 'admin' and values['matkhau'] == '123':
                window['tinnhan'].Update("Đăng Nhập Thành Công")
                trolyao.main()
                window.hide()
                window.un_hide()

            else:
                window['tinnhan'].Update("Đăng Nhập Không Thành Công")
    window.close()
if __name__ == '__main__':
    main()
