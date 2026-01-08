param(
  [ValidateSet("prep","stamp","open","all","help")]
  [string]$Cmd = "all"
)

# Make output behave (fixes weird â€” stuff)
$OutputEncoding = [Console]::OutputEncoding = [System.Text.UTF8Encoding]::new()
$env:PYTHONIOENCODING = "utf-8"

$root = Split-Path -Parent (Split-Path -Parent $MyInvocation.MyCommand.Path)
Set-Location $root

function Run-Py([string]$path) {
  Write-Host ""
  Write-Host ">>> python $path" -ForegroundColor Cyan
  python $path
  if ($LASTEXITCODE -ne 0) {
    throw "Command failed: python $path (exit $LASTEXITCODE)"
  }
}

function Get-LatestSessionLog {
  $logs = Join-Path $root "logs"
  if (!(Test-Path $logs)) { return $null }

  Get-ChildItem $logs -Filter "session_*.md" -File |
    Where-Object { $_.Name -match '^session_\d{4}-\d{2}-\d{2}_\d{4}\.md$' } |
    Sort-Object LastWriteTime -Descending |
    Select-Object -First 1
}

function Open-IfExists([string]$path) {
  if (Test-Path $path) {
    Start-Process $path | Out-Null
  }
}

switch ($Cmd) {
  "help" {
    Write-Host @"
Skyrim Vault helper

Usage:
  powershell -ExecutionPolicy Bypass -File scripts\skyrim.ps1 prep
  powershell -ExecutionPolicy Bypass -File scripts\skyrim.ps1 stamp
  powershell -ExecutionPolicy Bypass -File scripts\skyrim.ps1 open
  powershell -ExecutionPolicy Bypass -File scripts\skyrim.ps1 all
"@
    exit 0
  }

  "prep" {
    Run-Py "scripts/on_track.py"
    Run-Py "scripts/build_context.py"
    Run-Py "scripts/dragonbreak_cue.py"
    exit 0
  }

  "stamp" {
    Run-Py "scripts/session_stamp.py"
    $latest = Get-LatestSessionLog
    if ($null -ne $latest) {
      Write-Host ""
      Write-Host "Opening latest log: $($latest.FullName)" -ForegroundColor Green
      Start-Process $latest.FullName | Out-Null
    }
    exit 0
  }

  "open" {
    $act = Join-Path $root "modules\acts\ACT_01_BATTLE_OF_WHITERUN.md"
    Open-IfExists $act

    $latest = Get-LatestSessionLog
    if ($null -ne $latest) {
      Open-IfExists $latest.FullName
    }
    exit 0
  }

  "all" {
    Run-Py "scripts/on_track.py"
    Run-Py "scripts/build_context.py"
    Run-Py "scripts/dragonbreak_cue.py"
    Run-Py "scripts/session_stamp.py"

    $act = Join-Path $root "modules\acts\ACT_01_BATTLE_OF_WHITERUN.md"
    Open-IfExists $act

    $latest = Get-LatestSessionLog
    if ($null -ne $latest) {
      Open-IfExists $latest.FullName
    }
    exit 0
  }
}
