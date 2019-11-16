; Script generated by the Inno Setup Script Wizard.
; SEE THE DOCUMENTATION FOR DETAILS ON CREATING INNO SETUP SCRIPT FILES!

#define MyAppName "SB Calculator"
#define MyAppVersion "1.0"
#define MyAppPublisher "Subho Basak"
#define MyAppURL "subhobasak50@gmail.com"
#define MyAppExeName "SB_calculator.exe"

[Setup]
; NOTE: The value of AppId uniquely identifies this application. Do not use the same AppId value in installers for other applications.
; (To generate a new GUID, click Tools | Generate GUID inside the IDE.)
AppId={{18295066-3686-4ED4-A858-3773E106287F}
AppName={#MyAppName}
AppVersion={#MyAppVersion}
;AppVerName={#MyAppName} {#MyAppVersion}
AppPublisher={#MyAppPublisher}
AppPublisherURL={#MyAppURL}
AppSupportURL={#MyAppURL}
AppUpdatesURL={#MyAppURL}
DefaultDirName={autopf}\{#MyAppName}
DisableProgramGroupPage=yes
; Uncomment the following line to run in non administrative install mode (install for current user only.)
;PrivilegesRequired=lowest
OutputBaseFilename=mysetup
Compression=lzma
SolidCompression=yes
WizardStyle=modern

[Languages]
Name: "english"; MessagesFile: "compiler:Default.isl"

[Tasks]
Name: "desktopicon"; Description: "{cm:CreateDesktopIcon}"; GroupDescription: "{cm:AdditionalIcons}"; Flags: unchecked

[Files]
Source: "D:\my_github\Small_projects\Calculator\dist\SB_calculator\SB_calculator.exe"; DestDir: "{app}"; Flags: ignoreversion
Source: "D:\my_github\Small_projects\Calculator\dist\SB_calculator\_bz2.pyd"; DestDir: "{app}"; Flags: ignoreversion
Source: "D:\my_github\Small_projects\Calculator\dist\SB_calculator\_hashlib.pyd"; DestDir: "{app}"; Flags: ignoreversion
Source: "D:\my_github\Small_projects\Calculator\dist\SB_calculator\_lzma.pyd"; DestDir: "{app}"; Flags: ignoreversion
Source: "D:\my_github\Small_projects\Calculator\dist\SB_calculator\_socket.pyd"; DestDir: "{app}"; Flags: ignoreversion
Source: "D:\my_github\Small_projects\Calculator\dist\SB_calculator\_ssl.pyd"; DestDir: "{app}"; Flags: ignoreversion
Source: "D:\my_github\Small_projects\Calculator\dist\SB_calculator\_tkinter.pyd"; DestDir: "{app}"; Flags: ignoreversion
Source: "D:\my_github\Small_projects\Calculator\dist\SB_calculator\base_library.zip"; DestDir: "{app}"; Flags: ignoreversion
Source: "D:\my_github\Small_projects\Calculator\dist\SB_calculator\icon.ico"; DestDir: "{app}"; Flags: ignoreversion
Source: "D:\my_github\Small_projects\Calculator\dist\SB_calculator\libcrypto-1_1.dll"; DestDir: "{app}"; Flags: ignoreversion
Source: "D:\my_github\Small_projects\Calculator\dist\SB_calculator\libssl-1_1.dll"; DestDir: "{app}"; Flags: ignoreversion
Source: "D:\my_github\Small_projects\Calculator\dist\SB_calculator\pyexpat.pyd"; DestDir: "{app}"; Flags: ignoreversion
Source: "D:\my_github\Small_projects\Calculator\dist\SB_calculator\python37.dll"; DestDir: "{app}"; Flags: ignoreversion
Source: "D:\my_github\Small_projects\Calculator\dist\SB_calculator\SB_calculator.exe.manifest"; DestDir: "{app}"; Flags: ignoreversion
Source: "D:\my_github\Small_projects\Calculator\dist\SB_calculator\select.pyd"; DestDir: "{app}"; Flags: ignoreversion
Source: "D:\my_github\Small_projects\Calculator\dist\SB_calculator\tcl86t.dll"; DestDir: "{app}"; Flags: ignoreversion
Source: "D:\my_github\Small_projects\Calculator\dist\SB_calculator\tk86t.dll"; DestDir: "{app}"; Flags: ignoreversion
Source: "D:\my_github\Small_projects\Calculator\dist\SB_calculator\unicodedata.pyd"; DestDir: "{app}"; Flags: ignoreversion
Source: "D:\my_github\Small_projects\Calculator\dist\SB_calculator\VCRUNTIME140.dll"; DestDir: "{app}"; Flags: ignoreversion
Source: "D:\my_github\Small_projects\Calculator\dist\SB_calculator\tcl\*"; DestDir: "{app}\tcl"; Flags: ignoreversion recursesubdirs createallsubdirs
Source: "D:\my_github\Small_projects\Calculator\dist\SB_calculator\tk\*"; DestDir: "{app}\tk"; Flags: ignoreversion recursesubdirs createallsubdirs
; NOTE: Don't use "Flags: ignoreversion" on any shared system files

[Icons]
Name: "{autoprograms}\{#MyAppName}"; Filename: "{app}\{#MyAppExeName}"
Name: "{autodesktop}\{#MyAppName}"; Filename: "{app}\{#MyAppExeName}"; Tasks: desktopicon

[Run]
Filename: "{app}\{#MyAppExeName}"; Description: "{cm:LaunchProgram,{#StringChange(MyAppName, '&', '&&')}}"; Flags: nowait postinstall skipifsilent
