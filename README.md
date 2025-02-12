# EPUB 轉換器

臺北市立建國高級中學 圖書館潘威歷主任

本專案提供一個簡單的 Windows GUI 應用程式，可將 EPUB 文件轉換為 TXT、HTML 和 PDF 格式。

## 安裝與前置作業

### 1. 安裝 Python

請確保已安裝 Python 3.8 以上版本，可從 [Python 官方網站](https://www.python.org/downloads/) 下載。

### 2. 安裝必要套件

使用以下指令安裝所需的 Python 套件：

```sh
pip install ebooklib beautifulsoup4 pdfkit tkinter
```

### 3. 安裝 wkhtmltopdf

由於 PDF 轉換使用 `pdfkit`，請下載並安裝 `wkhtmltopdf`。

- 下載網址：[wkhtmltopdf 官方網站](https://wkhtmltopdf.org/downloads.html)
- 安裝後，請確認 `wkhtmltopdf.exe` 存在於 `C:/Program Files/wkhtmltopdf/bin/`

## 使用方式

1. 執行 `epub_converter.py`。
2. 選擇 EPUB 檔案。
3. 選擇輸出資料夾。
4. 按下「開始轉換」，程式會自動產生對應的 TXT、HTML、PDF 檔案。

所有轉換後的檔案將會存放於與 EPUB 檔案名稱相同的資料夾中，方便管理。

## 注意事項

- 確保 EPUB 檔案內容無加密保護，否則可能無法正確解析。
- 若發生亂碼問題，請確認 EPUB 檔案的編碼格式。
- 確保 `wkhtmltopdf` 正確安裝，否則 PDF 轉換功能無法運作。

