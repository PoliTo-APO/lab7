# Laboratorio 7
Si scriva un programma che sia in grado di 
rappresentare un servizio di streaming per film e serie TV.

I moduli e le classi vanno sviluppati nel package *streaming*.
Non spostare o rinominare moduli e classi esistenti e non modificare le signature dei metodi.

In *main.py* viene fornito del semplice codice, da voi modificabile, che testa le funzionalità base.
Esso mostra esempi di uso dei metodi principali ed esempi dei controlli richiesti.


## R1: Film e Serie TV
La classe astratta *MediaContent* rappresenta un contenuto multimediale generico.

Il costruttore accetta come parametri
il titolo del contenuto e l'anno di uscita.
Queste informazioni sono accessibili tramite i getters
```get_title(self) -> str``` e ```get_year(self) -> int```.

Il metodo astratto ```get_content_type(self) -> str```
restituisce una stringa che indica il tipo di contenuto.

Il metodo ``` __repr__(self) -> str```
restituisce la rappresentazione in stringa del contenuto multimediale.

La classe *StreamingService* contiene dei metodi
per aggiungere e ottenere contenuti multimediali.

Il metodo
```add_movie(self, title: str, year: int, director: str, duration: int) -> None```
permette di aggiungere un film,
specificando titolo, anno di uscita, nome del regista e durata in minuti.

Il metodo
```add_tv_show(self, title: str, year:int, num_seasons: int, num_episodes: int) -> None```
permette di aggiungere una serie tv,
specificando titolo, anno di uscita, numero di stagioni e numero di episodi.

Il metodo
```get_media_content(self, title: str) -> MediaContent```
restituisce il contenuto multimediale il cui titolo è passato come parametro.

Per un film, il metodo  ```get_content_type``` deve restituire la stringa *"movie"*,
mentre per una serie TV la stringa restituita deve essere *"tv show"*

La rappresentazione in stringa di un film deve contenere, 
il titolo, l'anno di uscita, il nome del regista e la durata in minuti
(in quest'ordine e separati da virgole **SENZA SPAZI AGGIUNTIVI**).
Esempio: *"Pulp Fiction,1994,Quentin Tarantino,154"*

La rappresentazione in stringa di una serie tv deve contenere,
il titolo, l'anno di uscita, il numero di stagioni e il numero di episodi
(in quest'ordine e separati da virgole **SENZA SPAZI AGGIUNTIVI**).
Esempio: *"Twin Peaks,1990,3,48"*


## R2: Utenti
Il metodo 
```add_user(self, name: str, age:int) -> None```
della classe *StreamingService* 
accetta come parametri il nome e l'età di un utente
che si registra al servizio di streaming.

Il metodo
```watch(self, user_name: str, title: str) -> None```,
accetta il nome di un utente e il titolo di un contenuto,
e registra la presa visone del contenuto da parte dell'utente.

Il metodo
```get_watched_by_user(self, user_name: str, min_year: Optional[int] = None) -> List[MediaContent]```, 
restituisce la lista di contenuti guardati dall'utente
il cui nome è fornito come primo parametro.
Il parametro opzionale *min_year*, se fornito,
permette di specificare un anno di uscita.
I contenuti restituiti dal metodo dovranno essere
più recenti dell'anno di uscita specificato.
Se non sono presenti contenuti guardati dall'utente
il metodo deve restituire una lista vuota.

Il metodo
```get_watchers_of_content(self, title: str) -> List[str]```
accetta come unico parametro il titolo di un contenuto,
e restituisce la lista dei nomi degli utenti che lo hanno guardato.
Se non sono presenti utenti che hanno guardato il contenuto
il metodo deve restituire una lista vuota.


## R3: Valutazioni
Il metodo ```add_rating(self, user_name: str, title: str, rating: int) -> None```
accetta come parametri il nome di un utente,
il titolo di un contenuto e la valutazione dell'utente per quel contenuto.

Il metodo ```get_avg_content_rating(self, title: str) -> float```
restituisce la media delle valutazioni
ricevute da un contenuto, il cui titolo è fornito come parametro.
Per i film, se le valutazioni sono più di due, non si considera quella più alta e quella più bassa.
Per le serie TV si devono considerare, in aggiunta a quelle reali,
10 valutazioni fittizie con punteggio pari a cinque.

Il metodo  ```get_avg_user_rating(self, user_name: str) -> float```
restituisce la media delle valutazioni
espresse da un utente, il cui nome è fornito come parametro.


## R4: Suggerimenti
Il metodo  ```get_recommendations(self, user_name: str) -> List[str]```
restituisce un lista di titoli di contenuti
da suggerire all'utente il cui nome viene passato come parametro.

La lista deve contenere i titoli di tutti i contenuti guardati da utenti
che hanno almeno un contenuto guardato in comune con l'utente
per cui viene richiesto il suggerimento.

La lista non deve contenere titoli già guardati dall'utente, e non deve contenere duplicati.
Se non sono presenti contenuti da suggerire la lista restituita deve essere vuota.


## R5: Maratona
Data una saga cinematografica e televisiva (ad es. l'universo *Marvel*),
e un contenuto che si vuole vedere della saga,
si vole sapere quali altri film della saga è necessario aver visto e in che ordine guardarli.

Il metodo ```set_previous_content(self, title: str, previous_title: str) -> None```,
accetta come parametri i titoli di due contenuti,
e impone in vincolo che il per vedere il primo titolo sia necessario aver visto il secondo.

Una volta impostati più vincoli, il metodo ```get_watch_list(self, title: str) -> list[str]```,
restituisce una lista di titoli di contenuti da guardare
prima di vedere il contenuto il cui titolo è fornito come parametro, in un ordine che rispetta i vincoli.

**IMPORTANTE** i vincoli sono settati di modo che ogni contenuto sia vincolante al più per un altro contenuto.
Facendo quest'assunzione, il grafo **DIRETTO** delle dipendenze è un **ALBERO**
che ha come radice l'ultimo contenuto della saga.









