# README för Projekt i Matematisk Modellering #

Projektets syfte är att skapa ett neuralt nätverk som predikterar studenters tagna poäng en kommande termin


# Anaconda #

```

Ladda ner anaconda och se till att terminalen du använder dig av har rätt path till anaconda-installationsmappen.



```

# Få åtkomst till filerna genom git #

 ```
$ : innebär consol-commando (terminal för mac och anaconda prompt för windows)
1. Se till att du har git installerat på din dator
2. Kopiera länken till repository:t genom att klicka på den gröna knappen "Clone or download"
3. Navigera till önskat installationsställe i terminalen. (använd $ ls och $ cd på linux)
4. Skriv in kommandot $ git clone https://github.com/filipvitez/Matmod_prediktera_examen.git
5. Skriv in kommandot $ cd Matmod_prediktera_examen

 ```


# Få igång jupyter notebook #

```

1. skriv in $ jupyter notebook i terminalen
2. En webbläsare kommer att öppnas med Matmod_prediktera_examen - mappen där du kan välja att navigera in på någon av filerna.
3. För att kunna köra koden kommer diverse paket att behöva laddas ner.
4. Detta görs enklast genom att försöka köra koden, undersöka de felmeddelanden som dyker upp, t.ex. "module not found: tensorflow", för att sedan i terminalen installera de saknade paketen genom terminalkommandot $ conda install "paketets namn"
5. Repetera detta tills alla paket är installerade och kör jupyterkoden cell-vis genom att klicka shift-enter. (alla celler är beroende av varandra så för att köra de understa kräver att man kört samtliga övriga celler minst en gång)



```

# GIT - grejer (för utveckling) #

```
$ : innebär consol-commando (terminal för mac och anaconda prompt för windows)
1. Börja alltid med $ git pull (för att säkerställa att du har den senaste versionen av koden)
2. När du är klar med dina ändringar:
  - $ git add - A
  - $ git commit -m "meddelande som förklarar vad du gjort"
  - $ git push
3. Allmänt:
  - Genom kommandot $ git status levereras en statusuppdatering på hur dina filer lokalt ligger till i förhållande till filerna i git-repot.
```
