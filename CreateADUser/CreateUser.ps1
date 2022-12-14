Add-Type -AssemblyName System.Windows.Forms

$OUPath = 'OU=Users,OU=OWL,DC=LARSONUS,DC=COM'
$UserFirstName = $args[1]
$UserLastName = $args[2]
$DisplayName = $UserFirstName + " " + $UserLastName
$SAM = $args[3] #account name
$UPN = $args[4] #unique identifier
$Password = $args[5]
$Email = $args[6]
$Location = $args[7]
$OU = "OU=" + $Location +"," + $OUPath

Write-Host "first" $UserFirstName
Write-Host "last" $UserLastName
Write-Host "display" $DisplayName
Write-Host "SAM" $SAM
Write-Host "UPN" $UPN
Write-Host "pass" $Password
Write-Host "email" $Email
Write-Host "location" $Location

New-ADUser -Name "$DisplayName" -DisplayName "$DisplayName" -SamAccountName $SAM -UserPrincipalName $UPN -GivenName "$UserFirstName" -Surname "$UserLastName" -AccountPassword(ConvertTo-SecureString $Password -AsPlainText -Force) -ChangePasswordAtLogon $False -PasswordNeverExpires $True -EmailAddress "$Email" -Path "$OU" -Enabled $true