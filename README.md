
# BlockWeb - Little System to Block HTTP Requests

There are some people who have difficulty controlling their emotions, such as playing games.

Games end up taking up a lot of people's time, time that could be invested in studying, physical activity, and so on.

This tool, BlockWeb, solves your problem when you want to avoid websites to maintain concentration, or for parents who want to control access to games. Initially, it is a tool that adds websites through HTTP requests. This work too for social media.


## Application Features

Website Blocking: You can block websites directly in the hosts file, redirecting them to the address 127.0.0.1.

Graphical Interface: Initially, a simple and intuitive interface was developed using Tkinter.

Add and remove websites with ease, with just one click, in addition to blocking and unblocking


## Technologies Used

Python 3.x

Tkinter

PyInstaller

Inno Setup


## How to Install 


Check your version before using this command:

```
python --version
```

Next step is using the pywin32. He provides the Python interface for interacting with the Windows API, including the services-related part (which you use to create Windows services). Follow the command:

```
pip install pywin32
```


And for the last, install tk. 

\
\
**Note**: 
Tkinter usually comes with Python, but if you need to install it manually (on some distributions), use:
```
pip install tk
```

## Development Environment

If you want understand how to generate the file into a Windows executable, follow the steps below:

Download Here: [Inno Setup](https://jrsoftware.org/isdl.php)  --- **Choose the US language**
\
\

After, you can put this script and iso, and run:


````
[Setup]
AppName=Bloqueador de Sites
AppVersion=1.0
DefaultDirName={pf}\BloqueadorDeSites
OutputDir=.\output
OutputBaseFilename=setup_bloqueador
Compression=lzma
SolidCompression=yes

[Files]
; Caminho do arquivo .exe gerado pelo PyInstaller
Source: "dist\interface.exe"; DestDir: "{app}"; Flags: ignoreversion

[Icons]
; Criar um atalho na área de trabalho
Name: "{userdesktop}\Bloqueador de Sites"; Filename: "{app}\interface.exe"

[Run]
; Definir a execução do aplicativo após a instalação
Filename: "{app}\interface.exe"; Description: "Iniciar Bloqueador de Sites"; Flags: nowait postinstall skipifsilent
````

Below is the explanation for each command:

| Seção      | Descrição                                                                                        |
|------------|--------------------------------------------------------------------------------------------------|
| **[Setup]** | Definindo o nome e versão do aplicativo, além do diretório de instalação e outras opções.         |
| `AppName`  | Nome do aplicativo, como ele aparecerá durante a instalação. Ex: `Bloqueador de Sites`.             |
| `AppVersion` | Versão do aplicativo. Ex: `1.0`.                                                                  |
| `DefaultDirName` | Caminho padrão para a instalação. Ex: `{pf}\BloqueadorDeSites`.                                 |
| `OutputDir` | Diretório onde o instalador gerado será salvo. Ex: `.\output`.                                    |
| `OutputBaseFilename` | Nome base do arquivo do instalador gerado. Ex: `setup_bloqueador`.                           |
| `Compression` | Tipo de compressão do instalador. Ex: `lzma`.                                                     |
| `SolidCompression` | Se a compressão será "sólida". Ex: `yes`.                                                       |
| **[Files]**   | Seção que define os arquivos a serem incluídos no instalador.                                      |
| `Source`    | Caminho para o arquivo `.exe` gerado pelo PyInstaller. Ex: `dist\interface.exe`.                  |
| `DestDir`   | Destino onde o arquivo será instalado. Ex: `{app}`.                                               |
| `Flags`     | Atributos para o arquivo, como `ignoreversion` (ignorar versão ao instalar).                     |
| **[Icons]**  | Seção que define os ícones do instalador, como atalhos na área de trabalho.                       |
| `Name`      | Nome do atalho que será criado. Ex: `{userdesktop}\Bloqueador de Sites`.                          |
| `Filename`  | Caminho para o arquivo que será vinculado ao atalho. Ex: `{app}\interface.exe`.                   |
| **[Run]**    | Seção que define o que o instalador fará após a instalação, como executar o aplicativo.           |
| `Filename`  | Caminho para o arquivo executável que será executado após a instalação. Ex: `{app}\interface.exe`.|
| `Description` | Descrição do que será feito. Ex: `Iniciar Bloqueador de Sites`.                                   |
| `Flags`     | Definição de comportamentos adicionais, como `nowait postinstall skipifsilent`.                   |

\
After configuring the script, click "Compile" in Inno Setup.









