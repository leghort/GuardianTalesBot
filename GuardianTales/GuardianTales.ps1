## Start GuadiantTales Apps powered by BlueStack
# Author : MedericCossu

$loop = "True"

function Connect-adb{
    $adbDeviceAddress = "127.0.0.1:$(Get-NetTCPConnection -OwningProcess $(get-process -Name "HD-Player" |select -expand id -First 1) -LocalAddress 127.0.0.1 | select -expand LocalPort -First 1)"
    cd "C:\Program Files\BlueStacks_nxt"
    ./HD-Adb.exe disconnect
    ./HD-Adb.exe connect $adbDeviceAddress
}

function Start-BlueStacks{
    Start "C:\Program Files\BlueStacks_nxt\HD-Player.exe" -ArgumentList '--instance Nougat32_1 --cmd launchApp --package "com.kakaogames.gdts"'
    Start-Sleep -Seconds 30
}

while($loop -eq "True")
{
    Start-BlueStacks
    $adbDeviceAddress = "127.0.0.1:$(Get-NetTCPConnection -OwningProcess $(get-process -Name "HD-Player" |select -expand id -First 1) -LocalAddress 127.0.0.1 | select -expand LocalPort -First 1)"
    Connect-adb
    $appVsize = .\HD-Adb.exe -s $adbDeviceAddress shell ps $(.\HD-Adb.exe -s $adbDeviceAddress shell pidof -s com.kakaogames.gdts) | ForEach-Object{($_ -split "\s+")[3]} | select -Last 1

    If($appVsize -le "2500000")
    {
        echo "if"
        Stop-Process -Name "HD-Player"
        Start-BlueStacks
        Connect-adb
        Start-Sleep -Seconds 1
        $appVsize = .\HD-Adb.exe -s $adbDeviceAddress shell ps $(.\HD-Adb.exe -s $adbDeviceAddress shell pidof -s com.kakaogames.gdts) | ForEach-Object{($_ -split "\s+")[3]} | select -Last 1
    }
    elseif($appVsize -ge "2500000"){
        echo "elseif"
        $loop = "False"
    }
    else
    {
        echo "else"
        $appVsize = .\HD-Adb.exe -s $adbDeviceAddress shell ps $(.\HD-Adb.exe -s $adbDeviceAddress shell pidof -s com.kakaogames.gdts) | ForEach-Object{($_ -split "\s+")[3]} | select -Last 1
    }
}
exit