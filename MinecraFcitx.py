import tkinter as tk
import pyclip
#import keyboard
import sys
import os
#import subprocess

if sys.platform=="win32":
    print("Windows detected")
    print("This program is not required on Windows, try IngameIME mod instead.")
    os._exit(0)


if len(sys.argv)>1:
    close_win=sys.argv[1].startswith("--close-instead-of-minimize")
else:
    close_win=False


def done(text:str):
    global win
    pyclip.copy(text)
    if close_win:
        os._exit(0)
    else:
        win.iconify()

win=tk.Tk()
win.title("在此输入中文 - MinecraFcitx")
win.attributes("-topmost",True)

text_input=tk.Text(win,relief="flat")
copy_btn=tk.Button(win,text="复制文本",bg="#000050",fg="#ffffff",command=lambda:pyclip.copy(text_input.get(1.0,tk.END)))
done_btn=tk.Button(win,text="复制文本并{after_action} (ENTER)".format(after_action="关闭" if close_win else "最小化"),
                   bg="#005000",fg="#ffffff",command=lambda:done(text_input.get(1.0,tk.END)))

done_btn.pack(fill=tk.X,side=tk.BOTTOM)
copy_btn.pack(fill=tk.X,side=tk.BOTTOM)
text_input.pack(fill=tk.BOTH,expand=True)

text_input.bind("<KeyRelease-Return>",lambda event:done(text_input.get(1.0,tk.END)))
win.bind("<KeyRelease-Return>",lambda event:done(text_input.get(1.0,tk.END)))

win.update()
win.geometry("300x150+{x}+{y}".format(x=str((win.winfo_screenwidth()-win.winfo_width())//2),
                                      y=str((win.winfo_screenheight()-win.winfo_height())//2)))

win.mainloop()
