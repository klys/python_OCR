== Como usar el OCR

- Deben tener Python3 instalado
- Instalar pytesseract https://github.com/tesseract-ocr/tesseract
- pip install pytesseract

el pytesseract ademas de tener packete en pip tiene un instalador aparte que se instala manualmente y se asigna su ubicacion exacta en

```
pytesseract.pytesseract.tesseract_cmd
```

Pagina oficial de pytesseract: https://pypi.org/project/pytesseract/

== Como ajustar el tamano de la pantalla ==

en la linea 7 se encuentra las dos posiciones x,y del primer punto y del segundo punto que conforman el cuadrado que se transformara en imagen que luego se transforama a su vez en texto

```
cap = ImageGrab.grab(bbox =(530, 200, 1330, 1000))
```

x | y
530, 200 es el primer punto

1330, 1000 es el segundo punto
