import os
import tkinter.messagebox as msgbox


def run_none(event):
    pass


def run_cmd(event):
    os.system("start")


def run_calc(event):
    os.system('start calc')


def run_notebook(event):
    os.system('start notepad')


def run_control_panel(event):
    os.system('start control')


def run_regedit(event):
    os.system('start regedit')


def run_services(event):
    os.system('start services.msc')


def run_winver(event):
    os.system('start winver')


def run_explorer(event):
    os.system('start explorer')


def run_write(event):
    os.system('start writer')


def run_mspaint(event):
    os.system('start mspaint')


