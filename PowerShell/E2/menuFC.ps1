# Edwin Javier Morin Ortiz 
Import-Module FC

# MENU 
Write-Host "-----Welcome-----"

[bool] $m = $true

while($m){
    $menu = Read-Host -Prompt "`nChoose an option`n`t`t[1] Check Profile Status`n`t`t[2] Change Profile Status`n`t`t[3] Check Network Profile`n`t`t[4] Change Network Profile`n`t`t[5] Check Blocking Rules`n`t`t[6] Add Blocking Rules`n`t`t[7] Delete Blocking Rules`n`t`t[8] Exit`n"

    switch($menu){
        1{Check-ProfilleStat}
        2{Change-ProfileStat}
        3{Check-NetProfile}
        4{Change-Netprofile}
        5{Check-BlockingRules}
        6{Add-BlockingRules}
        7{Del-BlockingRules}
        8{
            $m = $false
            Write-Host "`nExiting..."
        }
        default{
            Write-Host "Input an valid option!!`n"
        }
    }
}