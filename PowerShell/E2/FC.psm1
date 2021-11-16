# Check profile status
function Check-ProfilleStat{
    param([Parameter(Mandatory)] [ValidateSet("Public","Private")] [string] $profile)
    $status = Get-NetFirewallProfile -name $profile 
    Write-Host "`nProfile:" $profile

    if($status.Enabled){
        Write-Host "Status: Actived"
    }else{
      Write-Host "Status: Disabled"  
    }
}

# Change profile status
function Change-ProfileStat{
    param([Parameter(Mandatory)] [ValidateSet("Public","Private")] [string] $profile)
    $status = Get-NetFirewallProfile -Name $profile
    Write-Host "`nProfile:" $profile

    if($status.Enabled){
        Write-Host 'Status: Actived'
        $opc = Read-Host -Prompt "`nDo you want to disable it? [Y] Yes [N] No"

        if($opc -eq "Y"){
            Set-NetFirewallProfile -Name $profile -Enabled False
        }
    }else{
        Write-Host "Status: Disabled"
        $opc = Read-Host -Prompt "`nDo you want to activate it? [Y] Yes [N] No"

        if($opc -eq "Y"){
            Set-NetFirewallProfile -Name $profile -Enabled True
        }
    }
    Check-ProfilleStat -profile $profile
}

# Check Network profile
function Check-NetProfile{
    $netProfile = Get-NetConnectionProfile
    Write-Host "Network: " $netProfile.Name
    Write-Host "Network Profile: " $netProfile.NetworkCategory
}

# Change NetworkProfile 
function Change-Netprofile{
    $netProfile = Get-NetConnectionProfile
    
    if($netProfile.NetworkCategory -eq "Public"){
        Write-Host "Current profile --> Public"
        $opc = Read-Host -Prompt "`nDo you want to change to private?  [Y] Yes [N] No"

        if($opc -eq "Y"){
            Set-NetConnectionProfile -Name $netProfile.Name -NetworkCategory Private
            Write-Host "Profile has been changed.."
        }
    }else{
        Write-Host "Current profile --> Private"
        $opc = Read-Host -Prompt "`nDo you want to change to public?  [Y] Yes [N] No"

        if($opc -eq "Y"){
            Set-NetConnectionProfile -Name $netProfile.Name -NetworkCategory Public
            Write-Host "Profile has been changed.."
        }
    }
    Check-NetProfile
}


# Check Blocking rules
function Check-BlockingRules{
    if(Get-NetFirewallRule -Action Block -Enabled True -ErrorAction SilentlyContinue){
        Get-NetFirewallRule -Action Block -Enabled True
    }else{
        Write-Host "There is no rules yet"
    }
}


# Add Blocking Rules
function Add-BlockingRules{
    $port = Read-Host -Prompt "Which port do you want to block? "
    New-NetFirewallRule -DisplayName "Port-$port" -Profile "Public" -Direction Inbound -Action Block -Protocol TCP -LocalPort $port
}

# Deleting Blocking rules
function Del-BlockingRules{
    $rules = Get-NetFirewallRule -Action Block -Enabled True
    Write-Host 'Current Rules'

    foreach($rule in $rules){
        Write-Host "Rule :" $rule.DisplayName
        Write-Host 'Profile :' $rule.Profile
        Write-Host 'ID :' $rule.Name

        $opc = Read-Host -Prompt "`nDo you want to delete this rule?  [Y] Yes [N] No"
        
        if($opc){
            Remove-NetFirewallRule -ID $rule.name
            break
        }
    }
}