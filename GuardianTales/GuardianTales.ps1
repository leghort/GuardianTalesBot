## Start GuadiantTales Apps powered by BlueStack
# Author : MedericCossu

class adb {
    [string]return_adbDeviceAddress() {
        $blueStackId = get-process -Name "HD-Player" |select -expand id -First 1
        $adbDevicesPort = Get-NetTCPConnection -OwningProcess $blueStackId -LocalAddress 127.0.0.1 | select -expand LocalPort -First 1
        $adbDeviceAddress = "127.0.0.1:$adbDevicesPort"
        return $adbDeviceAddress
    }
    [int]return_appVsize() {
        $appVsize = .\HD-Adb.exe -s "127.0.0.1:$(Get-NetTCPConnection -OwningProcess $(get-process -Name "HD-Player" |select -expand id -First 1) -LocalAddress 127.0.0.1 | select -expand LocalPort -First 1)" shell ps (.\HD-Adb.exe -s "127.0.0.1:$(Get-NetTCPConnection -OwningProcess $(get-process -Name "HD-Player" |select -expand id -First 1) -LocalAddress 127.0.0.1 | select -expand LocalPort -First 1)" shell pidof -s com.kakaogames.gdts) | ForEach-Object{($_ -split "\s+")[3]} | select -Last 1
        return $appVsize
    }
}

function Connect-adb{
    $AdbClass = New-Object -TypeName adb
    cd "C:\Program Files\BlueStacks_nxt"
    ./HD-Adb.exe disconnect -out-null
    ./HD-Adb.exe connect $AdbClass.return_adbDeviceAddress()
    Start-Sleep -Seconds 1
}

function Start-BlueStacks{
    if((get-process "HD-Player" -ea SilentlyContinue) -eq $Null){ 
        echo "Start BlueStacks..."
        Start "C:\Program Files\BlueStacks_nxt\HD-Player.exe" -ArgumentList '--instance Nougat32_1 --cmd launchApp --package "com.kakaogames.gdts"'
        Start-Sleep -Seconds 30
    }
    else{
        echo "BlueStack is running"
        Start-Sleep -Seconds 1
    }
}

# Init var
$loop = "True"
$ErrorActionPreference = "SilentlyContinue"
$AdbClass = New-Object -TypeName adb

while($loop -eq "True")
{
    echo ""
    Start-BlueStacks
    Connect-adb
    echo "GuardiansTailesVsize : $($AdbClass.return_appVsize())"
    if($AdbClass.return_appVsize() -le 2500000){ 
        echo "GuardiansTailes fail running"
        Stop-Process -Name "HD-Player"
        Start-Sleep -Seconds 2
    }
    elseif($AdbClass.return_appVsize() -ge 2500000){ 
        echo "Guardians is running"
        $loop = "False"
    }
}
exit