## Start GuadiantTales Apps powered by BlueStack
# Author : MedericCossu

$loop = "True"
$adbDeviceAddress = "127.0.0.1:$(Get-NetTCPConnection -OwningProcess $(get-process -Name "HD-Player" |select -expand id -First 1) -LocalAddress 127.0.0.1 | select -expand LocalPort -First 1)"

function Connect-adb{
    $adbDeviceAddress = "127.0.0.1:$(Get-NetTCPConnection -OwningProcess $(get-process -Name "HD-Player" |select -expand id -First 1) -LocalAddress 127.0.0.1 | select -expand LocalPort -First 1)"
    cd "C:\Program Files\BlueStacks_nxt"
    ./HD-Adb.exe disconnect
    ./HD-Adb.exe connect $adbDeviceAddress
    Start-Sleep -Seconds 1
}

function Start-BlueStacks{
    Start "C:\Program Files\BlueStacks_nxt\HD-Player.exe" -ArgumentList '--instance Nougat32_1 --cmd launchApp --package "com.kakaogames.gdts"'
    Start-Sleep -Seconds 30
}

while($loop -eq "True")
{
    Start-BlueStacks
    Connect-adb
    $appVsize = .\HD-Adb.exe -s $adbDeviceAddress shell ps $(.\HD-Adb.exe -s $adbDeviceAddress shell pidof -s com.kakaogames.gdts) | ForEach-Object{($_ -split "\s+")[3]} | select -Last 1

    If($appVsize -lt "2500000")
    {
        Stop-Process -Name "HD-Player"
        Start-BlueStacks
        Connect-adb
    }
    else
    {
        $loop = "False"
    }
    exit
}
Start-Sleep -Seconds 10