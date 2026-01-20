# Python Organize by Extensions

Esse projeto tem como objetivo organizar os arquivos presentes em um diretório (selecionado pelo usuário) a partir da sua extensão, os salvando em um diretório também selecionado.

## Requisitos

- Python 3.4 ou superior

## Para rodar o projeto

Certifique-se de ter python instalado em sua máquina

Clone o projeto e acesse sua pasta
```bash
  git clone https://github.com/ViniciusCassemira/py-file-organizer.git
  cd py-file-organizer
```

Execute o script
```bash
  python app.py
```

## Exemplo de funcionamento

Para o nosso exemplo, imagine que exista um diretório localizado em `/home/vinicius/study`, e que dentro desse diretório existem outros 3 arquivos: `php.txt`, `photo.png` e `file.txt`. O objetivo é separar eles com base em suas extensões (`.txt` e `.png`).

Ao rodar a aplicação, o programa pede 2 caminhos: `Folder origin` e `Folder destination`. O primeiro será o caminho de onde os arquivos se encontram, o segundo é o local aonde as divisões com base na extensão serão feitas.

Continuando com o nosso exemplo, vamos imaginar que o nosso `Folder destination` receba o seguinte caminho: _/home/vinicius/new_study_. O programa vai interagir com todos os arquivos presentes no `Folder origin`, deixando sua organização assim:
```
/home/vinicius/new_study
  png/
    photo.png
  txt/
    file.txt
    php.txt
```

**Observações importantes:**
1) Os arquivos são movidos para esse novo caminho, **não é realizada** nenhuma cópia deles durante esse processo, sendo de fato transferidos.
2) Atualmente, essa organização não é recursiva. Caso o seu `Folder origin` possua um subdiretório, esse será movido para o seu `Folder destination`, esse bug logo será corrigido.
3) Confira o arquivo `logs.txt` após rodar o script. Ele armazena informações como arquivos movidos e possíveis erros.

## Referências utilizadas

- [w3schools: Python Datetime](https://www.w3schools.com/python/python_datetime.asp)
- [w3schools: Try Python (sandbox to datetime)](https://www.w3schools.com/python/trypython.asp?filename=demo_datetime_strftime_x2)
- [geeksforgeeks: pathlib module in python](https://www.geeksforgeeks.org/python/pathlib-module-in-python/)