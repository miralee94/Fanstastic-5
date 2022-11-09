[SERVERHALL]


### [FILES] ###

[server]        <multiconn_server.py>
[data-client]   <multiconn_data_client.py>
[user-client]   <multiconn_user.py>
[data-files]    <serverhall.py>
[pytest-tests]  <testers.py>


## Information ##

Serverhallen är ett  python projekt där det finns 2 klienter som pratar med servern.

>>> ["multiconn_data_client.py"]
Data-clienten skickar data from filen "serverhall.py" till Servern


>>> ["multiconn_user_client.py"]
Användar-clienten, skickar kommandon till servern, som i sin tur utför kod
som i det här fallet, är att skicka data från Data-klienten, till servern, som sedan skickar koden till Användar-clienten.
så det blir <Data-client> --> <Server> --> <Användarklient>


["Serverhall.py"] är en fil där mycket objekt-orienterad kod är samlad och även Data som skickas till och från server.

["testers.py"] är en fil där jag testar mina funktioner från koden och ser till att dom utför det som ska göra igenom att använda
<pytest> för att utföra dessa tester.


[----------------------------------------------------------------------------------------------]


## [PROGRAM] ##

>>> *HOW TO*

Börja med att start upp programmet från ["multiconn_server.py"] och sedan starta ut klienterna.

skicka datan från ["multiconn_data_client.py"] till servern, genom att följa instruktionerna.

Datan ska nu ha fångat upp senaste uppgifterna från servern.

Kör nu ["Multiconn_user_client.py"] och följ instruktionerna för att skicka datan från servern.


[----------------------------------------------------------------------------------------------]


## [FELHANTERING] ##

# Information ##

om man försöka fånga datan innan den har skickats från Data-klienten, så låser sig Användar-klienten (ej hanterad)
när man använder <"!DISCONNECT"> så säger den "string out of index". (ej hanterad)
Skickar man datan flera gången från Data klienten, så fångar Användar klienten all den data. och printar det om du hämtar datan. (Ej hanterad)






