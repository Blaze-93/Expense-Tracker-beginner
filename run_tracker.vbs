Set WinScriptHost = CreateObject("WScript.Shell")
' Added --port 8888 at the end
WinScriptHost.Run Chr(34) & "D:\Projects\Expense Tracker\venv\Scripts\python.exe" & Chr(34) & " -m uvicorn app.main:app --port 8888", 0
Set WinScriptHost = Nothing