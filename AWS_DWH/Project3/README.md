Udacity Project 3: Creating AWS Redshift Data Warehouse

Project Overview


The main goal of this project is to create a data warehouse in the cloud on an AWS Redshift cluster for a music streaming service called Sparkify. The initial situation is that Sparkify wants to map both its song database and the data of its users completely in ETL processes in the cloud. The song and user data are stored in Amazon S3 memory, in directories with JSON logs.


My approach to implementation was as follows:
1. I first created a Redshift cluster.
2. Next, I built an ETL pipeline that reads the data from the JSON logs and then fills the database. Data is extracted from the S3 and converted into the fact and dimension tables of the star schema.   
3. For a better processing speed, the order of the data was defined with sort keys.



Mein Vorgehen bei der Umsetzung sah wie folgt aus:
1. Ich habe zunächst ein Redshift Cluster erstellt.
2. Als nächstes habe ich eine ETL-Pipeline aufgebaut, welche die Daten aus den JSON-Logs rausliest und anschließend die Datenbank befüllt. Dabei werden Daten aus dem S3 extrahiert und in die Fakten- und Dimensionstabellen des Sternschemas umgewandelt.   
3. Für eine bessere Verarbeitungsgeschwindigkeit wurde die Reihenfolge der Daten mit Sort-Keys festgelegt.


Setup

Um den ETL-Prozess auszuführen müssen folgende Voraussetzungen vorliegen:
1. In der dwh.cfg müssen Login-Daten für einen aktiven AWS Redshift-Cluster vorhanden sein
2. Es muss im dwh.cfg eine ARN vorhanden sein
3. Die mit der ARN verbundene IAM-Rolle muss ein Zugriffsrecht auf den S3 haben

Sobald die Voraussetzungen erfüllt sind müssen folgende Schritte ausgeführt werden:
1. Ausführen von sql_queries.py (Terminal oder Python-Konsole)
2. Ausführen von create_tables.py (Terminal oder Python-Konsole)
3. Ausführen von etl.py (Terminal oder Python-Konsole)



Beschreibung der Daten

Die in der Datei "Star-Schema" dargestellte Datenbank besteht aus fünf Tabellen. Die Faktentabelle Songplays enthält die einzelnen Songplay-Ereignisse. Neben der Faktentabelle existieren vier weitere Dimensionstabellen. Diese enthalten die normalisierten Daten der Benutzer, Künstler, Songs und der Zeitstempel.
