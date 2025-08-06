# FP-subrip

a programe used to rip subtitles from fpt play

## Dependencies
- [Request](https://pypi.org/project/requests/)
## Installation
Clone this repository
```bash
git https://github.com/nhutloveillya/FP-subrip.git
cd FP-subrip
```
Using pip to install pkg
```bash
pip install ./
```
<!-- Auto generated -->
## Usage
```
fpsub [dl,dll] [option]
```
```
positional arguments:
  {dl,dll}       Command to execute: "dl" for download, "dll" for print download links

options:
  -h, --help     show this help message and exit
  -y Y           Year of the upload (YYYY)
  -m M           First month of the upload (1-12)
  -n N           Name of the series
  -yp YP         Year production (YYYY)
  -l L           Language of series (e.g., "JP", "EN")
  -e E           Number of episodes you want to download
  -s S           Directory to save subtitles
  -v, --version  show program's version number and exit
```
- E.g: to download subtitles of a series
  ```
  fpsub dl -y 2025 -m 7 -n Gachiakuta -yp 2025 -l JP -e 4 -s C:\Users\Admin\Downloads
  ```
- E.g: to get download links of subtitles
  ```
  fpsub dll -y 2025 -m 7 -n Gachiakuta -yp 2025 -l JP -e 4
  ```
