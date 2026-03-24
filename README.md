# Python Port Scanner

Un scanner de porturi rapid, scris în Python, care utilizează multithreading pentru performanță și include detectarea sistemului de operare bazată pe TTL.

## Caracteristici:

* **Multithreading:** Utilizează `ThreadPoolExecutor` pentru scanare rapidă.
* **OS Detection:** Identifică sistemul de operare (Windows/Linux/Cisco) prin analiza TTL-ului ICMP.
* **Service Detection:** Identifică serviciile comune bazate pe numărul portului.
* **Banner Grabbing:** Încearcă să extragă banner-ul serviciului pentru porturile deschise.
* **Suport DNS:** Poți introduce IP-uri sau nume de domenii (ex: google.com).

## Instalare:

1. Clonează repository-ul:

```
git clone https://github.com/Paius-George/Python-Port-Scanner
cd Python-Port-Scanner/
```

2. Instalează dependențele:

```
pip install -r requirements.txt
```

## Utilizare
Rulează scriptul și urmează instrucțiunile din terminal:

```
python portscanner.py
```

## Output:

<img width="913" height="1042" alt="image" src="https://github.com/user-attachments/assets/14e0d189-8642-4307-9f1d-4dccb3958e77" />


---
> Acest tool este creat strict în scopuri educaționale. Utilizatorul este singurul responsabil pentru modul în care alege să îl folosească. Scanarea rețelelor fără permisiune prealabilă poate fi ilegală.
