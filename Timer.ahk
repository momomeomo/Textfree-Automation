;#Warn
SendMode Input
#KeyHistory 0
#NoEnv
#SingleInstance Force
SetTitleMatchMode, 3
SetTitleMatchMode, Slow
DetectHiddenWindows, off
ListLines, off
SetControlDelay, -1
CoordMode, Mouse, Window

Gui, font, s14, Arial, cBlack, w700 

Gui, Color , ffffff, ffffff

Gui, Add, Text, cBlack x30 y80 w100 h40 , &Hours:
Gui, Add, Edit, cBlack x30 y110 w98 h40 Number vcd_HoursEdit gTimeEdited, % cd_Duration // 3600
Gui, Add, Text, cBlack x130 y80 w100 h40 , &Minutes:
Gui, Add, Edit, cBlack x130 y110 w98 h40 Number vcd_MinutesEdit gTimeEdited, % mod(cd_Duration, 3600) // 60
Gui, Add, Text, cBlack x230 y80 w100 h40 , S&econds:
Gui, Add, Edit, cBlack x230 y110 w100;w98 h40 Number vcd_SecondsEdit gTimeEdited, % mod(cd_Duration, 60)
Gui, Add, Text, cBlack x30 y166 w415;w410 h40 vcd_DurationText,
Gui, Add, Button, vcd_Button gCountDownPress Default, &Start (Press Enter)
Gui, Add, Checkbox, vOpt1, SMS row: 1
Gui, Add, Checkbox, vOpt2, SMS row: 2
Gui, Add, Checkbox, vOpt3, SMS row: 3
Gui, Add, Checkbox, vOpt4, SMS row: 4
Gui, Add, Checkbox, vOpt5, SMS row: 5
Gui, Add, Checkbox, vOpt6, SMS row: 6
Gui, Add, Checkbox, vOpt7, SMS row: 7
Gui, Add, Checkbox, vOpt8, SMS row: 8
Gui, Add, Checkbox, vOpt9, SMS row: 9
Gui, Add, Checkbox, vOpt10, SMS row: 10
Gui, Add, Checkbox, vOpt11, SMS row: 11
Gui, Add, Checkbox, vOpt12, SMS row: 12
Gui, Add, Button, gLabel, 
Gosub TimeEdited
Gui, Show,, CountDown
Gui +LastFound
cd_Gui := WinExist() ; Remember Gui window ID
Return

CountDownPress:
GuiControlGet cd_ButtonCaption,, cd_Button
if cd_ButtonCaption = &STOP ; Compare button text
{
  SetTimer CountDownTimer, Off
  WinSetTitle ahk_id %cd_Gui%,, CountDown
  GuiControl,, cd_Button, &START
  Return
}
cd_Duration := GetDurationInSec()
if cd_Duration <= 0
{
  MsgBox 16, Error, Invalid time.
  Return
}
WinSetTitle ahk_id %cd_Gui%,, %cd_Duration% ; Refresh tray button text
GuiControl,, cd_Button, &STOP
SetTimer CountDownTimer, 1000
Return

CountDownTimer:
cd_Duration--
WinSetTitle ahk_id %cd_Gui%,, %cd_Duration% ; Refresh tray button text
if cd_Duration = 0
    StopCountDown()
    Return

TimeEdited: ; Update duration text
GuiControl,, cd_DurationText, % "Duration: " GetDurationInSec() " seconds"
Return


GetDurationInSec()
{
local Hours, Minutes, Seconds
GuiControlGet Hours,, cd_HoursEdit
if ! Hours
Hours := 0
GuiControlGet Minutes,, cd_MinutesEdit
if ! Minutes
Minutes := 0
GuiControlGet Seconds,, cd_SecondsEdit
if ! Seconds
Seconds := 0
Return Hours * 3600 + Minutes * 60 + Seconds
}

StopCountDown()
{
  WinActivate, 0
  ControlClick, Button1, 0, , , , , ,
  sleep, 100
  WinActivate, CountDown
  ControlClick, Button14, CountDown, , , , , ,
}

;new
Label:
Gui, Submit, NoHide ;this command submits the guis' datas' state
WinActivate, Main
If Opt1 = 1
  Click, 620, 116

If Opt2 = 1
  Click, 620, 143

If Opt3 = 1
  Click, 620, 165

If Opt4 = 1
  Click, 620, 197

If Opt5 = 1
  Click, 620, 225

If Opt6 = 1
  Click, 620, 254

If Opt7 = 1
  Click, 620, 279

If Opt8 = 1
  Click, 620, 306

If Opt9 = 1
  Click, 620, 335

If  Opt10 = 1
  Click, 620, 360

If  Opt11 = 1
  Click, 620, 390

If  Opt12 = 1
  Click, 620, 414

Return

GuiClose:
ExitApp

; Start/Stop button
;Win Title: CountDown   ;changes to #
;Class: ahk_class AutoHotKeyGUI
;Process: ahk_exe AutoHotKey.exe
;ClassNN: Button1

; Submit button
;Win Title: CountDown   ;changes to #
;Class: ahk_class AutoHotKeyGUI
;Process: ahk_exe AutoHotKey.exe
;ClassNN: Button14

;Tkinter
;Win Title: Main
;Class:  TkTopLevel
;Process: Python.exe
;ClassNN: Button14 - 3