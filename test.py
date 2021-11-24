
import win32api
fname = "C:/Users/Chatraporn.yon/Desktop/python_app/qrcode_pdf/document-output__13-35-25.pdf"
win32api.ShellExecute(0, "print", fname, None,  ".",  0)
