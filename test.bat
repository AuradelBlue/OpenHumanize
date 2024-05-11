@echo off
setlocal enabledelayedexpansion

:: Create an empty JSON object
set "json={"

:: Iterate over specified file types
for %%x in (.py, .md, .bat, .txt, .env) do (
    for %%f in (*%%x) do (
        :: Read the content of the file
        set "content="
        for /f "usebackq delims=" %%i in ("%%f") do (
            set "line=%%i"
            set "line=!line:\=\\!"
            set "line=!line:"=\\"!"
            set "content=!content!!line!\r\n"
        )

        :: Escape double quotes in JSON strings
        set "content=!content:"=\"!"

        :: Append to JSON object
        set "json=!json!\"%%f\": \"!content!\","
    )
)

:: Remove the last comma
set "json=!json:~0,-1!}"

:: Write the JSON object to codebase.json
echo !json! > codebase.json

endlocal
