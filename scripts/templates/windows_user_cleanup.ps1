# Cleanup inactive users
Get-LocalUser | Where-Object { $_.Enabled -eq $true -and $_.LastLogon -lt (Get-Date).AddDays(-90) } | ForEach-Object {
    Write-Host "Disabling user: $($_.Name)"
    Disable-LocalUser -Name $_.Name
}
